FROM python:3
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install

ENV FLASK_APP=app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True

EXPOSE 5000
CMD flask run -h 0.0.0.0 -p 5000

