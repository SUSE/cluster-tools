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
%wcs:HIDE:Select or enter cli file(s) (one or multiple):ls -1 *.cli
#
WEDIT:MAIN:Edit Wow File:vi %{ww}
WCALL:MAIN:Call wow script:bash /usr/lib/ClusterTools2/scripts/%{s} %{ww}
WSHOW:MAIN:Show created cli file:cat %{wcs}
WBURN:MAIN:Apply created cli file:/usr/lib/ClusterTools2/wow_crm_call %{wcs}
WCOMM:MAIN:Commit wow shadow cib:crm cib commit wow
WDELS:MAIN:Delete wow shadow cib:crm cib delete wow
CONTROL:HIDE:::exit
EXIT:HIDE:::exit
QUIT:HIDE:::exit
