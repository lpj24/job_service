FROM ubuntu
WORKDIR /usr/local/job_service
COPY ./requirements.txt ./
RUN apt-get update && apt-get -y install python-setuptools python-dev libmysqlclient-dev python-pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
EXPOSE 5900
CMD ["python", "manage.py", "runserver", "0.0.0.0:5900"]

# docker run -d -p 5555:5555 -v /home/lpj/Documents/nginx.conf:/etc/nginx/nginx.conf -v /home/lpj/dist:/usr/local/dist --net=host --name=job_vue nginx

# nginx
