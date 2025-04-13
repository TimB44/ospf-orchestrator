vtysh -c 'configure terminal' \
  -c 'interface eth0' -c 'ip ospf cost 10' -c 'exit' \
  -c 'interface eth1' -c 'ip ospf cost 10' -c 'exit' \
  -c 'exit' -c 'write memory'
