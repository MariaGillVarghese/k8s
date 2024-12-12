# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy all files from the current directory (including app.py)
COPY . .

# Install necessary Python packages (Pillow in this case for image handling)
RUN pip install --no-cache-dir pillow

# Set the environment variable for FILE_DIRECTORY
ENV FILE_DIRECTORY="/usr/src/app/Dir"

# Command to run the script
CMD ["python", "app.py"]
