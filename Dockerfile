FROM python:3.11

ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt . 
RUN pip install -r requirements.txt

COPY . .

COPY migration.sh /migration.sh
RUN chmod +x /migration.sh

ENTRYPOINT ["/migration.sh"]
