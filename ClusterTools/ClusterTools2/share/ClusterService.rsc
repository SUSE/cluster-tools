#
# resource get list
%r:HIDE:Select resource:crm_resource -l
#%r:HIDE::/usr/bin/printf "rsc_A\nrsc_B\nrsc_C\n"
#
# node get list
%n:HIDE:Select node:crm_node -A -l | awk '/member/ { print $2 }'
#%n:HIDE::/usr/bin/printf "nodeA\nnodeB\n"
#
# set node online
NSO:MAIN:set node online:crm node online %n
#
# set node standby
NSS:MAIN:set node standby:crm node standby %n
#
# show status all nodes
CSAN:MAIN:show status all nodes:crm node show
#
# show status specific node
NSSTAT:MAIN:show status specific node:crm node show %n
#
# set target-role stopped for resource
RDN:MAIN:set target-role stopped for resource:crm resource stop %r
#
# set target-role started for resource
RUP:MAIN:set target-role started for resource:crm resource start %r
#
# show status of all resources
CSS:MAIN:show status of all resources:crm_mon -r -1
#
# set unmanaged for resource
RSU:MAIN:set unmanaged for resource:crm resource unmanaged %r
#
# set managed for resource
RSM:MAIN:set managed for resource:crm resource managed %r
#
# migrate resource
RMI:MAIN:migrate resource:crm resource migrate %r
#
# migrate resource to specific node
RUMH:MAIN:migrate resource to specific node:crm resource migrate %r %n
#
# unmigrate resource
RUM:MAIN:unmigrate resource:crm unmigrate %r
#
# show (open) cluster actions, if changes where commited
CSA:MAIN:show (open) cluster actions using ptest
#
# cleanup resource
RCL:MAIN:cleanup resource:crm resource cleanup %r
#
# cleanup resource node
RCLN:MAIN:cleanup resource node:crm resource cleanup %r %n
#
# show failcount of resource on node
CSFN:MAIN:show failcount of resource on node:crm resource failcount %r show %n
#
# delete failcount of resource on node
CDFN:MAIN:delete failcount of resource on node:crm resource failcount %r delete  %n
#
# FENCE node!!
NFENCE:MAIN:FENCE node!!:crm node fence %n
#
MP:MAIN:multipath status:multipath -ll
LS:MAIN:show mapper devices:ls /dev/mapper/*
LOG:MAIN:show CLX log entries:grep CLX /var/log/messages
LF:MAIN:show failcounts:list_failcounts
RF:MAIN:reset failcounts:reset_failcounts
CRMMON:HIDE::crm_mon -r
### TODO
# show scores
# reset status/failcounts for all failed resources
# show resource status 
# show detailed cluster failure status (clusterstate)
# show detailed cluster history (cluster_actions)
# show detailed link status (linkstate)
