FROM python:3.10-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy other files for running
COPY . .

# Run the app
CMD ["sh", "start.sh"]
