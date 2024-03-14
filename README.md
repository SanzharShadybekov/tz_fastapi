# Bet Maker FastApi service
## Test Project on FastApi, SQlAlchemy, PostgreSQL
### Deploy and start project on AWS Ubuntu instance
* **Clone project from git repository**
```
git clone "your_repos_ssh_or_http_url"
```
Moving to project dir 
```
cd "directory"
```
* **Installing docker in ubuntu 20/22 instance** 
```
sudo apt update && sudo apt upgrade -y
sudo apt install ca-certificates curl gnupg lsb-release unzip
```
Add Docker’s GPG key
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
Add official docker repo
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```
Installing docker
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Adding user to docker group
```
sudo usermod -aG docker $USER
id $USER
newgrp docker
```
Installing docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
Checking docker and docker-compose
```
docker run hello-world
docker-compose --version
```
* ### Running project docker containers
```
docker-compose up --build -d
```
Run alembic migration 
```
docker-compose exec web alembic upgrade head
```

* **Docs: [http://0.0.0.0/docs/](http://0.0.0.0/docs/)**

Add a bet:

```sh
curl -d '{"event_identifier":"event-1", "bet_amount":"10000.00"}' -H "Content-Type: application/json" -X POST http://0.0.0.0/bets/
```

Update an event:
```sh
curl -d '{"status": "won"}' -H "Content-Type: application/json" -X PUT http://0.0.0.0/events/event-1/
```

* **Get all bets: [http://0.0.0.0/bets/](http://0.0.0.0/bets/)**

