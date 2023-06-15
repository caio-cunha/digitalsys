FROM python:3.11

WORKDIR /src/app

COPY requirements.txt /src/app/

RUN apt-get update  && apt -y install gdal-bin && apt-get install -y gettext

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt 

COPY . /src/app/
COPY ./docker /src/app/

RUN mkdir -p /src/logs
RUN mkdir -p /src/app/static

RUN chmod -R 100 /src/app/entrypoints/

EXPOSE 8000