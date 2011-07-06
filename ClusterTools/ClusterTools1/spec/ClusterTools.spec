#
# spec file for package ClusterTools
#
# Copyright (c) 2008-2009 SUSE LINUX GmbH, Frankfurt, Germany.
# Copyright (c) 2009 SUSE LINUX GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# GPL
#
#
Name:         ClusterTools
License:      GPL
Group:        System/Cluster
Autoreqprov:  on
Summary:      Cluster Tools to control some functions easy
Version:      1.0.0
Release:      1
Source:       %{name}-%{version}.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Vendor:	      SUSE Linux GmbH
Requires:     heartbeat >= 2.1.4
Obsoletes:    wow
	
%description
ClusterTools provides tools for setting up and managing an heartbeat2
cluster.

- wow helps you to create linux-ha system resources.
The main program to be called is whbcc (wow heartbeat config change).
The wow package countains some agents (which are used to figure out
config values) and xml-templates (which are used to create the xml-
snipsets to be inserted into the cluster).

- ClusterServcie is the main tool for managing a linux-ha cluster.
There are some other commandline tools to make life easier.

%prep
%setup -c -T -a 0

%build

%clean
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p %{buildroot}/etc/ClusterTools/
mkdir -p %{buildroot}/usr/sbin/
mkdir -p %{buildroot}/usr/lib/perl5/site_perl/XML/
mkdir -p %{buildroot}/usr/lib/wow/agents
mkdir -p %{buildroot}/usr/share/doc/packages/wow
mkdir -p %{buildroot}/usr/share/doc/packages/wow/samples
mkdir -p %{buildroot}/usr/share/wow
mkdir -p %{buildroot}/usr/share/wow/xml
mkdir -p %{buildroot}/usr/share/man/man7
mkdir -p %{buildroot}/usr/share/man/man8

