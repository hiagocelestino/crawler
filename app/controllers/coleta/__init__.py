from flask import Blueprint, jsonify, request, Response
from app.crawlers.crawler_extra_clube import CrawlerExtraClube
BLUEPRINT = Blueprint('coleta', __name__)

@BLUEPRINT.route('/coleta', methods=['POST'])
def get_coleta():
    req = request.get_json()
    scrapy = CrawlerExtraClube(**req)
    try:
        scrapy.run_scrapy()
        retorno = scrapy.consulta._consulta_dict()
    except Exception as e:
        retorno = {
            'msg': 'Falha ao realizar consulta'
        }

    return jsonify(retorno)

@BLUEPRINT.route('/coleta', methods=['GET'])
def get_resultado_coleta():
    return jsonify({

    })
