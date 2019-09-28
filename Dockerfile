FROM python:3

ADD main.py /

RUN pip install vk_api
RUN pip install requests

CMD [ "python", "./main.py" ]