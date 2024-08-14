FROM alpine:3.17.0

RUN apk update && \
    apk add --no-cache python3 py3-pip && \

    adduser -D -u 1000 user && \
    echo "user:$(head -c 32 /dev/urandom | base64)" | chpasswd

WORKDIR /usr/app/
ADD ./src .

RUN /usr/bin/python3 -m pip install -r requirements.txt

CMD ["/usr/bin/python3", "/usr/app/app.py"]
