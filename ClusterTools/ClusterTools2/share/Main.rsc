#
#
%cs:HIDE:Select or enter full path to your wow file:( cd /usr/share/ClusterTools2/; ls -1 *.rsc)
#
CSERVICE:MAIN:ClusterService Menu:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/ClusterService.rsc
WOW:MAIN:WOW! Menu:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/Wow.rsc
CLXEVA:MAIN:CLX specific Menu:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/CLXEVA.rsc
ANY:MAIN:Select a Menu:/usr/sbin/menueng2 --rscFile /usr/share/ClusterTools2/%{cs}
CONTROL:HIDE:::exit
EXIT:HIDE:::exit
QUIT:HIDE:::exit
UP:HIDE:::exit
