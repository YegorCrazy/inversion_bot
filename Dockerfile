FROM python

RUN ["apt-get", "install", "python3-opencv"]
RUN ["pip", "install", "telebot"]

COPY ./inverter.py /code/inverter.py
COPY ./bot.py /code/bot.py

WORKDIR /code

CMD ["python", "bot.py"]
