iptables:
  pkg:
    - installed

# iptables rules for allowing incoming connections to the master
/etc/ossim/firewall_include:
  file.append:
    - text:
      - -A INPUT -m state --state new -m tcp -p tcp --dport 80 -j ACCEPT


# vim: filetype=yaml number ts=2 sts=2 expandtab
