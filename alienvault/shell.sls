# av's bashrc is overwritten in every ossim-setup
# set a different bash prompt color for every av profile
/root/.bashrc:
  file.append:
    - text:
      - EDITOR=vim
      - GREP_OPTIONS='--color=auto'
      - GREP_COLOR='1;32'
    {% if 'alienvault_is_server' in grains and grains['alienvault_is_server'] %}
      - PS1='\[\033[01;31m\]\h \[\033[00m\](server)\[\033[01;34m\] \w \$\[\033[00m\] '
    {% elif 'alienvault_is_framework' in grains and grains['alienvault_is_framework'] %}
      - PS1='\[\033[01;32m\]\h \[\033[00m\](web)\[\033[01;34m\] \w \$\[\033[00m\] '
    {% elif 'alienvault_is_sensor' in grains and grains['alienvault_is_sensor'] %}
      - PS1='\[\033[01;36m\]\h \[\033[00m\](sensor)\[\033[01;34m\] \w \$\[\033[00m\] '
    {% elif 'alienvault_is_database' in grains and grains['alienvault_is_database'] %}
      - PS1='\[\033[01;38m\]\h \[\033[00m\](ddbb)\[\033[01;34m\] \w \$\[\033[00m\] '
    {% endif %}

# vim: filetype=sh number ts=2 sts=2 expandtab
