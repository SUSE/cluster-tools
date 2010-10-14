#
### init 
#
:HIDE:width_cmd:12:val
#
### select helper
#
%r:HIDE:Select resource:crm_resource -l
%sid:HIDE:Select SAP system:crm_resource -L | awk -F_ '/grp_sap_/ { print $3 }'
%n:HIDE:Select node:crm_node -A -l | awk '/member/ { print $2 }'
%s:HIDE:Select wow script:(cd /usr/lib/ClusterTools2/scripts; ls -1)
%ww:HIDE:Select or enter full path to your wow file:ls -1 *.wow
%wc:HIDE:Select or enter full path to your cli file:ls -1 *.cli
#
### MAIN menu
#
:MAIN:Control NA0::bar
:MAIN:::descr
:MAIN:Control the SAP system NA0::descr
:MAIN:  - you can start, stop the complete SAP sytem::descr
:MAIN:  - you can start, stop the complete SAP resource group including FS and IP::descr
:MAIN:::decr
:MAIN:::descr
SAPDB-NA0-DN:MAIN:stop  SAP NA0 system (incl DB):crm resource stop rsc_sapdb_NA0
SAPDB-NA0-UP:MAIN:start SAP NA0 system (incl DB):crm resource start rsc_sapdb_NA0
SAPGR-NA0-DN:MAIN:stop  SAP NA0 system (incl. FS and IP):crm resource stop grp_sap_NA0
SAPGR-NA0-UP:MAIN:start SAP NA0 system (incl. FS and IP):crm resource start grp_sap_NA0
SAPGR-NA0-MI:MAIN:migrate SAP NA0 system:crm resource migrate grp_sap_NA0
SAPGR-NA0-UM:MAIN:unmigrate SAP NA0 system:crm resource unmigrate grp_sap_NA0
:MAIN:::descr
:MAIN:Cluster nodes and resources::bar
:MAIN:::descr
NSA:MAIN:set node online/active (params NODE):crm node online %{n}
NSS:MAIN:set node standby (params NODE):crm node standby %{n}
#
:MAIN:::descr
#
CSS:MAIN:show status of all resources:crm_mon -r -1
CLF:MAIN:show all failcounts:list_failcounts
CRF:MAIN:reset all failcounts:reset_failcounts
:MAIN:::descr
#
:MAIN:Experts::bar
:MAIN:::descr
SAPMENU:MAIN:open SAP menu:SAP:menu
CSERVICE:MAIN:menu for experts:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/ClusterTools.rsc:
:MAIN:::descr
:MAIN:Current cluster status::bar
:MAIN:Cluster status (fake):echo "IDLE":status
:MAIN:Cluster health (fake):echo "GREEN":status
:MAIN:Cluster ring   (fake):echo "LINKS UP":status
#
### SAP MENU
#
:SAP:Control SAP systems::bar
:SAP:Control any SAP system in the cluster::descr
:SAP:  - your resource group must be named grp_sap_SID, where SID is the::descr
:SAP:    SAP system ID (i.e. NA0)::descr
:SAP:::descr
SAPDB-DN:SAP:stop  SAP system (incl. DB - params SID):crm resource stop rsc_sapdb_%{sid}
SAPDB-UP:SAP:start SAP system (incl. DB - params SID):crm resource start rsc_sapdb_%{sid}
SAPGR-DN:SAP:stop  SAP system (incl. FS and IP - params SID):crm resource stop grp_sap_%{sid}
SAPGR-UP:SAP:start SAP system (incl. FS and IP - params SID):crm resource start grp_sap_%{sid}
SAPGR-MI:SAP:migrate SAP system (params SID):crm resource migrate grp_sap_%{sid}
SAPGR-UM:SAP:unmigrate SAP system (params SID):crm resource unmigrate grp_sap_%{sid}
MAIN:SAP:Main menu:MAIN:menu
#
## commands
#
EXIT:HIDE:::exit
QUIT:HIDE:::exit
### TODO
# show scores
# reset status/failcounts for all failed resources
# show resource status 
# show detailed cluster failure status (clusterstate)
# show detailed cluster history (cluster_actions)
# show detailed link status (linkstate)
