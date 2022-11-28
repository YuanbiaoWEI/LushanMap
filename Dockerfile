FROM python:3.9

MAINTAINER weiyuanbiao@whu.edu.cn

WORKDIR /home
COPY LushanMap ./LushanMap

WORKDIR /home/LushanMap

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
