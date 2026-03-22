# 🚀 AWS Flask Deployment — Dockerised Portfolio on EC2

A Python Flask portfolio web app **fully Dockerised and deployed on AWS EC2** — with IAM security, S3 integration, CloudWatch monitoring, and an automated GitHub Actions CI/CD pipeline.

🌍 **Live App:** `http://13.233.47.153:5000`

---

## 🏗️ Architecture

```
Developer (VS Code)
        │
        │ git push
        ▼
   GitHub Repository
        │
        │ GitHub Actions triggers automatically
        ▼
   Docker Image Built
        │
        │ docker push
        ▼
   Docker Hub (msvasanth/vasanth-flask-app)
        │
        │ docker pull
        ▼
   AWS EC2 Instance (Mumbai — ap-south-1)
        │
        ├── IAM Role attached (S3 + CloudWatch access)
        ├── Security Group (port 5000 open)
        ├── S3 Bucket (reads message.txt)
        └── CloudWatch (CPU alarm at 80%)
        │
        ▼
   App Live on Internet 🌍
```

---

## ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python + Flask | Web application |
| Docker | Containerisation |
| Docker Hub | Container registry |
| AWS EC2 | Cloud server (t3.micro, Mumbai) |
| AWS IAM | Security — roles, users, policies |
| AWS S3 | File storage — reads `message.txt` |
| AWS CloudWatch | Monitoring — CPU alarm at 80% |
| GitHub Actions | CI/CD — auto build and push on every commit |

---

## 📁 Project Structure

```
aws-docker-flask-deploy/
│
├── app.py                          ← Flask web app (portfolio + S3 reader)
├── requirements.txt                ← Python dependencies (flask, boto3)
├── Dockerfile                      ← Container build instructions
├── .github/
│   └── workflows/
│       └── deploy.yml              ← GitHub Actions CI/CD pipeline
└── README.md                       ← This file
```

---

## 🐳 Docker

### Build locally
```bash
docker build -t vasanth-flask-app .
```

### Run locally
```bash
docker run -p 5000:5000 vasanth-flask-app
```

### Pull from Docker Hub
```bash
docker pull msvasanth/vasanth-flask-app
```

---

## ☁️ AWS Setup

### EC2 Instance
- **Type:** t3.micro (Free tier eligible)
- **OS:** Amazon Linux 2023
- **Region:** Asia Pacific — Mumbai (ap-south-1)
- **Public IP:** 13.233.47.153

### IAM
- Created IAM user `vasanth-app-user` with S3 + CloudWatch policies
- Created IAM role `vasanth-ec2-role` attached to EC2 instance
- EC2 accesses S3 securely via IAM role — no hardcoded credentials ✅

### Security Group — Inbound Rules
| Port | Protocol | Source |
|---|---|---|
| 22 | SSH | Anywhere |
| 5000 | TCP | Anywhere (0.0.0.0/0) |

### S3
- Bucket: `vasanth-flask-bucket`
- File: `message.txt`
- Accessed at: `http://13.233.47.153:5000/s3`
- EC2 reads from S3 using IAM role — no public access on bucket ✅

### CloudWatch
- Metric: CPUUtilization
- Alarm: `vasanth-cpu-high` — triggers when CPU > 80%
- Notification: Email alert via SNS

---

## 🔄 CI/CD Pipeline

Every `git push` to `main` branch automatically:

1. ✅ Checks out the code
2. ✅ Logs into Docker Hub
3. ✅ Builds the Docker image
4. ✅ Pushes to Docker Hub

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Login to Docker Hub
        run: echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
      - name: Build Docker image
        run: docker build -t msvasanth/vasanth-flask-app .
      - name: Push to Docker Hub
        run: docker push msvasanth/vasanth-flask-app
```

**GitHub Secrets required:**
- `DOCKER_USERNAME` — Docker Hub username
- `DOCKER_PASSWORD` — Docker Hub access token

---

## 🚀 Deploy on EC2 (Manual steps after CI/CD push)

SSH into EC2 and run:

```bash
sudo docker pull msvasanth/vasanth-flask-app
sudo docker stop $(sudo docker ps -q)
sudo docker run -d -p 5000:5000 msvasanth/vasanth-flask-app
```

---

## 📍 App Routes

| Route | Description |
|---|---|
| `/` | Portfolio homepage |
| `/health` | Health check endpoint |
| `/s3` | Reads and displays message from S3 bucket |

---

## 📸 Screenshots

### Portfolio App Live on EC2
> `http://13.233.47.153:5000`

### S3 Integration
> `http://13.233.47.153:5000/s3`

### GitHub Actions Pipeline
> Actions tab → Build and Push Docker Image ✅

### CloudWatch CPU Alarm
> CloudWatch → Alarms → vasanth-cpu-high

---

## 👨‍💻 Author

**Vasanth M**
Observability Platform Engineer @ PayPal (via TCS)
- 📧 vishnuvasanth9669@gmail.com
- 💻 [github.com/VishnuVasi](https://github.com/VishnuVasi)
- 🌐 [Portfolio](https://portfolio-five-coral-ttj0dlg86a.vercel.app/)
