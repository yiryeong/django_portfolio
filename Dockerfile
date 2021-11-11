# ubuntu:18.04의 이미지로 부터
FROM ubuntu:18.04


RUN apt-get update -y
RUN apt-get install git -y


# github 에 소스코드 받기
RUN git clone https://github.com/yiryeong/django_portfolio.git
WORKDIR /django_portfolio


# 필요한 환경 설치
RUN apt-get install -y python3 python3-pip build-essential
RUN pip3 install -r requirements.txt


EXPOSE 6000
# container가 구동되면 실행
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:6000"]
