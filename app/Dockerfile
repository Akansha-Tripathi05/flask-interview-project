FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt || pip install flask flask_sqlalchemy flask_marshmallow flask_jwt_extended pytest
EXPOSE 5000
CMD ["python", "run.py"]