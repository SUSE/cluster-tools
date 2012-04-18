# Version: 2012-02-10 

PKT=ClusterTools2

vers=$(shell awk '/Version:/' spec/$(PKT).spec)
rel=$(shell awk '/Release:/' spec/$(PKT).spec)

#VERS=0.1.0
#REL=1

vA = $(vers:Version:=)
VERS = $(strip ${vA})
rA = $(rel:Release:=)
REL = $(strip ${rA})

default:	all

test:
	echo "--${VERS}--${REL}--"
#	A=$(VERS:Version:%=a%)
#	echo ">>$A<<"
	

tar:	
	tar -cvzf ${PKT}-${VERS}.tgz man? share sbin spec agents lib scripts samples cli etc plugins

rpm:	tar
	mv ${PKT}-${VERS}.tgz /usr/src/packages/SOURCES
	cp spec/${PKT}.spec /usr/src/packages/SPECS
	( cd /usr/src/packages;  sudo rpmbuild -ba --target noarch SPECS/${PKT}.spec )

all:	tar rpm
	echo building ${PKT}-${VERS}-${REL}
#
