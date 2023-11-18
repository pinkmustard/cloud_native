# 파이썬 버전 알파인,슬림 버스터 다 오류로 기본 파이썬 이미지 로드
FROM python:3.8.18

# 프로젝트 작업 폴더를 /usr/src/app으로 지정
WORKDIR /usr/src/app

# .pyc파일 생성하지 않게함
ENV PYTHONDONTWRITEBYTECODE 1
# 파이썬 로그가 버퍼링 없이 즉각적으로 출력하게 함
ENV PYTHONUNBUFFERED 1

# 로컬 컴퓨터의 현재 위치에 있는 파일을 모두 작업 폴더로 복사
COPY . /usr/src/app/
# 나열된 라이브러리 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt