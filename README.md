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
    - The version tag needs to be changed whenever there is an update.

  - minikube image load  pixel-to-minikube:1.0.1
    - The version tag needs to be changed whenever there is an update.

  - kubectl apply -f ./deployment/deployment.yaml -n pixel-dev
    - kubectl get services --all-namespaces

  - minikube service  {service-name} —-url -n pixel-dev
    - minikube service $(echo $(kubectl get pods -n pixel-dev -o custom-columns=":metadata.name")) --url -n pixel-dev
  - kubectl exec -it {pod-name} -n pixel-dev -- /bin/sh
  - minikube service pixel-artist-backend —url -n pixel-dev

#### Minkube maintain:
  
  - kubectl rollout restart deployment  -n pixel-dev
  - kubectl get pods -n pixel-dev
  - kubectl exec -it {pod name} -n pixel-dev -c {container} -- /bin/sh

## Others
  - 為了養成好的開發習慣，我並沒有公開table的columns的名稱，所以若有需要使用請務必告訴我(If you wanna run the app, send a mail to me)。