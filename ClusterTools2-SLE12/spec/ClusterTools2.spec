#
# spec file for package ClusterTools2
#
# Copyright (c) 2011-2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018-2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           ClusterTools2
Summary:        Cluster Tools to control some functions easy
License:        GPL-2.0
Group:          Productivity/Clustering/HA
Version:        3.1.0
Release:        101
Source:         %{name}-%{version}.tbz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       systemd
Requires:       logrotate
Requires:       pacemaker > 1.1.1
Requires:       perl-TermReadLine-Gnu >= 1.16
Requires(post): man

%description
ClusterTools2 provides tools for setting up and managing a corosync/
pacemaker cluster.
There are some other commandline tools to make life easier.
Starting with version 3.0.0 is support for SUSE Linux Enterprise Server 12.

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
#mkdir -p %{buildroot}/usr/lib/ClusterTools2/check
mkdir -p %{buildroot}/usr/lib/ClusterTools2/scripts
mkdir -p %{buildroot}/usr/share/man/man5
mkdir -p %{buildroot}/usr/share/man/man7
mkdir -p %{buildroot}/usr/share/man/man8
mkdir -p %{buildroot}/usr/lib/ClusterTools2/supportconfig/plugins
mkdir -p %{buildroot}/usr/lib/systemd/system

#
# "binaries"
#
cp -va sbin/* %{buildroot}/usr/sbin/
cp -va system/* %{buildroot}/usr/lib/systemd/system
cp -va plugins/* %{buildroot}/usr/lib/ClusterTools2/supportconfig/plugins/
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
#cp -a cli/* %{buildroot}/usr/share/ClusterTools2/cli/
chmod 0755 samples/*.pl 
cp -a samples/* %{buildroot}/usr/share/ClusterTools2/samples/
#cp -a lib/* %{buildroot}/usr/lib/ClusterTools2/
#cp -a lib/check/* %{buildroot}/usr/lib/ClusterTools2/check
#cp -a agents/* %{buildroot}/usr/lib/ClusterTools2/agents/
#cp -a scripts/* %{buildroot}/usr/lib/ClusterTools2/scripts
#
# man pages and license
#
cp -a man5/*.gz %{buildroot}/usr/share/man/man5/
cp -a man7/*.gz %{buildroot}/usr/share/man/man7/
cp -a man8/*.gz %{buildroot}/usr/share/man/man8/

%post
mkdir -p /usr/lib/systemd/system
mkdir -p /usr/lib/supportconfig/plugins
cp /usr/lib/ClusterTools2/supportconfig/plugins/* /usr/lib/supportconfig/plugins
for f in /usr/lib/man/man/man8/cs_* /usr/lib/man/man8/{ClusterService,psauxlog,meminfolog,lsoflog,wow} /usr/lib/man/man7/ha_related_*; do mandb -q $f; done

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
