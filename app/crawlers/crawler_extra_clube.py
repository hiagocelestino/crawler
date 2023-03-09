
from .crawler_base import CrawlerBase

class CrawlerExtraClube(CrawlerBase):
    
    def __init__(self, user, password, documento):
        super().__init__("http://extratoclube.com.br/", documento)
        self.user = user #user
        self.password = password #password
    
    def scrapy(self):
        self.realiza_login()
        self.page.dispatch_event('#ion-overlay-1 > div.modal-wrapper.ion-overlay-wrapper.sc-ion-modal-md > app-modal-fila > ion-button', 'click')
        self.page.dispatch_event("body > app-root > app-home > ion-app > ion-menu > ion-content > ion-list > ion-item:nth-child(2)", 'click')        
        self.page.click('#extratoonline > ion-row:nth-child(2) > ion-col > ion-card > ion-button:nth-child(12)')
        self.page.click('#extratoonline > ion-row:nth-child(2) > ion-col > ion-card > ion-grid > ion-row:nth-child(2) > ion-col > ion-card > ion-item > ion-input')
        self.page.fill('#extratoonline > ion-row:nth-child(2) > ion-col > ion-card > ion-grid > ion-row:nth-child(2) > ion-col > ion-card > ion-item > ion-input > input', self.busca)
        self.page.click('#extratoonline > ion-row:nth-child(2) > ion-col > ion-card > ion-grid > ion-row:nth-child(2) > ion-col > ion-card > ion-button')

        result_consulta = self.page.query_selector_all('#extratoonline > ion-row:nth-child(2) > ion-col > ion-card > ion-grid > ion-row:nth-child(2) > ion-col > ion-card > ion-item')
        self.get_resultado_busca(result_consulta)
    
    def realiza_login(self):
        try:
            self.url = self.page.query_selector('frameset frame').get_attribute("src")
            self.go_to_page(self.url)
            self.page.click('input[name="usuario"]')
            self.page.fill('input[name="usuario"]', self.user)
            self.page.click('//*[@id="pass"]')
            self.page.fill('input[name="senha"]', self.password)
            self.page.click('button')

        except Exception as e:
            print(f"Erro ao realizar login.\nError: {e}")
    
    def get_resultado_busca(self, resultado):
        for res in resultado:
            self.resultado.append(res.inner_text())