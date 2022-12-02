FROM ubuntu:18.04

RUN apt-get -qq update && \
    apt-get -qq install git python3.8 python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

RUN python3 -m venv /mnt/scheduler
RUN . /mnt/scheduler/bin/activate && \
    pip3 install -e git+https://github.com/shclub/ndscheduler.git#egg=ndscheduler && \
    pip3 install -r /mnt/scheduler/src/ndscheduler/simple_scheduler/requirements.txt

ADD simple_scheduler/docker/apns.pem /mnt/scheduler/
ADD simple_scheduler/docker/run_scheduler /mnt/scheduler/bin/run_scheduler
RUN chmod 755 /mnt/scheduler/bin/run_scheduler

CMD ["/mnt/scheduler/bin/run_scheduler"]
