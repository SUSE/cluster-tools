#
# spec file for package ClusterTools2
#
# Copyright (c) 2011-2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019-2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           ClusterTools2
Summary:        Tools for cluster management
License:        GPL-2.0-or-later
Group:          Productivity/Clustering/HA
Version:        3.1.3
Release:        0
Source:         %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       systemd
Requires:       logrotate
Requires:       pacemaker > 1.1.1
%if 0%{?suse_version} < 1600
Requires:       perl-TermReadLine-Gnu >= 1.16
%endif
Obsoletes:      ClusterTools2-doc < %{version}
Provides:       ClusterTools2-doc = %{version}
Url:            http://www.suse.com


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
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/usr/lib/ClusterTools2
mkdir -p %{buildroot}/usr/lib/ClusterTools2/scripts
mkdir -p %{buildroot}/usr/lib/ClusterTools2/supportconfig/plugins
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/share/ClusterTools2
mkdir -p %{buildroot}/usr/share/ClusterTools2/samples
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
cp -va etc/logrotate.d/* %{buildroot}/etc/logrotate.d/
#
# share
#
cp -a share/* %{buildroot}/usr/share/ClusterTools2/
chmod 0755 samples/*.pl
cp -a samples/* %{buildroot}/usr/share/ClusterTools2/samples/
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

%files
%defattr(-,root,root)
/usr/sbin/*
/usr/share/ClusterTools2
/usr/lib/ClusterTools2
/usr/lib/systemd/system
%config(noreplace) /etc/ClusterTools2
%config(noreplace) /etc/logrotate.d/*
%doc /usr/share/man/man5/*.gz
%doc /usr/share/man/man7/*.gz
%doc /usr/share/man/man8/*.gz

%changelog
