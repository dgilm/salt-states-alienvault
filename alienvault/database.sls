mysql-server:
  pkg:
    - installed
    - names:
      - percona-server-client
      - percona-server-server
      - python-mysqldb
      - mytop

/etc/mysql/my.cnf:
  file:
    - sed
    - before: '127.0.0.1'
    - after: '0.0.0.0'
    - limit: '^bind-address'
    - require:
      - pkg: percona-server-server

mysql:
  service:
    - running
    - require:
      - pkg: percona-server-server
    - watch:
      - file: /etc/mysql/my.cnf

# vim: filetype=yaml number ts=2 sts=2 expandtab
