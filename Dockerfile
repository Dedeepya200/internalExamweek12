From python:3.9-slim
workdir /app
copy requirements.txt requirements.txt
run pip install -r requirements.txt
copy . .
Expose 5003
cmd ["python", "app.py"]
