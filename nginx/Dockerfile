FROM nginx:1.13.8
RUN mkdir -p /etc/nginx/sites-available/\
    && mkdir -p /etc/nginx/sites-enabled/

COPY nginx.conf /etc/nginx/
COPY bis_nginx.conf /etc/nginx/sites-available/

RUN ln -s /etc/nginx/sites-available/bis_nginx.conf /etc/nginx/sites-enabled/

# RUN rm /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]