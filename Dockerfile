FROM python:3.9.8
ENV PYTHONBUFFERED=1
WORKDIR /usr/src/fastapi
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
