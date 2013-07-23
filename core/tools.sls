core-tools:
  pkg:
    - installed
    - names:
      - vim
      - locate
      - iptraf
      - htop
      - anacron

/etc/vim/vimrc.local:
  file:
    - managed
    - source: salt://core/vimrc
    - require:
      - pkg: vim

# vim: filetype=yaml number ts=2 sts=2 expandtab
