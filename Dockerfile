FROM python:3.9

RUN apt-get update && apt-get install -y \
	unixodbc \
	unixodbc-dev \
	tdsodbc
RUN apt-get install -y freetds-common freetds-bin freetds-dev


ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]