FROM python:3.10-buster

ENV FLASK_ENV=production 
ENV PROD_DATABASE_URI=""
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/flaskapp/.local/bin
ENV DB_HOST = 
ENV DB_USER =
ENV DB_PASSWORD =
ENV DB_NAME =
ENV DB_PORT =

#crea usuario
RUN useradd --create-home --home-dir /home/flaskapp flaskapp

#seleccionar la carpeta de usuario
WORKDIR /home/flaskapp
#instala dependencias del sistema
RUN apt-get update
RUN apt-get install -y curl gcc g++ libffi-dev libssl-dev build-essential default-mysql-client python3-mysqldb libmariadb-dev
# RUN apt-get install -y inetutils-ping
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
RUN rm -rf /var/lib/apt/lists/*

# aca se termina el root

USER flaskapp
RUN mkdir app
#copia la carpeta del proyecto a la imagen
COPY ./app.py .

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gevent gunicorn==20.1.0

#puerto por el que escucha la imagen
EXPOSE 5000

#HEALTHCHECK --interval=10s --timeout=10s --start-period=55s 
#CMD curl -f --retry 10 --max-time 15 --retry-delay 10 --retry-max-time 60 "http://localhost:5000/api/v1/health" || exit 1   

#ejecuta la aplicación
#CMD ["gunicorn", "--workers", "1", "--log-level", "INFO", "--bind", "0.0.0.0:5000", "app:create_app()"]
CMD [ "python", "./app.py" ]