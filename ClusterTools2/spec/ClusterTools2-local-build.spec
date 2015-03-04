#
# spec file for package ClusterTools2
#
# Copyright (c) 2008-2010 SUSE LINUX GmbH, Germany.
# Copyright (c) 2011-2014 SUSE LINUX Products GmbH, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# GNU General Public License
#
# please send bugfixes or comments to feedback@suse.de.
#
Name:         ClusterTools2
License:      GPL
Group:        Productivity/Clustering/HA
Autoreqprov:  on
Summary:      Cluster Tools to control some functions easy
Version:      2.5.2
#Release:      0.5.2
Release:      9 
Source:       %{name}-%{version}.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Vendor:	      SUSE Linux Products GmbH
Requires:     pacemaker > 1.1.1
Requires:     perl-TermReadLine-Gnu >= 1.16
	
%description
ClusterTools2 provides tools for setting up and managing a corosync/
pacemaker cluster.

- wow helps you to create Linux-ha system resources.
The wow package countains some agents (which are used to figure out
config values) and templates (which are used to create the crm-
snipsets to be inserted into the cluster).

- ClusterService is the main tool for managing a Linux-ha cluster.
There are some other commandline tools to make life easier.

%prep
%setup -c -T -a 0

%build
( cd man5; for mp in *5; do gzip $mp; done )
( cd man7; for mp in *7; do gzip $mp; done )
( cd man8; for mp in *8; do gzip $mp; done )
mkdir -p etc/ClusterTools2

%clean
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p %{buildroot}/etc/ClusterTools2
mkdir -p %{buildroot}/etc/cron.d
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/share/ClusterTools2
mkdir -p %{buildroot}/usr/share/ClusterTools2/cli
mkdir -p %{buildroot}/usr/share/ClusterTools2/samples
mkdir -p %{buildroot}/usr/lib/ClusterTools2
mkdir -p %{buildroot}/usr/lib/ClusterTools2/agents
mkdir -p %{buildroot}/usr/lib/ClusterTools2/scripts
mkdir -p %{buildroot}/usr/share/man/man5
mkdir -p %{buildroot}/usr/share/man/man7
mkdir -p %{buildroot}/usr/share/man/man8
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins

