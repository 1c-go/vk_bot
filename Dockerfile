FROM python:3.7-slim
ADD main.py /
RUN pip install vk_api
CMD [ "python", "main.py" ]
