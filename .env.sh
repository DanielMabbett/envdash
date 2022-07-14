docker build -t envdash .

docker run -it -p 8020:8020 \
     -e DJANGO_SUPERUSER_USERNAME=envdash \
     -e DJANGO_SUPERUSER_PASSWORD=somePassWordThat1MadeUp? \
     -e DJANGO_SUPERUSER_EMAIL=admin@justanexample.com \
     envdash