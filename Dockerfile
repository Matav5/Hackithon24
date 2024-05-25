FROM python:latest

WORKDIR /srv

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /srv
ENV FLASK_APP=app
CMD ["python","main.py"]