base:

  '*':
    - core.tools
    - core.hosts
    - core.dns
    - core.users
    - core.repos
    - alienvault.shell

  {% if 'alienvault_is_server' in grains and grains['alienvault_is_server'] %}
    - alienvault.server
    - alienvault.logger
  {% endif %}

  {% if 'alienvault_is_framework' in grains and grains['alienvault_is_framework'] %}
    - alienvault.framework
  {% endif %}

  {% if 'alienvault_is_sensor' in grains and grains['alienvault_is_sensor'] %}
    - alienvault.sensor
  {% endif %}

  {% if 'alienvault_is_database' in grains and grains['alienvault_is_database'] %}
    - alienvault.database
  {% endif %}


#    # Filter by Alienvault Version
#    {% if grains['lsb_codename'] == 'squeeze' %}
#      # Alienvault 3.x
#    {% elif grains['lsb_codename'] == 'lenny' %}
#      # Alienvault 4.x
#    {% endif %}


#  # Filter by minion id
#  '(avsiem|avserver|ossim-server)':
#    - match: pcre
#    - alienvault.server

# vim: filetype=yaml number ts=2 sts=2 expandtab
