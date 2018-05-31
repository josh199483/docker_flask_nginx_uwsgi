# build image
docker build -t flask_image ./flask --no-cache

docker build -t nginx_image ./nginx --no-cache

# tcp socket
docker network create --driver bridge bis_network

docker run -d -p 80:80 -v ~/bis/nginx/log:/var/log/nginx --network=bis_network nginx_image

docker run -it -p 5001:5001 -v ~/bis/flask:/app --link nginx:nginx --name flask flask_image /bin/bash    uwsgi --ini uwsgi_test.ini

# unix socket
# 全部指令都打
docker run -d -v my_volume:/tmp -v ~/bis/flask:/app --name=flask flask_image uwsgi --ini uwsgi.ini

# 指定要run哪一個ini檔，因為dockerfile裡有定義entrypoint、CMD可以在啟動容器時更改參數
docker run -d -v my_volume:/tmp -v ~/bis/flask:/app --name=flask flask_image uwsgi.ini

# 背景執行nginx
docker run -d -p 80:80 -v my_volume:/tmp -v ~/bis/nginx/log:/var/log/nginx --name=nginx nginx_image

# mongo
docker run --name mongo -d mongo