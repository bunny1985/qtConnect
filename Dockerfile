FROM sanicframework/sanic:LTS

RUN mkdir /app

EXPOSE 8000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

CMD [ "python", "/app/main.py" ]
