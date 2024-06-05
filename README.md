# pixel-artist-backend

## ENV

  - python version: 3.12.3

## How to run?
  - Step0. Create network:
    - docker network create pixel-artist-dev-net
  
  - Step1. Create fake-gcs-server container.
    - NOTE: DONT replace pixel-artist-backend's docker-compose.yaml !
    - 1-1. Rename gcs_docker-compose.yaml to docker-compose.yaml.
    - 1-2 docker-compose up -d --build

  - Step2. Create pixel-artist-backend.
    - 1-1 docker-compose up -d --build

  - Step3. To interact with the pixel-artist-backend.
    - docker exec -it pixel-artist-backend sh

  - Step4. Run turn on the server command:

    Step1. pip3 install -r requirements.txt

    Step2. flask run --host=0.0.0.0 --port=10000

    Step3. To type localhost:10000 on your browser or any client.
  
## 確認安裝是否成功：
  - 成功會看到:
    - Connection with gcs established.

## 更新與維護
  - 若遇到有一些套件有更新或漏洞的話可以參照:
    - Step0. pip3 install safety
    - Step1. safety check
      - 這個會直接照出所有有漏洞的package.
    - Step2. pip install --upgrade your-package
  - 有安裝新套件:
    - Step1. pip show new-package.
    - Step2. append package's version to requirements.txt .
