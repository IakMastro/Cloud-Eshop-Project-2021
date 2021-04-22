# Python version 3.7 from Alpine
FROM python:3.7-alpine

# Path on container
WORKDIR /users

# Enviroment variables
ENV FLASK_APP=users.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install additional modules
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Expose the port 5000
EXPOSE 5000
COPY users.py .

# Run the app
CMD ["flask", "run"]