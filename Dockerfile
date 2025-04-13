FROM ubuntu

RUN apt-get update
RUN apt-get -y install bash iproute2 net-tools tcpdump vim iputils-ping
RUN apt-get clean

COPY configure-scripts /configure-scripts
CMD ["bash"]
