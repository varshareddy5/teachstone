FROM ubuntu:22.04
RUN useradd -m mytest

WORKDIR /app

RUN apt-get update && apt-get install -y vim python3 python3-pip supervisor wget
RUN pip install requests
RUN pip install datetime

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY report-generator.py /usr/local/bin/report-generator.py

RUN chmod 755 /usr/local/bin/report-generator.py
RUN chown mytest:mytest /app


USER mytest
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
