FROM alpine 
# Alpine container is bigger/slower? wtf... Need to test and replace base image!
# https://pythonspeed.com/articles/alpine-docker-python/

# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
ENV PYTHONUNBUFFERED=1

RUN apk add gcc git python3 python3-dev linux-headers libc-dev && rm -rf /var/cache/apk/*
RUN pip3 install --upgrade pip psutil
RUN git clone https://github.com/nickvsh/metrics.git ~/metrics
ENTRYPOINT ["python3","/root/metrics/metrics.py"]
CMD ["all"]
