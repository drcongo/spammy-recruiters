[![Build Status](https://travis-ci.org/resmo/ansible-role-mysql.svg?branch=master)](https://travis-ci.org/resmo/ansible-role-mysql)

Ansible MySQL Server Role
=========================

This roles helps to install MySQL Server across RHEL and Ubuntu variants.Apart from installing the MySQL Server

The role can also be used to add databases to the MySQL server and create users in the database. It also supports configuring the databases for replication--both master and slave can be configured via this role.

This role was forked from <https://github.com/bennojoy/mysql>.

Requirements
------------

This role requires Ansible 1.4 or higher, and platform requirements are listed
in the metadata file.

Role Variables
--------------


* `mysql_port`:
  - Description: Port where MySQL is listen
  - Default: `3306`

* `mysql_bind_address`:
  - Description: Address MySQL is using
  - Default: `'127.0.0.1'`

* `mysql_root_db_pass`:
  - Description: Address MySQL is using. Empty String will be ignored.
  - Default: `''`

* `mysql_data_dir`:
  - Description: Path where MySQL stores the DBs.
  - Default: `/var/lib/mysql`

* `mysql_state`:
  - Description: Whether MySQL service should be running.
  - Default: `started`

* `mysql_enabled`:
  - Description: Whether MySQL service should be started on boot.
  - Default: `'yes'`

* `mysql_configs`:
  - Description: Various MySQL configs.
  - Default:
  ```
  - { name: 'query_cache_limit', value: '16M'}
  - { name: 'query_cache_size', value: '32M'}
  - { name: 'join_buffer_size', value: '32M'}
  - { name: 'thread_cache_size', value: '4'}
  - { name: 'innodb_rollback_on_timeout', value: '1'}
  - { name: 'innodb_buffer_pool_size', value: '128M'}
  - { name: 'innodb_log_file_size', value: '128M'}
  - { name: 'table_cache', value: '256'}
  ```

* `mysql_db`:
  - Description: Databases to be present.
  - Default: `[]`

* `mysql_users`:
  - Description: MySQL users to be present.
  - Default: `[]`

* `mysql_repl_user`:
  - Description: MySQL repl user.
  - Default: `[]`

* `mysql_repl_role`:
  - Description: MySQL repl user.
  - Values: '' | master | slave
  - Default: `''`


Examples
--------

1) Install MySQL Server and set the root password, but don't create any
database or users.

      - hosts: all
        roles:
        - {role: mysql, root_db_pass: s3cur3 }

2) Install MySQL Server and create 2 databases and 2 users.

      - hosts: all
        roles:
         - {role: mysql, mysql_db: [{name: benz},
                                    {name: benz2}],
            mysql_users: [{name: ben3, pass: foobar, priv: "*.*:ALL"},
                          {name: ben2, pass: foo}] }

Note: If users are specified and password/privileges are not specified, then
default values are set.

3) Install MySQL Server and create 2 databases and 2 users and configure the
database as replication master with one database configured for replication.

      - hosts: all
        roles:
         - {role: mysql, mysql_db: [{name: benz, replicate: yes },
                                    { name: benz2, replicate: no}], 
                         mysql_users: [{name: ben3, pass: foobar, priv: "*.*:ALL"},
                                       {name: ben2, pass: foo}],
                         mysql_repl_user: [{name: repl, pass: foobar}] }

4) A fully installed/configured MySQL Server with master and slave
replication.

      - hosts: master
        roles:
         - {role: mysql, mysql_db: [{name: benz}, {name: benz2}],
                         mysql_users: [{name: ben3, pass: foobar, priv: "*.*:ALL"},
                                       {name: ben2, pass: foo}],
                         mysql_configs: [{ name: 'mysql_db_id', value: '8'}] }

      - hosts: slave
        roles:
         - {role: mysql, mysql_db: none, mysql_users: none,
                  mysql_repl_role: slave, mysql_repl_master: vm2,
                  mysql_configs: [{ name: 'mysql_db_id', value: '9'}],
                  mysql_repl_user: [{name: repl, pass: foobar}] }

Note: When configuring the full replication please make sure the master is
configured via this role and the master is available in inventory and facts
have been gathered for master. The replication tasks assume the database is
new and has no data.


Dependencies
------------

None

License
-------

BSD

Author Information
------------------

Benno Joy
René Moser
