# pixel-artist-backend

## How to run?
  
  1. docker network create pixel-artist-dev-net
  2. docker-compose up -d --build

## debug(in Docker):
  
  2. docker exec -it pixel-artist-backend bash
  3. flask run --host=0.0.0.0 --port=10000
    
## Deploy to minikube
  * [] <- for Optional cmd
  * {} <- customed
  - Install minikube
  - minikube start —driver=docker
  - [kubectl create namespace pixel-dev]
  - docker build -t pixel-to-minikube:1.0.1 .
  - minikube image load  pixel-to-minikube:1.0.1
  - kubectl apply -f ./deployment/deployment.yaml [-n pixel-dev]
    - kubectl get services --all-namespaces
  - minikube service  {service-name} —url [-n pixel-dev]

## Others
  - 為了養成好的開發習慣，我並沒有公開table的columns的名稱，所以若有需要使用請務必告訴我(If you wanna run the app, send a mail to me)。
