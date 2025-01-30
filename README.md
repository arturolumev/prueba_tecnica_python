# Sistema de Procesamiento y Visualización de Datos

## Requisitos

1. Python 3.x
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux
   venv\Scripts\activate     # Windows
3. Instalar las dependencias
   pip install -r requirements.txt
4. Configurar las variables de entorno:
   AWS_ACCESS_KEY_ID
   AWS_SECRET_ACCESS_KEY
   AWS_BUCKET_NAME
   AWS_REGION
   DATABASE_URL (opcional para usar SQLite)

## Ejecución

1. Ejecutar las migraciones:
   flask db init
   flask db migrate -m "Create sales table"
   flask db upgrade
2. Iniciar la aplicación:
   python run.py
3. Acceder a los endpoints:
   POST /load_data: Cargar datos desde un CSV.
   GET /generate_report: Generar y almacenar el gráfico.
   GET /filter_sales: Filtrar ventas por rango de fechas.