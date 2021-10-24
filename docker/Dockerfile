FROM python:3.8-buster

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y  apt-utils python3-dev python3-setuptools \
                        gcc libc-dev \
                        libffi-dev libssl-dev musl-dev && \
    pip install --upgrade pip \
    mkdir /blog 


COPY requirements.txt /blog/requirements.txt

RUN pip install --no-cache -r /blog/requirements.txt && \
    useradd -s /bin/bash user && 

WORKDIR /blog

RUN chown -R user /blog

USER user

CMD ["/bin/bash"]
