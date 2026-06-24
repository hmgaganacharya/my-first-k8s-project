# ☸️ Cloud-Native DevOps Hub: My First End-to-End Kubernetes & CI/CD Pipeline

A hands-on, production-ready DevOps implementation demonstrating how to containerize, orchestrate, and automate a web application using modern cloud-native methodologies. 

This project bridges the gap between raw code and automated infrastructure by integrating **Docker** for containerization, **Kubernetes** for cluster orchestration, and **GitHub Actions** for continuous integration.

---

## 🏗️ Architecture Blueprint

```text
  [ Developer Push ] 
          │
          ▼
┌──────────────────┐      ┌───────────────┐
│  GitHub Actions  │ ───> │  Docker Hub   │ (Automated Image Registry)
└──────────────────┘      └───────┬───────┘
                                  │ (Pulls latest image)
                                  ▼
                        ┌──────────────────┐
                        │   Minikube K8s   │
                        │     Cluster      │
                        └────────┬─────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
       ┌──────────────────┐            ┌──────────────────┐
       │   Pod 1 (App)    │            │   Pod 2 (App)    │
       └──────────────────┘            └──────────────────┘
                 ^                               ^
                 └───────────────┬───────────────┘
                                 │ (Load Balanced)
                           [ K8s Service ]
                                 ▲
                                 │ (Exposes Port 30001)
                           [ Web Browser ]

🛠️ Tech Stack & Skills Demonstrated
Containerization: Docker, Dockerfiles, Container Networking, Port Mapping.

Orchestration (Kubernetes): Deployments, ReplicaSets (2x active app redundancy), NodePort Services, Cluster Management via kubectl.

CI/CD Automation: GitHub Actions Workflows, Secrets/Token management, Automated remote builds.

Infrastructure Background: Windows Subsystem for Linux (WSL2), local environment virtualization.

📂 Project Structure
Plaintext
├── .github/workflows/
│   └── ci-cd.yml         # GitHub Actions automated build pipeline
├── app.py                # Python web application source code
├── Dockerfile            # Container blueprint for packaging the application
├── deployment.yml        # Kubernetes declarative deployment configuration
├── service.yml           # Kubernetes network exposure routing mapping
└── README.md             # Project documentation
🚀 How to Run this Project Locally
1. Prerequisites
Ensure you have the following installed on your machine:

Docker Desktop

Minikube + kubectl

2. Boot up the Cluster
Bash
minikube start
3. Deploy the Manifests
Clone this repository, navigate to the folder, and run:

Bash
kubectl apply -f deployment.yml
kubectl apply -f service.yml
4. Verify Pod Status
Check to ensure both application replicas are healthy and scaling properly:

Bash
kubectl get pods
5. Access the Web Application
Launch the application instantly through Minikube's built-in network proxy:

Bash
minikube service my-app-service
🔄 Automated CI/CD Lifecycle
Whenever code is committed directly to the main branch of this repository:

A GitHub Actions runner triggers an isolated build environment.

The pipeline authenticates securely with Docker Hub utilizing encrypted credentials.

The newer application version builds, tags itself as latest, and pushes directly to the cloud image container registry.
