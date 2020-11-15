sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
cd /usr/src
sudo wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
sudo tar xzf Python-3.7.9.tgz
cd Python-3.7.9
sudo ./configure --enable-optimizations
sudo make altinstall
sudo rm /usr/src/Python-3.7.9.tgz