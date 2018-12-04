FROM python:3.6

WORKDIR /var/www

RUN pip install django
RUN pip install djangorestframework
RUN pip install django-filter
RUN pip install PyMySQL
