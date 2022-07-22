FROM python

RUN ["pip", "install", "pyTelegramBotAPI", "numpy", "pillow"]

COPY ./inverter.py /code/inverter.py
COPY ./bot.py /code/bot.py

WORKDIR /code

CMD ["python", "bot.py"]
