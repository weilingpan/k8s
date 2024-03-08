kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/serviceMonitor.yaml
kubectl wait --for=condition=ready pod -l module=flask-example 
kubectl port-forward -n=default svc/flask-prometheus-example-nodeport 30391:5000