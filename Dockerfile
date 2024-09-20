FROM python:3.12-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set the working directory to where the app.py is located
WORKDIR /usr/src/app/src/app

# Expose the port your app will run on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
