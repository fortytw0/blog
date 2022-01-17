---
title: Default Docker Deploy Environment
date: 01-16-2022
tags: [docker, CD, django]
slug: default-docker-deploy
meta: A Docker setup that will help you deploy your Django projects more easily.
---

# Default Docker Deploy Environment

### If you read my last blog post, I decided that I will focus on designing a deployment environment, so that I can publish my changes as and when they happen. This is it, folks! 

This blog is really just a place holder for my Github repository that holds the environment. 

[### Use this link to clone the repository.](https://github.com/fortytw0/default-django-deploy/tree/example)

The example is really straightforward, you can just use the `docker-compose up --build` command to run the setup. 

This branch exists to provide you a glimpse into how you can setup your services and have a reverse-proxy serve them to the web. Some things that you can note : 

1. Start with your service. In the docker folder for each uniquely named service, configure the `docker/nginx.conf`.
-  You should change the server name to whatever you provide in the `docker-compose.yml`. 
- The `location` parameter is whatever sub-url that will be passed from the reverse-proxy. 
- This sub-url system needs to lineup with Django's URL system, and allowed hosts as well. So in your Django project, ensure that your urls are prefixed appropriately (in this example, they are prefixed with 'service1') and 
- Ensure that you edit the `ALLOWED_HOSTS` parameter in `docker/RUN_SECRETS.env` .

2. Move to the server. Open `docker/nginx.conf`
- You should ideally provide a `server_name`, which is typically your domain name. 
- Add proxies to your services. The `location` parameter should align with the service sub-urls you have provided. 

3. Move to the `docker-compose.yml`. 
- Add your service entrypoint file, your environment files, and remember to connect it to the bridge network. 
- Link the 80 and 443 ports to the server's operating port. In this example, that would be port 3000. 


### And that's it! You are done! Feels good to have such easy deployment right? 

If you have any problems running this - you can email me at dananjay (dot) srinivas (at) colorado d(dot) edu




