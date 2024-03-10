kubectl apply -f deploy/deployment.yaml
kubectl apply -f deploy/serviceMonitor.yaml
kubectl wait --for=condition=ready pod -l module=fastapi-example
kubectl port-forward -n=default svc/fastapi-prometheus-example-nodeport 30390:8000