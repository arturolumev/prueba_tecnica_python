# def test_upload_csv(client):
#     response = client.post('/upload', data={'file': (io.BytesIO(b'producto,cantidad,precio,fecha\nA,10,5,2023-01-01'), 'test.csv')})
#     assert response.status_code == 201

# def test_graph_generation():
#     data = [{'producto': 'A', 'cantidad': 10, 'precio': 5}]
#     graph = generate_graph(data)
#     assert isinstance(graph, str)

import pytest
from app import app, db
from app.models import Venta

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_load_data(client):
    data = {
        'csv': (open('test_sales.csv', 'rb'), 'test_sales.csv')
    }
    response = client.post('/load_data', data=data)
    assert response.status_code == 200
    assert b'Datos cargados exitosamente' in response.data

def test_generate_report(client):
    response = client.get('/generate_report')
    assert response.status_code == 200
    assert 'report_url' in response.json

def test_filter_sales(client):
    response = client.get('/filter_sales?start_date=2024-01-01&end_date=2024-12-31')
    assert response.status_code == 200
    assert isinstance(response.json, list)
