FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN conda env create -f environment.yml
EXPOSE 5000
CMD ["python", "run.py"] 