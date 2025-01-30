import matplotlib.pyplot as plt
import os
from io import BytesIO
import boto3
from app.config import Config

def generate_sales_bar_chart():
    # Consulta de ventas totales por producto
    from app.models import Venta
    from app import db

    ventas = db.session.query(Venta.producto, db.func.sum(Venta.cantidad * Venta.precio).label('total_ventas')) \
                       .group_by(Venta.producto).all()

    # Generación del gráfico
    productos = [v.producto for v in ventas]
    totales = [v.total_ventas for v in ventas]

    fig, ax = plt.subplots()
    ax.bar(productos, totales)
    ax.set_xlabel('Producto')
    ax.set_ylabel('Ventas Totales')
    ax.set_title('Ventas Totales por Producto')

    # Guardar el gráfico en memoria
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Subir a S3
    s3 = boto3.client('s3', aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
                     aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
                     region_name=Config.AWS_REGION)
    
    bucket_name = Config.AWS_BUCKET_NAME
    s3.upload_fileobj(img, bucket_name, 'ventas_totales.png', ExtraArgs={'ContentType': 'image/png'})
    
    # Generar la URL pública del archivo
    url = f"https://{bucket_name}.s3.{Config.AWS_REGION}.amazonaws.com/ventas_totales.png"
    return url
