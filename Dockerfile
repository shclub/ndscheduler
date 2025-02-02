FROM ubuntu:18.04

MAINTAINER Wenbin Fang <wenbin@nextdoor.com>

RUN apt-get -qq update && \
    apt-get -qq install python3  python3-pip  git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#    apt-get -qq install python-virtualenv git && \

RUN pip3 install virtualenv

RUN virtualenv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/shclub/ndscheduler.git#egg=ndscheduler && \
    pip install -r /mnt/scheduler/src/ndscheduler/simple_scheduler/requirements.txt
    
ADD simple_scheduler/docker/apns.pem /mnt/scheduler/
ADD simple_scheduler/docker/run_scheduler /mnt/scheduler/bin/run_scheduler

RUN chmod 755 /mnt/scheduler/bin/run_scheduler

RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && echo Asia/Seoul > /etc/timezone

CMD ["/mnt/scheduler/bin/run_scheduler"]
