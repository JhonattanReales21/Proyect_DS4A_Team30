sudo git pull
sudo docker rm $(docker ps -qa) -f
sudo docker system prune -af
sudo docker build -t dash . 
sudo docker run -it -d -p 8050:8050  -v "$(PWD)":/app --rm dash /bin/bash -c 'BUCKET_NAME=ds4a-team-30 URI=postgres://postgres:postgres@database-team30.cn9ikgjikjdg.us-east-2.rds.amazonaws.com:5432/postgres python3 index.py'