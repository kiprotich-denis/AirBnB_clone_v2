#!/usr/bin/env bash
# web server for deployment
if [ ! -x /usr/sbin/nginx ]
then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tBest School\n\t</body>\n</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu "/data/"

new_str="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "35i $new_str" /etc/nginx/sites-enabled/default

sudo service nginx restart
