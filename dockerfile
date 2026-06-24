# Step 1: Use an official light-weight Python environment
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy our app.py file into the container
COPY app.py .

# Step 4: Tell the container to expose port 5000
EXPOSE 5000

# Step 5: The command to run when the container starts
CMD ["python", "app.py"]