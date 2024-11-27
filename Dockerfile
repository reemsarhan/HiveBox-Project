# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any needed dependencies
RUN pip install --no-cache-dir Flask

# Step 5: Expose port 5000 to be accessible outside the container
EXPOSE 5000

# Step 6: Define environment variable for Flask app
ENV FLASK_APP=main.py

# Step 7: Run the Flask app in production mode when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
