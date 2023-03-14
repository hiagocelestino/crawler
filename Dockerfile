FROM python:3

RUN pip install poetry
RUN mkdir /app

WORKDIR /app

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True

EXPOSE 5000
CMD poetry install \
    && poetry run playwright install \
    && poetry run flask run -h 0.0.0.0 -p 5000 --debug