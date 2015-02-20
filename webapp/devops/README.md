# Ansible stuff

Everything in here is kinda ready to drop into your project as a devops folder. Wherever possible, all config for the various Ansible roles is done in the group_vars.

## Group Vars

In the directory ```group_vars``` you'll find configs for different servers. The ```all``` file will be used by every server.


## Provisioning a remote server

Before you can provision a remote server, you'll need to generate a deploy password to put into the ```staging``` and ```remote``` group_vars. To do this...

    sudo pip install passlib

    python

    > from passlib.hash import sha256_crypt
    > hash = sha256_crypt.encrypt("YOUR DEPLOY PASSWORD GOES HERE")
    > hash

This will generate a massive long hashed string of whatever deploy password you give it.

You will also need to generate the deploy keys. CD to the keys directory and run ```ssh-keygen``` making sure to call your key ```deploy_key```. 



### TO DO

* RabbitMQ needs the auth stuff fixing.

