FROM python:3.9.12
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
#CMD ["python", "-m", "unittest", "discover", "-s", "tests"]
