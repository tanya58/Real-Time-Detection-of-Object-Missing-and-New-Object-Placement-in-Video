# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies (include any libraries your project needs, like OpenCV, NumPy, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port for the container to communicate (if necessary)
EXPOSE 8080

# Command to run the application (replace with your actual script if needed)
CMD ["python", "main.py"]
