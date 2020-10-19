#!/bin/bash

# minikube start --vm=true --kubernetes-version=v1.18.1
# wait for all pods
# minikube addons enable ingress
# wait for ingress pods

helm uninstall flask-app-backend

docker build -t flask_app:latest .
docker tag flask_app:latest registry.gitlab.com/realsystem/flask_app:0.1.0
docker push registry.gitlab.com/realsystem/flask_app:0.1.0

helm package flask_app
helm install flask-app-backend flask-app-0.0.1.tgz

# wait for flask-app-backend pods
# add new record for /etc/hosts: <NODE IP> flask-app.io
# verify application
# curl -v flask-app.io
