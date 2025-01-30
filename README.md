# Sistema de Procesamiento y Visualización de Datos

## Requisitos

1. Python 3.x
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux
   venv\Scripts\activate     # Windows
3. Instalar las dependencias
   ```bash
   pip install -r requirements.txt
4. Configurar las variables de entorno en un archivo .env:
   ```bash
   AWS_ACCESS_KEY_ID
   AWS_SECRET_ACCESS_KEY
   AWS_BUCKET_NAME
   AWS_REGION
   DATABASE_URL (opcional para usar SQLite)

## Ejecución

1. Ejecutar las migraciones:
   ```bash
   flask db init
   flask db migrate -m "Create sales table"
   flask db upgrade
2. Iniciar la aplicación:
   ```bash
   python run.py
3. Acceder a los endpoints:
   ```bash
   POST /load_data: Cargar datos desde un CSV.
   GET /generate_report: Generar y almacenar el gráfico.
   GET /filter_sales: Filtrar ventas por rango de fechas.