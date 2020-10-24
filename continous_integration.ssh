sudo git pull
sudo docker rm $(docker ps -qa) -f
sudo docker system prune -af
sudo docker build -t dash . 
sudo docker run -it -p 8050:8050  -v "$(PWD)":/app --rm dash /bin/bash -c 'URI=postgres://postgres:postgres@database-1.c04tyndaqlxm.us-east-2.rds.amazonaws.com:5432/postgres python3 index.py'