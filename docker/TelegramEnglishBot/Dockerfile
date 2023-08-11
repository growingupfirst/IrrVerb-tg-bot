FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -U --pre aiogram
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./bot.py"]