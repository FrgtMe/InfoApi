FROM python:3.9

WORKDIR /APP

COPY . /APP

RUN pip install flask pyrogram tgcrypto

ENTRYPOINT ["python", "app.py"]
