FROM python:3.10-slim
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD python3 bot.py
{
  "build": {
    "commands": "npm install"
  },
  "start": {
    "commands": "npm start"
  }
}
