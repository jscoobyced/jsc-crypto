FROM --platform=linux/amd64 python:latest

# Prepare environment
ARG JSC_CRYPTO=/opt/jsc_crypto
ARG JSC_CRYPTO_DATA=/opt/jsc_crypto/data
RUN mkdir -p ${JSC_CRYPTO_DATA}
WORKDIR ${JSC_CRYPTO}
RUN pip3 install requests

# Install files
COPY jsc_crypto/jsc_ticker.py .
COPY jsc_crypto/ticker.py .
COPY start.sh .
RUN chmod u+x start.sh

VOLUME ${JSC_CRYPTO_DATA}
EXPOSE 8888

CMD ["./start.sh"]