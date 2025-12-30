# honeypot
A lightweight, containerized honeypot designed to monitor unauthorized access attempts on specific ports. When a connection attempt is detected, the system immediately sends a real-time notification to a designated Telegram chat via a bot.

### Getting Started
#### 1. Build the Image
First, build the Docker image locally using the following command:
```
docker build -t honeypot .
```
#### 2. Run the Container
Launch the honeypot in detached mode with automatic restart enabled. This command automatically injects your local host IP into the environment and uses the host network stack to monitor ports:
```
docker run --restart=always \
  --env-file .env \
  -e HOST_IP=$(hostname -I | awk '{print $1}') \
  -d --net host \
  honeypot
```
