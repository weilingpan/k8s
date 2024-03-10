eval $(minikube -p minikube docker-env)

docker build -t flask-prometheus-example:v0.0.3.errorhandler .
# docker run -d --name flask-prometheus-example -p 5000:5000 flask-prometheus-example


#   minikube docker-env
#   eval $(minikube -p minikube docker-env)
#   minikube image ls --format table | grep example
#   docker build -t fastapi-prometheus-example .
#   minikube image ls --format table | grep example