#!/bin/bash

minikube start --vm=true --kubernetes-version=v1.18.1
# wait for all pods
minikube addons enable ingress
# wait for ingress pods
docker build -t flask_app:latest .
docker tag flask_app:latest flask_app:0.1.0
helm package flask-app
helm install flask-app-hello flask-app-0.0.1.tgz
