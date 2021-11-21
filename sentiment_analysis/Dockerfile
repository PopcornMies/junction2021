FROM python:3.8

##WORKDIR 

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN ["python3", "nltk_downloader.py"]

#CMD ["python3", "analyze_sound.py", "worried.wav"]