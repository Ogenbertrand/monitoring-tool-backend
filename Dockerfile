# Use Python 3.12 slim version
FROM python:3.12-slim


WORKDIR /src


COPY requirements.txt /src/


RUN pip install --no-cache-dir -r /src/requirements.txt

COPY src/app.py /src/


EXPOSE 5050

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5050

CMD ["flask", "run"]
