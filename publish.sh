#!/bin/bash

# Sakura 100yen hosting server with no ssh/rsync support
SERVER=diveintopython3-ja.rdy.jp

./build_ja.py
python3 ./buildtoc.py
python3 ga.py

read -p "User: " USER
read -s -p "Password: " PASSWORD

ftp -v -n -i $SERVER << EOS
user $USER $PASSWORD
lcd output/
cd www/dip3-ja/
mput *.html
bye
EOS

