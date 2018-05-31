FROM python:3.6
LABEL maintainer joshua
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY . /app
#EXPOSE 5001
VOLUME /app
RUN pip install -r requirements.txt
RUN mv flask.service /etc/systemd/system/
ENTRYPOINT ["uwsgi","--ini"]
CMD ["uwsgi.ini"]

