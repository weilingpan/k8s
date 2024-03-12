eval $(minikube -p minikube docker-env)

docker build -t fastapi-prometheus-example:v0.0.8.pid .
# docker run -d --name fastapi-prometheus-example -p 8000:8000 fastapi-prometheus-example
