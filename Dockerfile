FROM python:3.7-alpine
COPY . /Telecontact-Scraper
WORKDIR /Telecontact-Scraper

RUN apk add --no-cache --virtual .build-deps gcc musl-dev libxslt-dev && pip install lxml
RUN pip install -r requirements.txt

RUN pip install -e .

ENTRYPOINT ["telecontact-scraper","mine"] 