#
# binaries
#
cp -a sbin/*    %{buildroot}/usr/sbin
cp -a agents/* %{buildroot}/usr/lib/wow/agents
#
# libs
#
cp -a lib/*    %{buildroot}/usr/lib/wow
cp -a lib/Simple.pm %{buildroot}/usr/lib/perl5/site_perl/XML
#
# xml templates and defaults
#
cp -a etc/ClusterTools/* %{buildroot}/etc/ClusterTools
cp -a xml/*    %{buildroot}/usr/share/wow/xml
#
# doc and samples including license and man pages
#
cp -va doc/*        %{buildroot}/usr/share/doc/packages/wow
cp -va samples/*    %{buildroot}/usr/share/doc/packages/wow/samples
gzip man/*.7
gzip man/*.8
cp -va man/*.7.gz       %{buildroot}/usr/share/man/man7
cp -va man/*.8.gz       %{buildroot}/usr/share/man/man8

#
# set owner/group to root
#
chmod a+x 	%{buildroot}/usr/sbin/*

%post

%files
%defattr(-,root,root)
/usr/sbin/ClusterService*
/usr/sbin/clusterstate
/usr/sbin/cluster_actions
/usr/sbin/check-split-brain
/usr/sbin/find_appconf
/usr/sbin/grep_error_patterns
/usr/sbin/grep_supportconfig
/usr/sbin/linkstate
/usr/sbin/list_failcounts
/usr/sbin/make_hb_backup
/usr/sbin/psauxlog
/usr/sbin/reset_failcounts
/usr/sbin/showscores
/usr/sbin/sleha_cleanup
/usr/sbin/sum_base_config
/usr/sbin/wow
/usr/sbin/woweng
/usr/sbin/whbcc
/usr/sbin/whbsaprecheck
/usr/lib/wow
/usr/lib/perl5/site_perl/XML/Simple.pm
/usr/share/wow
%doc /usr/share/doc/packages/wow
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*
%config /etc/ClusterTools

%changelog -n ClusterTools
* Tue Jul 05 2011 - fabian.herschel@novell.com, lars.pinne@novell.com
  1.0.0 added backported scripts from ClusterTools2
* Mon Feb 15 2010 - fabian.herschel@novell.com
  0.9.6-1 IP agent can now select to use IPaddr2 or IPaddr
* Tue Jan 26 2010 - fabian.herschel@novell.com
  0.9.4-1 new wow man page
  update whbcsaprecheck
  update ClusterTools manpage
* Mon Dec 14 2009 - fabian.herschel@novell.com
  0.9.4-1 new wow agents for ipmi and for changes
  - fixed wow agent for master/slave scs/ers
* Fri Dec 11 2009 - fabian.herschel@novell.com
  0.9.3-1 man pages - the documentation is started
* Thu Dec 10 2009 - fabian.herschel@novell.com
  0.9.2-1 wow is now integrated in the ClusterTools
  - SAP ERS support in test status
  - agent for scs/ers: 01-C-01-masterslave_create_scsers
  - riloe agent now sets can-reset parameter
  - whbsaprecheck 
  - wow sapmples now have extention "wow"
  - description updated
  - the command wow is now the master command for all wow subcommands like whbcc whbsaprecheck
* Thu Oct 29 2009 - fabian.herschel@novell.com
  0.8.1-2 Changed package build to fit build.opensuse.org
* Thu Sep 10 2009 - fabian.herschel@novell.com
  0.8.0-1 new versions if ClusterService and make_hb_backup
  - ClusterService can now be used by users in group haclient
  - make_hb_backup can create local archives (single system archives)
    this may be needed if password free ssh between nodes is turned off (security)
  - make_hb_backup now uses supportconfig (package supportutils) 
    to include even more detailed system analyse data
* Wed Sep 09 2009 - fabian.herschel@novell.com
  0.7.4-1 ClusterService update
  - remove old ClusterService1
  - remove numbers of command in ClusterService
  - introduce new command line language (command names)
  - make commands case insensitive (both command line and interactive mode)
  - remove thelimitation that the script onyy run as root to support users in haclient in the future
* Wed Sep 09 2009 - fabian.herschel@novell.com
  0.7.3-1 fixed command line mode
* Fri Mar 04 2009 - fabian.herschel@novell.com
  0.7.1-2 added make_hb_backup
* Wed Feb 11 2009 - fabian.herschel@novell.com
  0.7.0 enhanced cluster_actions
  cluster_actions now can print new operations even, if a node (heartbeat) is restarted
  cluster_actions now provides an intervall (-i intervall) option
* Wed Jan 21 2009 - fabian.herschel@novell.com
  0.6.1-1 showscores integrated in ClusterService (RSS)
* Thu Jan 08 2009 - fabian.herschel@novell.com
  0.6.0-1 new changes (also for heartbeat 2.1.4)
  - new tools (linkstate and showscores)
* Wed Apr 16 2008 - fabian.herschel@novell.com
  0.5.1-2 fixed path in cluster_actions
* Tue Mar 25 2008 - fabian.herschel@novell.com
  0.5.1-1 CheckService renamed to ClusterService
  0.5.0-1 Renamed the tools withou the file extension
  Special version for new customers use cases
  Block/Unblock of clone resource instances on specific nodes
* Wed Mar 05 2008 - fabian.herschel@novell.com
  0.4.0-1 clustercheck.pl and cluster_actions
  cluster_actions: new script to only show "new" cluster actions in a
     loop - this should help to follow the cluster sctions during cluster tests
  svn revison 14
  clustercheck.pl: missleading failcount message fixed
  0.3.0-1 CheckService.sh improved
  added parameter --simul for no-cluster development tests :-)
  command line mode now can read params like vt01 or maloja03
  simulation mode now includes all actions against the cluster
  the over all status is now shown with colored status
  svn revision 11
* Tue Mar 04 2008 - fabian.herschel@novell.com
  0.2.0-2 restart_cluster.sh added
  Some cosmetical changes
  svn revision 6
  0.2.0-1 perl module Simple.pm included
  CheckService.sh has now a mnemonic menue
  svn revision --
* Fri Feb 15 2008 - fabian.herschel@novell.com
  0.1.2-1 sample implementation for is_managed-feature
  svn revision --
* Thu Feb 14 2008 - fabian.herschel@novell.com
  0.1.1-1 simplified build process for the package
  improved reset_failcount.sh to fit the "INFINITY" case
  svn revision --
* Tue Feb 12 2008 - fabian.herschel@novell.com
  0.1.0-1 initial package version
  svn revision --
