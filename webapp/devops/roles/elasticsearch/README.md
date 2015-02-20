Ansible ElasticSearch playbook
=====

This role installs and configures ElasticSearch on a server.

Requirements
------------

This role requires Ansible 1.4 or higher and platform requirements are listed
in the metadata file.

Role Variables
--------------

The variables that can be passed to this role and a brief description about
them are as follows.

```
# Elasticsearch version from debian repository
# elasticsearch.yml
es_version: 1.3
# Address of elasticsearch used by fluentd
es_fqdn: localhost
es_port: 9200
# Curator tool
install_curator: True
curator_max_keep_days: 90
# Head plugin
install_head: True
# ElasticHQ plugin
install_eshq: False
# Marvel plugin
install_marvel: True
```

Examples
========

```
# Roles
- name: log server
  hosts: logs
  user: root
  roles:
    - elasticsearch
  vars_files:
    - "host_vars/elasticsearch.yml"

```

Dependencies
------------

None

License
-------

GPL

Author Information
------------------

Pierre Mavro / deimosfr


