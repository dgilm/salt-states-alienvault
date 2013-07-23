packages:
  pkg:
    - installed
    - names:
      - ossim-framework
      - ossim-framework-daemon

apache2:
  pkg:
    - installed
  service:
    - running


# vim: filetype=yaml number ts=2 sts=2 expandtab
