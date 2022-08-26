FROM python:3
COPY . /
RUN pip install kubernetes
COPY ./setup.sh /setup.sh
CMD [ "/setup.sh" ]
