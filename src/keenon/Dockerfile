 FROM python:3

 ENV PYTHONUNBUFERED 1

 WORKDIR /app

 ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN echo  $'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nInstalling requirements...........\n'
RUN pip install -r requirements.txt

RUN echo  $'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nProject SyntaxCheck...........\n'
RUN python manage.py check

RUN echo  $'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nExecuting Tests...........\n'
RUN python manage.py test


COPY . /app
