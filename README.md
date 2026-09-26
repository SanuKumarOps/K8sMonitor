# K8sMonitor

Kubernetes CI/CD + Monitoring Pipeline built on AWS EC2.

## Tech Stack

- AWS EC2
- Docker
- Kubernetes
- Minikube
- GitHub Actions
- DockerHub
- Prometheus
- Grafana
- Helm
- Flask

## Architecture

GitHub → GitHub Actions → DockerHub → Kubernetes/Minikube → Prometheus → Grafana

## Kubernetes

- 3 replicas
- CPU and memory requests/limits
- Readiness probe
- Liveness probe
- NodePort service

## CI/CD

GitHub Actions automatically builds and pushes the Docker image to DockerHub whenever code is pushed to the main branch.

Docker image: sanukumar2/k8smonitor:latest

## Monitoring

Prometheus collects application metrics through a Kubernetes ServiceMonitor.

Grafana is connected to Prometheus for visualization and monitoring.

## Helm

The application is packaged and deployed using Helm.

## Verification

kubectl get pods
kubectl get svc
helm list

## Deployment Environment

The complete Kubernetes environment is running on an AWS EC2 instance using Minikube with the Docker driver.

## Key Learning Outcomes

- Containerized a Flask application
- Built Kubernetes Deployment and Service
- Implemented health probes and resource management
- Automated Docker image builds with GitHub Actions
- Integrated DockerHub
- Implemented Prometheus monitoring
- Visualized metrics using Grafana
- Packaged the application with Helm
