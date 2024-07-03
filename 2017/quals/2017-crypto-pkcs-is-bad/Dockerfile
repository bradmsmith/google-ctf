FROM golang:1.22.5
ADD . /go
WORKDIR /go
RUN go build -o 2017-crypto-pkcs-is-bad
CMD ["/go/2017-crypto-pkcs-is-bad"]
EXPOSE 8080
