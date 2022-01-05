FROM python:3.8-slim-buster

RUN mkdir /frontend
COPY . /frontend
WORKDIR /frontend

RUN apt-get -y update
RUN apt-get -y upgrade

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "streamlit-app.py"]