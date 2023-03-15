from abc import ABC, abstractmethod
from playwright.sync_api import sync_playwright
from app.repositories.consulta import ConsultaDB
from app.repositories.erros.erros_personalizados import ErrorPersistirDados

class CrawlerBase(ABC):

    def __init__(self, url, parametro_busca=None):
        self.url = url
        self.busca = parametro_busca
        self.resultado = ''
        self.consulta = None

    def start_crawler(self):
        self.playwright = sync_playwright().start()
    
    def close_crawler(self):
        self.playwright.stop()

    def create_navegador(self):
        self.navegador = self.playwright.chromium.launch(headless=True)
    
    def close_navegador(self):
        self.navegador.close()
        
    def create_page(self):
        self.page = self.navegador.new_page()
    
    def go_to_page(self, page=None):
        self.page.goto(page)
    
    @abstractmethod
    def scrapy(self):
        pass

    def run_scrapy(self):
        self.start_crawler()
        self.create_navegador()
        try:           
            self.create_page()
            self.go_to_page(self.url)
            self.scrapy()
        except Exception as e:
            print("Falha na execução da coleta de dados")
            print(e)
            raise e
        finally:
            self.salva_resultado()
            self.close_navegador()
            self.close_crawler()

    def salva_resultado(self):
        try:
            status = 'CONCLUIDO'
            if not self.resultado or len(self.resultado) < 0:
                status = 'FALHA'
            consulta = {
                'busca': self.busca,
                'resultado': self.resultado,
                'status': status
            }
            consult = ConsultaDB(consulta)
            consult.add_consulta()
            print(consult.id)
            self.consulta = consult._consulta_dict()
        except ErrorPersistirDados as e:
            print(e)
        except Exception as e:
            print(f"Erro ao salvar resultado no banco.\nErro: {e}")
