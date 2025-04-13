#!/bin/bash

vtysh -c 'configure terminal' \
  -c 'interface eth0' -c 'ip ospf cost 10' -c 'exit' \
  -c 'interface eth1' -c 'ip ospf cost 10' -c 'exit' \
  -c 'router ospf' \
  -c 'network 10.0.16.0/24 area 0.0.0.0' \
  -c 'network 10.0.17.0/24 area 0.0.0.0' \
  -c 'exit' -c 'write memory'
