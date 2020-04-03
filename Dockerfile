FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000/tcp

CMD [ "python3", "muddy.py" ]