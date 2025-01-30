from flask import Flask, jsonify, request
# from app import db
from . import db
from app.models import Venta
from app.utils import generate_sales_bar_chart
from app.tasks import load_sales_data_from_csv

# app = Flask(__name__)

def init_routes(app):
    @app.route('/load_data', methods=['POST'])
    def load_data():
        file = request.files['csv']
        load_sales_data_from_csv(file)
        return jsonify({"message": "Datos cargados exitosamente"}), 200

    @app.route('/generate_report', methods=['GET'])
    def generate_report():
        url = generate_sales_bar_chart()
        return jsonify({"report_url": url}), 200

    @app.route('/filter_sales', methods=['GET'])
    def filter_sales():
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        sales = Venta.query.filter(Venta.fecha.between(start_date, end_date)).all()
        return jsonify([{'producto': sale.producto, 'cantidad': sale.cantidad, 'precio': sale.precio, 'fecha': sale.fecha} for sale in sales]), 200

    if __name__ == '__main__':
        app.run(debug=True)
