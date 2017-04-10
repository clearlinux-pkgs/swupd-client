#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-client
Version  : 3.8.6
Release  : 186
URL      : https://github.com/clearlinux/swupd-client/releases/download/v3.8.6/swupd-client-3.8.6.tar.gz
Source0  : https://github.com/clearlinux/swupd-client/releases/download/v3.8.6/swupd-client-3.8.6.tar.gz
Source1  : swupd-client.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: swupd-client-bin
Requires: swupd-client-config
Requires: swupd-client-autostart
Requires: swupd-client-lib
Requires: swupd-client-data
Requires: swupd-client-doc
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : systemd-dev

%description
The swupd-client package provides a reference implementation of a software
update client which performs file level updates of an OS, preferentially
using binary deltas whenever possible for efficiency under an assumption
that the OS develops with a release process aimed at rapidly deploying
small incremental changes.

%package autostart
Summary: autostart components for the swupd-client package.
Group: Default

%description autostart
autostart components for the swupd-client package.


%package bin
Summary: bin components for the swupd-client package.
Group: Binaries
Requires: swupd-client-data
Requires: swupd-client-config

%description bin
bin components for the swupd-client package.


%package config
Summary: config components for the swupd-client package.
Group: Default

%description config
config components for the swupd-client package.


%package data
Summary: data components for the swupd-client package.
Group: Data

%description data
data components for the swupd-client package.


%package dev
Summary: dev components for the swupd-client package.
Group: Development
Requires: swupd-client-lib
Requires: swupd-client-bin
Requires: swupd-client-data
Provides: swupd-client-devel

%description dev
dev components for the swupd-client package.


%package doc
Summary: doc components for the swupd-client package.
Group: Documentation

%description doc
doc components for the swupd-client package.


%package extras
Summary: extras components for the swupd-client package.
Group: Default

%description extras
extras components for the swupd-client package.


%package lib
Summary: lib components for the swupd-client package.
Group: Libraries
Requires: swupd-client-data
Requires: swupd-client-config

%description lib
lib components for the swupd-client package.


%prep
%setup -q -n swupd-client-3.8.6

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491853937
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%configure --disable-static --disable-tests \
--enable-signature-verification \
--with-contenturl=https://cdn.download.clearlinux.org/update \
--with-versionurl=https://download.clearlinux.org/update \
--with-formatid=12
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491853937
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/swupd-client.conf
## make_install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d/
install -m644 swupd.bash %{buildroot}/usr/share/defaults/etc/profile.d/50-swupd.bash
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -sf ../swupd-update.timer %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer

%files bin
%defattr(-,root,root,-)
/usr/bin/swupd
/usr/bin/verifytime

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/check-update.service
%exclude /usr/lib/systemd/system/check-update.timer
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
/usr/lib/systemd/system/swupd-update.service
/usr/lib/systemd/system/swupd-update.timer
/usr/lib/systemd/system/verifytime.service
/usr/lib/tmpfiles.d/swupd-client.conf

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/50-swupd.bash

%files dev
%defattr(-,root,root,-)
/usr/lib64/libswupd.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man4/*

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer

%files lib
%defattr(-,root,root,-)
/usr/lib64/libswupd.so.2
/usr/lib64/libswupd.so.2.0.0
