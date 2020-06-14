FROM python:latest

# Debian set Locale
RUN apt-get update && \
    apt-get -y install locales task-japanese && \
    locale-gen ja_JP.UTF-8 && \
    rm -rf /var/lib/apt/lists/*
ENV LC_ALL=ja_JP.UTF-8 \
    LC_CTYPE=ja_JP.UTF-8 \
    LANGUAGE=ja_JP:jp
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

# Debian set TimeZone
ENV TZ=Asia/Tokyo
RUN echo "${TZ}" > /etc/timezone && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# コンテナのデバッグ等で便利なソフト導入しておく
RUN apt-get update && \
    apt-get -y install vim && \
    apt-get -y install git && \
    apt-get -y install curl && \
    apt-get -y install wget && \
    apt-get -y install zip && \
    apt-get -y install unzip && \
    apt-get -y install ruby-dev && \
    apt-get -y install make && \
    apt-get -y install sudo && \
    apt-get -y install gcc && \
    apt-get -y install libc-dev && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install psycopg2-binary
#ADD . /usr/src/app/

CMD ["/usr/local/bin/run.sh"]

# Set entrypoint
#ENTRYPOINT ["/bin/bash", "scripts/init_mysite.sh"]
