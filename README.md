# Birthday-Greeting-Kata

## 建置流程

```
# 建立 Docker Bridge Network
docker network create kata-api

# 部署服務
docker docker-compose up

# 如果找不到靜態檔案時，把靜態檔案蒐集到 STATIC_ROOT 中
docker exec kata_api python kata/manage.py collectstatic
```

## 初始化資料

```
docker exec kata_api python kata/manage.py makemigrations
docker exec kata_api python kata/manage.py migrate

docker exec kata_api python kata/manage.py createsuperuser
```

接著就能透過設定的帳密登入[後台](http://localhost:9001/admin)，進行用戶資料的新增

## 執行單元測試

請先至 settings.py 將 DATABASES 換至測試

```
docker exec kata_api python kata/manage.py api.tests
```

###### 標籤: `Django` `Django REST framework` `Interview`