# ------------------------------------------------------------------------------
# Copyright (c) 2011-2018 SUSE Linux GmbH, Nuernberg, Germany.
# Copyright (c) 2019-2023 SUSE LLC
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of version 2 of the GNU General Public License as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, contact SUSE Linux GmbH.
#
# ------------------------------------------------------------------------------

PKG=ClusterTools2
SPECFILE=spec/$(PKG).spec
CHANGESFILE=spec/$(PKG).changes

VERSION=$(strip $(patsubst Version:,,$(shell grep '^Version:' $(SPECFILE))))
RELEASE=$(strip $(patsubst Release:,,$(shell grep '^Release:' $(SPECFILE))))

# OBS local project path: set it as a command line argument or as an ENV variable
OBSPROJ ?= "placeholder"

default:	all

test:
	echo "--${VERSION}--${RELEASE}--"

tar:
	tar -cvjf ${PKG}-${VERSION}.tgz man? share sbin spec samples etc plugins system

.ONESHELL:
copy:	tar
	@if [ $(OBSPROJ) = "placeholder" ]; then
		echo -e "\e[31mProject directory is missing. Set it via 'OBSPROJ=/path/to/project'\e[0m";
		exit 1;
	fi
	@echo -e "\e[33mCopying the SPEC file, CHANGES file and the tarball to ${OBSPROJ}\e[0m"
	@cp ${CHANGESFILE} ${OBSPROJ}
	@cp ${SPECFILE} ${OBSPROJ}
	@cp ${PKG}-${VERSION}.tgz ${OBSPROJ}
	@echo -e "\e[32mDone\e[0m"

rpm:	tar
	mv ${PKG}-${VERSION}.tbz /usr/src/packages/SOURCES
	cp spec/${PKG}.spec /usr/src/packages/SPECS
	( cd /usr/src/packages; sudo rpmbuild -ba --target noarch SPECS/${PKG}.spec )

all:	tar rpm
	echo building ${PKG}-${VERSION}-${RELEASE}
