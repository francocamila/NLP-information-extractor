FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /pdf_keywords && apt-get update && apt-get install -y postgresql \
                           postgresql-client \
                           libpq-dev

WORKDIR /pdf_keywords
COPY requirements.txt /pdf_keywords/
RUN pip install -r requirements.txt
COPY . /pdf_keywords