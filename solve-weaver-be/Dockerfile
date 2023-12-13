
FROM python:3.12.1-slim 

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the source code into the container.
COPY ./src /app/src

# Run the application.
#CMD gunicorn 'venv.lib.python3.12.site-packages.fastapi.middleware.wsgi' --bind=0.0.0.0:8000
RUN echo "starting gunicorn on 8000..."

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]