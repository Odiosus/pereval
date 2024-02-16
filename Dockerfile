FROM python:3.10-alpine3.19


WORKDIR /pereval
COPY requirements.txt /temp/requirements.txt
COPY . /pereval

EXPOSE 8000
RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password test-user

USER test-user

#CMD [ "python", "manage.py", "migrate" ]
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
