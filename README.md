# django_tutorial

## djangoの生成
```bash
docker-compose build
docker-compose run web_django django-admin startproject config .
```

## データベースの作成
```bash
docker-compose run web_django python3 manage.py migrate
```

## 全部をきちんと整理しておくため、プロジェクトの中に別のアプリケーションを作ります。
```bash
docker-compose run web_django python3 manage.py startapp blog
```