FROM python:3.12.0-alpine3.17

WORKDIR /code/

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./sodimac/ /code/sodimac/

# Ejecutar las pruebas con pytest
CMD ["pytest", "./sodimac/tests/test_casos_de_uso.py"]
