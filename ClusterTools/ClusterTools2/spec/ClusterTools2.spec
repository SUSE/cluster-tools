#
# spec file for package ClusterTools
#
# Copyright (c) 2008 SUSE LINUX GmbH, Frankfurt, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# GPL
#
# please send bugfixes or comments to feedback@suse.de.
#
Name:         ClusterTools2
License:      GPL
Group:        System/terminalserver
Autoreqprov:  on
Summary:      Cluster Tools to control some functions easy
Version:      2.1.1
Release:      3 
Source:       %{name}-%{version}.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Vendor:	      SUSE Linux GmbH
Requires:     pacemaker > 1.1.1
Requires:     perl-TermReadLine-Gnu >= 1.16
	
%description
ClusterTools provides tools for setting up and managing an openais/
pacemaker cluster.

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
( cd man7; for mp in *7; do gzip $mp; done )
( cd man8; for mp in *8; do gzip $mp; done )

%clean
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/share/ClusterTools2
mkdir -p %{buildroot}/usr/share/ClusterTools2/cli
mkdir -p %{buildroot}/usr/share/ClusterTools2/samples
mkdir -p %{buildroot}/usr/lib/ClusterTools2
mkdir -p %{buildroot}/usr/lib/ClusterTools2/agents
mkdir -p %{buildroot}/usr/lib/ClusterTools2/scripts
mkdir -p %{buildroot}/usr/share/man/man7
mkdir -p %{buildroot}/usr/share/man/man8

#
# "binaries"
#
cp -va sbin/* %{buildroot}/usr/sbin
#
# share 
#
cp -a share/* %{buildroot}/usr/share/ClusterTools2
cp -a cli/* %{buildroot}/usr/share/ClusterTools2/cli
cp -a samples/* %{buildroot}/usr/share/ClusterTools2/samples
#
#
cp -a lib/* %{buildroot}/usr/lib/ClusterTools2
cp -a agents/* %{buildroot}/usr/lib/ClusterTools2/agents
cp -a scripts/* %{buildroot}/usr/lib/ClusterTools2/scripts
# man page(s) and license
#
cp -a man7/*.gz %{buildroot}/usr/share/man/man7
cp -a man8/*.gz %{buildroot}/usr/share/man/man8

%post

%files
%defattr(-,root,root)
/usr/sbin/ClusterService
#/usr/sbin/clusterstate
#/usr/sbin/cluster_actions
#/usr/sbin/linkstate
/usr/sbin/list_failcounts
#/usr/sbin/make_hb_backup
/usr/sbin/reset_failcounts
/usr/sbin/whbsaprecheck
/usr/sbin/wow*
/usr/sbin/menueng2
#/usr/sbin/showscores
/usr/share/ClusterTools2
/usr/lib/ClusterTools2
%doc /usr/share/man/man7/*.gz
%doc /usr/share/man/man8/*.gz

%changelog -n ClusterTools
* Thu Oct 07 2010 - fabian.herschel@novell.com
  2.1.0-1 reintegrated wow to ClusterTools2
* Wed Oct 06 2010 - fabian.herschel@novell.com
  2.0.0-1 initial package
