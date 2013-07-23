/etc/apt/sources.list:
  file.append:
    - text:
      - deb http://backports.debian.org/debian-backports squeeze-backports main contrib non-free
      - deb http://debian.saltstack.com/debian squeeze-saltstack main

#repos:
#  pkgrepo.managed:
#    - name: squeeze-backports
#    - humanname: Debian Squeeze Backports
#    - uri: http://backports.debian.org/debian-backports
#    - comps: main
#    - dist: squeeze-backports
#    - comments:
#      - # Squeeze Backports

# vim: filetype=yaml number ts=2 sts=2 expandtab