#
# "binaries"
#
cp -va sbin/* %{buildroot}/usr/sbin/
cp -va plugins/* %{buildroot}/usr/lib/supportconfig/plugins
#
# etc
#
cp -va etc/ClusterTools2/* %{buildroot}/etc/ClusterTools2/
cp -va etc/cron.d/* %{buildroot}/etc/cron.d/
cp -va etc/logrotate.d/* %{buildroot}/etc/logrotate.d/
#
# share 
#
cp -a share/* %{buildroot}/usr/share/ClusterTools2/
cp -a cli/* %{buildroot}/usr/share/ClusterTools2/cli/
cp -a samples/* %{buildroot}/usr/share/ClusterTools2/samples/
cp -a lib/* %{buildroot}/usr/lib/ClusterTools2/
cp -a agents/* %{buildroot}/usr/lib/ClusterTools2/agents/
cp -a scripts/* %{buildroot}/usr/lib/ClusterTools2/scripts
#
# man pages and license
#
cp -a man5/*.gz %{buildroot}/usr/share/man/man5/
cp -a man7/*.gz %{buildroot}/usr/share/man/man7/
cp -a man8/*.gz %{buildroot}/usr/share/man/man8/

%post

%files
%defattr(-,root,root)
/usr/sbin/ClusterService
/usr/sbin/add_softdog_to_initrd
/usr/sbin/add_watchdog_to_initrd
/usr/sbin/clusterstate
#/usr/sbin/cluster_actions
/usr/sbin/disable_other_watchdog
/usr/sbin/find_appconf
/usr/sbin/fhcrmedit
/usr/sbin/grep_cluster_patterns
/usr/sbin/grep_cluster_transition
/usr/sbin/grep_error_patterns
/usr/sbin/grep_supportconfig
#/usr/sbin/linkstate
/usr/sbin/list_failcounts
/usr/sbin/lsoflog
#/usr/sbin/make_hb_backup
/usr/sbin/make_corosync_conf
/usr/sbin/make_iscsi_conf
/usr/sbin/make_sbd_devices
/usr/sbin/menueng2
/usr/sbin/reset_failcounts
/usr/sbin/whbsaprecheck
/usr/sbin/wow*
/usr/sbin/prepare_wowfile
/usr/sbin/prepare_crm_basics
/usr/sbin/precheck_for_sap
#/usr/sbin/precheck_for_oracle
/usr/sbin/psauxlog
/usr/sbin/sleha_cleanup
/usr/sbin/show_scores
/usr/sbin/showscores
/usr/sbin/sum_base_config
/usr/sbin/xmstat
#/usr/sbin/test_udpmcast
/usr/share/ClusterTools2
/usr/lib/ClusterTools2
/usr/lib/supportconfig/plugins
%doc /usr/share/man/man5/*.gz
%doc /usr/share/man/man7/*.gz
%doc /usr/share/man/man8/*.gz
%config(noreplace) /etc/ClusterTools2
%config(noreplace) /etc/cron.d
%config(noreplace) /etc/logrotate.d

%changelog -n ClusterTools2
* Fri Feb 10 2012 - lars.pinne@novell.com
  - eDir back again
* Tue Nov 15 2011 - lars.pinne@novell.com
  - more grep patterns, minor fixes
* Fri Oct 21 2011 - lars.pinne@novell.com
  - added lsoflog, merged separate crontab and logrotate to one ClusterTools2, fixed grep_supportconfig
* Thu Oct 05 2011 - lars.pinne@novell.com
  - added grep_cluster_transition
* Thu Sep 29 2011 - lars.pinne@novell.com
  - moved add_softdog_to_initrd to add_watchdog_to_initrd, added grep_cluster_patterns, various fixes and updates
* Thu Sep 22 2011 - lars.pinne@novell.com
  - added xmstat, various fixes and updates
* Tue Aug 30 2011 - lars.pinne@novell.com
  - added wow on-fail-block, added supportconfig plugins
* Fri Aug 26 2011 - fabian.herschel@suse.com
  2.2.9 package version
* Tue Jul 18 2011 - lars.pinne@novell.com
  - added man page, fixed config scripts, 2nd ring in make_corosync_conf, set config (noreplace)
* Wed Jul 06 2011 - fabian.herschel@suse.com
  2.2.8 fixed node status (CSN)
* Tue Jul 05 2011 - fabian.herschel@suse.com
  2.2.7 fixed command line option
  - fixed missing groups in resource list
* Tue Jul 05 2011 - fabian.herschel@suse.com
  2.2.6 new package version for opensuse.org
  - You could (only recommended for test scenarious) switchoff STONITH by setting STONITH_ENABLED=false in your WOW file
  - corrected error in samples (uninitialized SAPsid)
* Tue Jun 14 2011 - fabian.herschel@suse.com
  2.2.5-1 added corrections/improvements from lars.pinne@novell.com
  - changed menueng2, wow and ClusterService to display better help (program name now matches the use case)
* Sat May 14 2011 - fabian.herschel@suse.com
  2.2.4-1 added fhcrmedit to have a batch-able editor - fhcrmedit will be renamed in the future and is only a draft for internal tests
* Fri May 13 2011 - fabian.herschel@suse.com
  2.2.3-1 simple stack now has now the option to skip the SFEX device resource (just let SFEX_DEVICE be empty)
* Tue May 10 2011 - lars.pinne@novell.com
  2.2.2-1 added sum and error patterns, fixed minor bugs, added some man pages, updated ClusterService
* Tue Apr 29 2011 - fabian.herschel@novell.com
  2.2.1-1 fixed package spec to get it build (added precheck_for_sap)
* Tue Apr 29 2011 - lars.pinne@novell.com
  2.2.0-1 added psauxlog
* Tue Apr 12 2011 - fabian.herschel@novell.com
  2.2.0-1 now supports command mode (--cmd CMD options)
* Thu Apr 12 2011 - lars.pinne@novell.com
  2.1.10-1 update and cleanup 
  - sum_base_config
* Mon Mar 07 2011 - lars.pinne@novell.com
  2.1.9-1 update and cleanup 
  - grep_error_patterns
* Mon Mar 07 2011 - fabian.herschel@novell.com
  2.1.8-1 prepare_wowfile (lp)
  - RAID1 devices resources could be named more flexible (fh)
* Tue Feb 22 2011 - lars.pinne@novell.com
  2.1.7-1 Updated files
  - Manpages: sbd.8, sleha_cleanup.8
  - grep-error-patterns
  - sleha_cleanup
  - whbsaprecheck
* Tue Feb 01 2011 - fabian.herschel@novell.com
  2.1.6-1 added sleha_cleanup and grep-error-patterns from Lars Pinne
* Mon Nov 15 2010 - fabian.herschel@novell.com
  2.1.5-1 added new man pages from Lars
* Mon Oct 25 2010 - fabian.herschel@novell.com
  2.1.4-1 added new use case for fs only stack
* Thu Oct 14 2010 - fabian.herschel@novell.com
  2.1.3-1 menueng2 now supports multiple menues and additional control commands
  - use case specific sample CS_SAPNA0
* Tue Oct 12 2010 - fabian.herschel@novell.com
  2.1.2-1 name scheme for wow and submenus
* Thu Oct 07 2010 - fabian.herschel@novell.com
  2.1.0-1 reintegrated wow to ClusterTools2
* Wed Oct 06 2010 - fabian.herschel@novell.com
  2.0.0-1 initial package
