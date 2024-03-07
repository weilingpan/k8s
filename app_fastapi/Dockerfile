FROM ubuntu:20.04

# Install Miniconda
RUN apt-get update && \
    apt-get install -y wget && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-latest-Linux-x86_64.sh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Add conda to the PATH environment variable
ENV PATH=/opt/conda/bin:$PATH

# Create a new conda environment
COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the conda environment
ENV PATH /opt/conda/envs/myenv/bin:$PATH
RUN /bin/bash -c "source activate myenv"

# Set the working directory in the container
WORKDIR /app

# Copy the FastAPI application files to the container
COPY . /app

# Expose the port on which the FastAPI application will run
EXPOSE 80

# Command to run the FastAPI application using uvicorn
CMD ["python", "main.py"]

#docker build -t fastapi-prometheus-example .
#docker run -d --name fastapi-prometheus-example -p 8000:8000 fastapi-prometheus-example


#   minikube docker-env
#   eval $(minikube -p minikube docker-env)
#   minikube image ls --format table
#   minikube image ls --format table | grep example
#   docker build -t fastapi-prometheus-example .
#   minikube image ls --format table | grep example


