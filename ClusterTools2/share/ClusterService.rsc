#
# resource get list
#%r:HIDE:Select resource:crm_resource -l
%r:HIDE:Select resource:/usr/lib/ClusterTools2/list_resources
#%r:HIDE::/usr/bin/printf "rsc_A\nrsc_B\nrsc_C\n"
#
# node get list
%n:HIDE:Select node:crm_node -A -l | awk '/member/ { print $2 }'
#%n:HIDE::/usr/bin/printf "nodeA\nnodeB\n"
#
#
%s:HIDE:Select wow script:(cd /usr/lib/ClusterTools2/scripts; ls -1)
#
#
%ww:HIDE:Select or enter full path to your wow file:ls -1 *.wow
%wc:HIDE:Select or enter full path to your cli file:ls -1 *.cli
#
# set node online
NSA:MAIN:set node online/active:crm node online %{n}
#
# set node standby
NSS:MAIN:set node standby:crm node standby %{n}
#
# FENCE node!!
NFENCE:MAIN:FENCE node!!:crm node fence %{n}
#
:MAIN:::bar
#
# show status of all nodes
CSN:MAIN:show status of all nodes:crm_node -l
#
# show locgical status of rings
CSR:MAIN:show logical status of all rings:corosync-cfgtool -s
#
# show status of all resources
CSS:MAIN:show status of all resources:crm_mon -r -1
#
# show (open) cluster actions, if changes where commited
CSA:MAIN:show (open) cluster actions using ptest:ptest -L -D /tmp/CT.$$; cat /tmp/CT.$$; rm /tmp/CT.$$
CSAG:MAIN:show (open) cluster actions using ptest (graph):crm configure ptest
#
# show failcount of resource on node
CSFN:MAIN:show failcount of resource on node:crm resource failcount %{r} show %{n}
#
# delete failcount of resource on node
CDFN:MAIN:delete failcount of resource on node:crm resource failcount %{r} delete  %{n}
CLF:MAIN:show all failcounts:list_failcounts
CRF:MAIN:reset all failcounts:reset_failcounts
#
:MAIN:::bar
#
# set target-role stopped for resource
RDN:MAIN:set target-role stopped for resource:crm resource stop %{r}
#
# set target-role started for resource
RUP:MAIN:set target-role started for resource:crm resource start %{r}
#
# set unmanaged for resource
RSU:MAIN:set unmanaged for resource:crm resource unmanage %{r}
#
# set managed for resource
RSM:MAIN:set managed for resource:crm resource manage %{r}
#
# migrate resource
RMI:MAIN:migrate resource:crm resource migrate %{r}
#
# migrate resource to specific node
RIMN:MAIN:migrate resource to specific node:crm resource migrate %{r} %{n}
#
# unmigrate resource
RUM:MAIN:unmigrate resource:crm resource unmigrate %{r}
#
# cleanup resource
RCL:MAIN:cleanup resource:crm resource cleanup %{r}
#
# cleanup resource node
RCLN:MAIN:cleanup resource node:crm resource cleanup %{r} %{n}
#
RSS:MAIN:Show scores of all resources:ptest -L -s
#
:MAIN:::bar
HELP:MAIN:Man pages:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/Help.rsc
CRMMON:HIDE::crm_mon -r
CONTROL:HIDE:::exit
EXIT:HIDE:::exit
QUIT:HIDE:::exit
### TODO
# show scores
# reset status/failcounts for all failed resources
# show resource status 
# show detailed cluster failure status (clusterstate)
# show detailed cluster history (cluster_actions)
# show detailed link status (linkstate)
