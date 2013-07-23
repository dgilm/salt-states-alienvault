
## definitions for specific hosts (/etc/hosts)
#server1:
#  host.present:
#    - ip: 192.168.1.25
#    - names:
#      - server1
#      - alias1

/etc/motd:
  file.append:
    - text:
      - Deployment made by A3Sec - http://www.a3sec.com

# vim: filetype=yaml number ts=2 sts=2 expandtab
