#
# spec file for package ClusterTools2
#
# Copyright (c) 2008-2010 SUSE LINUX GmbH, Germany.
# Copyright (c) 2011-2014 SUSE LINUX Products GmbH, Germany.
# Copyright (c) 2015-2018 SUSE LINUX GmbH, Germany.
# Copyright (c) 2019-2020 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# GNU General Public License. No Warranty.
#
# please send bugfixes or comments to feedback@suse.de.
#
Name:         ClusterTools2
License:      GPL
Group:        Productivity/Clustering/HA
Autoreqprov:  on
Summary:      Cluster Tools to control some functions easy
Version:      3.0.1
Release:      109
Source:       %{name}-%{version}.tgz
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Vendor:	      SUSE Linux GmbH
Requires:     pacemaker > 1.1.1
Requires:     perl-TermReadLine-Gnu >= 1.16
Requires:     logrotate

%description
ClusterTools2 provides tools for setting up and managing a corosync/
pacemaker cluster.
There are some other commandline tools to make life easier.
The version 2 is for SLES11, version 3 for SLES12.

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
#mkdir -p %{buildroot}/etc/cron.d
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/share/ClusterTools2
#mkdir -p %{buildroot}/usr/share/ClusterTools2/cli
mkdir -p %{buildroot}/usr/share/ClusterTools2/samples
mkdir -p %{buildroot}/usr/lib/ClusterTools2
#mkdir -p %{buildroot}/usr/lib/ClusterTools2/agents
#mkdir -p %{buildroot}/usr/lib/ClusterTools2/scripts
mkdir -p %{buildroot}/usr/share/man/man5
mkdir -p %{buildroot}/usr/share/man/man7
mkdir -p %{buildroot}/usr/share/man/man8
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins
mkdir -p %{buildroot}/usr/lib/systemd/system

#
# "binaries"
#
cp -va sbin/* %{buildroot}/usr/sbin/
cp -va system/* %{buildroot}/usr/lib/systemd/system/
cp -va plugins/* %{buildroot}/usr/lib/supportconfig/plugins/
#
# etc
#
cp -va etc/ClusterTools2/* %{buildroot}/etc/ClusterTools2/
#cp -va etc/cron.d/* %{buildroot}/etc/cron.d/
cp -va etc/logrotate.d/* %{buildroot}/etc/logrotate.d/
#
# share 
#
cp -a share/* %{buildroot}/usr/share/ClusterTools2/
cp -a cli/* %{buildroot}/usr/share/ClusterTools2/cli/
cp -a samples/* %{buildroot}/usr/share/ClusterTools2/samples/
#cp -a lib/* %{buildroot}/usr/lib/ClusterTools2/
#cp -a agents/* %{buildroot}/usr/lib/ClusterTools2/agents/
#cp -a scripts/* %{buildroot}/usr/lib/ClusterTools2/scripts
#
# man pages and license
#
cp -a man5/*.gz %{buildroot}/usr/share/man/man5/
cp -a man7/*.gz %{buildroot}/usr/share/man/man7/
cp -a man8/*.gz %{buildroot}/usr/share/man/man8/

%post

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/share/ClusterTools2
/usr/lib/ClusterTools2
/usr/lib/systemd/system
%config(noreplace) /etc/ClusterTools2
#%config(noreplace) /etc/cron.d/*
%config(noreplace) /etc/logrotate.d/*
%doc /usr/share/man/man5/*.gz
%doc /usr/share/man/man7/*.gz
%doc /usr/share/man/man8/*.gz

%changelog
