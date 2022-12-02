FROM ubuntu:14.04

RUN apt-get -qq update && \
    apt-get -qq install python-virtualenv git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN virtualenv /mnt/scheduler && \
    . /mnt/scheduler/bin/activate && \
    pip install -e git+https://github.com/shclub/ndscheduler.git#egg=ndscheduler && \
    pip install -r /mnt/scheduler/src/shclub/simple_scheduler/requirements.txt

ADD simple_scheduler/docker/apns.pem /mnt/scheduler/
ADD simple_scheduler/docker/run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

CMD ["/mnt/scheduler/bin/run_scheduler"]
