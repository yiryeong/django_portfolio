# ubuntu:18.04의 이미지로 부터
FROM ubuntu:18.04


# 필요한 환경 설치
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN pip3 install django
RUN pip3 install djangorestframework
RUN pip3 install markdown
RUN pip3 install django-filter
RUN pip3 install mysqlclient
RUN pip3 install drf-yasg


# github 에 소스코드 받기
Run git clone https://github.com/yiryeong/django_portfolio.git
WORKDIR /django_portfolio


# container가 구동되면 실행
ENTRYPOINT ["python3", "manage.py", "runserver", "6000"]
