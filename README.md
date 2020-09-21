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
docker exec -it web_django python3 manage.py startapp blog
```

### モデルを作ったあとに
```
docker exec -it web_django python3 manage.py makemigrations blog
docker exec -it web_django python3 manage.py migrate blog
```

# 管理画面のスーパーユーザーの作成
```
docker exec -it web_django python3 manage.py createsuperuser
```

### Django Shell
```
docker exec -it web_django python3 manage.py shell
```