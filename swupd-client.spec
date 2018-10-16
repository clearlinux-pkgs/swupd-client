#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : swupd-client
Version  : 3.18.2
Release  : 285
URL      : https://github.com/clearlinux/swupd-client/releases/download/v3.18.2/swupd-client-3.18.2.tar.gz
Source0  : https://github.com/clearlinux/swupd-client/releases/download/v3.18.2/swupd-client-3.18.2.tar.gz
Source1  : swupd-client.tmpfiles
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: swupd-client-autostart = %{version}-%{release}
Requires: swupd-client-bin = %{version}-%{release}
Requires: swupd-client-config = %{version}-%{release}
Requires: swupd-client-data = %{version}-%{release}
Requires: swupd-client-license = %{version}-%{release}
Requires: swupd-client-man = %{version}-%{release}
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libarchive)
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
Requires: swupd-client-data = %{version}-%{release}
Requires: swupd-client-config = %{version}-%{release}
Requires: swupd-client-license = %{version}-%{release}
Requires: swupd-client-man = %{version}-%{release}

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


%package extras
Summary: extras components for the swupd-client package.
Group: Default

%description extras
extras components for the swupd-client package.


%package license
Summary: license components for the swupd-client package.
Group: Default

%description license
license components for the swupd-client package.


%package man
Summary: man components for the swupd-client package.
Group: Default

%description man
man components for the swupd-client package.


%prep
%setup -q -n swupd-client-3.18.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539390519
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-tests \
--enable-signature-verification \
--with-contenturl=https://cdn.download.clearlinux.org/update \
--with-versionurl=https://download.clearlinux.org/update \
--with-formatid=26 \
--with-fallback-capaths=/usr/share/ca-certs/.prebuilt-store/anchors \
--with-post-update=/usr/bin/update-helper
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1539390519
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/swupd-client
cp COPYING %{buildroot}/usr/share/package-licenses/swupd-client/COPYING
%make_install
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/swupd-client.conf
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d/
install -m644 swupd.bash %{buildroot}/usr/share/defaults/etc/profile.d/50-swupd.bash
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -sf ../swupd-update.timer %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
## install_append end

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

%files extras
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swupd-client/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swupd.1
/usr/share/man/man4/check-update.service.4
/usr/share/man/man4/check-update.timer.4
/usr/share/man/man4/swupd-update.service.4
/usr/share/man/man4/swupd-update.timer.4
/usr/share/man/man4/update-triggers.target.4
