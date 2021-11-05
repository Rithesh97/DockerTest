FROM python:3
WORKDIR /app
COPY . /app
EXPOSE 5001
RUN pip install -r requirements.txt
CMD [ "python", "./flaskapp.py" ]
