from app import db
from app.models import Venta
import pandas as pd
from datetime import datetime

def load_sales_data_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        # venta = Venta(producto=row['producto'], cantidad=row['cantidad'], precio=row['precio'], fecha=row['fecha'])
        venta = Venta(producto=row['producto'], cantidad=row['cantidad'], precio=row['precio'], fecha=datetime.strptime(row['fecha'], '%Y/%m/%d').date())

        db.session.add(venta)
    db.session.commit()
