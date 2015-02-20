# Security

You only want to run this one against a remote server.

To generate a deploy password to put into the ```staging``` and ```remote``` group_vars. To do this...

    sudo pip install passlib

    python

    > from passlib.hash import sha256_crypt
    > hash = sha256_crypt.encrypt("YOUR DEPLOY PASSWORD GOES HERE")
    > hash

This will generate a massive long hashed string of whatever deploy password you give it.
