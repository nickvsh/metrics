Summary
=======

**metrics.py** is a Python script which shows **useful monitoring information** about your server.

Under the hood it uses [psutil](https://github.com/giampaolo/psutil) - a cross-platform library for retrieving information on 
**running processes** and **system utilization** (CPU, memory, disks, network, sensors) in Python.

At the moment metrics.py supports only CPU and Memory metrics. But it is not the end)

Example of usage
==============

```
python3 metrics.py --help

Usage: python3 metrics.py [OPTION]
Shows useful server metrics

Mandatory arguments to long options are mandatory for short options too.
  help, --help, -h                print this help info
  all, --all, -a                  show ALL available metrics
  cpu, --cpu, -c                  show CPU metrics
  mem, --mem, -m                  show Memory metrics
  ... to be continued
```

### CPU

```
$ python3 metrics.py cpu

system.cpu.idle 5453.69
system.cpu.user 829.33
system.cpu.guest 0.0
system.cpu.iowait 7.14
system.cpu.stolen 0.0
system.cpu.system 131.74
```

### MEMORY

```
$ python3 metrics.py mem

virtual total 5631401984
virtual used 2467139584
virtual free 730787840
virtual shared 338530304
swap total 595619840
swap used 0
swap free 595619840
```

Installation on Linux
==============
To install metrics.py just do the following:

**Ubuntu / Debian**

    sudo apt-get install -y gcc python3 python3-pip python3-dev git
    pip3 install psutil

**RedHat / CentOS**

    sudo yum install -y gcc python3 python3-pip python3-devel git
    pip3 install psutil

**Just Go Johnny go**

    git clone https://github.com/nickvsh/metrics.git ~/metrics 
    python3 ~/metrics/metrics.py --help


Docker
==============
For those who are familiar with docker.
You can build the docker image from [Dockerfile](https://github.com/nickvsh/metrics/blob/master/Dockerfile) with:
    
    git clone https://github.com/nickvsh/metrics.git ~/metrics
    cd ~/metrics
    docker build -t nickvsh/metrics .
    docker run -it --rm --pid=host -v /etc/passwd:/etc/passwd nickvsh/metrics
    
OR

Simply run image from [dockerhub](https://hub.docker.com/repository/docker/nickvsh/metrics) like this:

##### shows all available metrics

    docker run -it --rm --pid=host -v /etc/passwd:/etc/passwd nickvsh/metrics 

##### shows shows help info

    docker run -it --rm --pid=host -v /etc/passwd:/etc/passwd nickvsh/metrics help

