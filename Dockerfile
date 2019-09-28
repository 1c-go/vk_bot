FROM python:3

ADD main.py /

RUN pip install vk_api

CMD [ "python", "./main.py" ]