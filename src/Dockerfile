FROM python:3.8-alpine as base

# Installs graphviz
RUN apk add --update --no-cache \
            graphviz \
            ttf-freefont


RUN mkdir /app

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

COPY app.py /app/app.py

WORKDIR /app
# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py"]
#CMD ["python", "-m flask run"]