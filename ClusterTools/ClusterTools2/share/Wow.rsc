#
# resource get list
%r:HIDE:Select resource:crm_resource -l
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
WOWED:MAIN:Edit Wow File:vi %{ww}
WOWCALL:MAIN:call wow with scriptname:bash /usr/lib/ClusterTools2/scripts/%{s} %{ww}
WOWCAT:MAIN:show created cli file:cat %{wc}
WOWBURN:MAIN:apply created cli file:crm -f %{wc}
CONTROL:HIDE:::exit
EXIT:HIDE:::exit
QUIT:HIDE:::exit
