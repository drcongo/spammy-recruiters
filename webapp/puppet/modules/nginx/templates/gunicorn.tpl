upstream app_server {
    # server unix:/tmp/gunicorn.sock fail_timeout=0;
    # For a TCP configuration:
    server 127.0.0.1:8000 fail_timeout=0;
}

server {
    listen 80 default;
    server_name _;

    keepalive_timeout 5;

    # path for static files
    root /srv/www/app/static;

    location / {
        # Serve static files first, otherwise proxy to gunicorn
        try_files $uri @proxy_to_app;
    }

    location @proxy_to_app {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_redirect off;

        proxy_pass   http://app_server;
    }
}
