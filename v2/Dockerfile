FROM apache/airflow:2.8.2
COPY requeriments.txt /requeriments.txt
# Copie a pasta Functions para o contêiner -> fiz isso no docker-compose
# COPY src /usr/local/airflow/src
RUN pip install --user --upgrade pip
RUN pip install pandas psycopg2-binary python-dotenv
RUN pip install --no-cache-dir --user -r /requeriments.txt