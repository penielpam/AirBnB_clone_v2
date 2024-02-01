#!/usr/bin/env bash
<<<<<<< HEAD
# Configures a web server for deploying web_static.

# Update and install Nginx
apt-get update
apt-get install -y nginx

# Create necessary directories and index file
=======
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

>>>>>>> 73551a09623cbc28dea49449990f143215404231
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

<<<<<<< HEAD
# Set ownership and group for directories
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Configure Nginx server block
=======
chown -R ubuntu /data/
chgrp -R ubuntu /data/

>>>>>>> 73551a09623cbc28dea49449990f143215404231
printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

<<<<<<< HEAD
# Restart Nginx service
=======
>>>>>>> 73551a09623cbc28dea49449990f143215404231
service nginx restart
