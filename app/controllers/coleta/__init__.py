from flask import Blueprint, jsonify, request, Response
from app.crawlers.crawler_extra_clube import CrawlerExtraClube
BLUEPRINT = Blueprint('coleta', __name__)

@BLUEPRINT.route('/coleta', methods=['POST'])
def get_coleta():
    req = request.get_json()
    scrapy = CrawlerExtraClube(**req)
    try:
        scrapy.run_scrapy()
        retorno = scrapy.consulta
    except Exception as e:
        print(e)
        retorno = {
            'msg': 'Falha ao realizar consulta'
        }

    return jsonify(retorno)

@BLUEPRINT.route('/coleta/<id_coleta>', methods=['GET'])
def get_resultado_coleta(id_coleta):
    return jsonify({

    })
