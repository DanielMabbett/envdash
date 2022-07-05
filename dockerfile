ARG VARIANT="3.8"
FROM python:${VARIANT}

LABEL maintainer=""


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# COPY docker-entrypoint.sh /
# ENTRYPOINT ["/docker-entrypoint.sh"]
# 
EXPOSE 8000
# 
# #STOPSIGNAL SIGQUIT
# 
# #CMD ["nginx", "-g", "daemon off;"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
