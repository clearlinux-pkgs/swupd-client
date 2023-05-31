#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : swupd-client
Version  : 5.0.5
Release  : 382
URL      : https://github.com/clearlinux/swupd-client/releases/download/v5.0.5/swupd-client-5.0.5.tar.gz
Source0  : https://github.com/clearlinux/swupd-client/releases/download/v5.0.5/swupd-client-5.0.5.tar.gz
Source1  : swupd-cleanup.service
Source2  : swupd-cleanup.timer
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: swupd-client-autostart = %{version}-%{release}
Requires: swupd-client-bin = %{version}-%{release}
Requires: swupd-client-data = %{version}-%{release}
Requires: swupd-client-license = %{version}-%{release}
Requires: swupd-client-man = %{version}-%{release}
Requires: swupd-client-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : pkgconfig(bsdiff)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi-docutils
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-polkit-files.patch
Patch2: 0002-Disable-forcing-http2.patch
Patch3: silencewarning.patch
Patch4: notelemetry.patch
Patch5: moreinfo.patch
Patch6: log-downloads.patch

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
Requires: swupd-client-license = %{version}-%{release}
Requires: swupd-client-services = %{version}-%{release}

%description bin
bin components for the swupd-client package.


%package data
Summary: data components for the swupd-client package.
Group: Data

%description data
data components for the swupd-client package.


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


%package services
Summary: services components for the swupd-client package.
Group: Systemd services
Requires: systemd

%description services
services components for the swupd-client package.


%prep
%setup -q -n swupd-client-5.0.5
cd %{_builddir}/swupd-client-5.0.5
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
pushd ..
cp -a swupd-client-5.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685501637
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static --disable-tests \
--enable-signature-verification \
--with-contenturl=https://cdn.download.clearlinux.org/update/ \
--with-versionurl=https://cdn.download.clearlinux.org/update/ \
--with-formatid=34 \
--with-fallback-capaths=/usr/share/ca-certs/.prebuilt-store/anchors \
--with-post-update=/usr/bin/update-helper \
--with-build-number=%{release} \
--enable-third-party
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --disable-tests \
--enable-signature-verification \
--with-contenturl=https://cdn.download.clearlinux.org/update/ \
--with-versionurl=https://cdn.download.clearlinux.org/update/ \
--with-formatid=34 \
--with-fallback-capaths=/usr/share/ca-certs/.prebuilt-store/anchors \
--with-post-update=/usr/bin/update-helper \
--with-build-number=%{release} \
--enable-third-party
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
./swupd -v | grep '+SIGVERIFY'
./swupd -v | grep '+STATELESS'
./swupd -v | grep '+THIRDPARTY'
./swupd -v | grep '\-DEBUG_MODE'
./swupd -v | grep '\-FORCE_TARTAR'

VAR=$(./swupd -v | grep "^state directory" | awk '{ print $3 }')
[[ "$VAR" == "/var/lib/swupd" ]]

VAR=$(./swupd -v | grep "^certificate path" | awk '{ print $3 }')
[[ "$VAR" == "/usr/share/clear/update-ca/Swupd_Root.pem" ]]

VAR=$(./swupd -v | grep "^fallback certificate path" | awk '{ print $4 }')
[[ "$VAR" == "/usr/share/ca-certs/.prebuilt-store/anchors" ]]

VAR=$(./swupd -v | grep "^systemd unitdir" | awk '{ print $3 }')
[[ "$VAR" == "/usr/lib/systemd/system" ]]

VAR=$(./swupd -v | grep "^content URL" | awk '{ print $3 }')
[[ "$VAR" == "https://cdn.download.clearlinux.org/update/" ]]

VAR=$(./swupd -v | grep "^version URL" | awk '{ print $3 }')
[[ "$VAR" == "https://cdn.download.clearlinux.org/update/" ]]

VAR=$(./swupd -v | grep "^post-update hook" | awk '{ print $3 }')
[[ "$VAR" == "/usr/bin/update-helper" ]]

FMT=$(./swupd -v | grep "format ID" | awk '{ print $3 }')
[[ "$FMT" == "34" ]]

%install
export SOURCE_DATE_EPOCH=1685501637
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/swupd-client
cp %{_builddir}/swupd-client-%{version}/COPYING %{buildroot}/usr/share/package-licenses/swupd-client/f5b8c6b890f2c7664954577396afb1fed9aa550f || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/swupd-cleanup.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/swupd-cleanup.timer
## Remove excluded files
rm -f %{buildroot}*/usr/lib/systemd/system/check-update.service
rm -f %{buildroot}*/usr/lib/systemd/system/check-update.timer
rm -f %{buildroot}*/usr/lib/systemd/system/multi-user.target.wants/check-update.timer
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d/
install -m644 swupd.bash %{buildroot}/usr/share/defaults/etc/profile.d/50-swupd.bash
mkdir -p %{buildroot}/usr/share/zsh/site-functions/
install -m644 swupd.zsh %{buildroot}/usr/share/zsh/site-functions/_swupd
mkdir -p %{buildroot}/usr/share/defaults/swupd/
install -m644 config %{buildroot}/usr/share/defaults/swupd/config
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -sf ../swupd-update.timer %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
mkdir -p %{buildroot}/usr/lib/systemd/system/timers.target.wants/
ln -sf ../swupd-cleanup.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer
mkdir -p %{buildroot}/usr/share/polkit-1/actions
mkdir -p %{buildroot}/usr/share/polkit-1/rules.d
install -m644 data/org.clearlinux.swupd.policy %{buildroot}/usr/share/polkit-1/actions/
install -m644 data/org.clearlinux.swupd.rules %{buildroot}/usr/share/polkit-1/rules.d/
echo "https://clearlinux-distro-public.s3.us-west-2.amazonaws.com/update/" > %{buildroot}/usr/share/defaults/swupd/mirror_versionurl
echo "https://clearlinux-distro-public.s3.us-west-2.amazonaws.com/update/" > %{buildroot}/usr/share/defaults/swupd/mirror_contenturl
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
/usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/swupd
/V3/usr/bin/verifytime
/usr/bin/swupd
/usr/bin/verifytime

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/50-swupd.bash
/usr/share/defaults/swupd/config
/usr/share/defaults/swupd/mirror_contenturl
/usr/share/defaults/swupd/mirror_versionurl
/usr/share/polkit-1/actions/org.clearlinux.swupd.policy
/usr/share/polkit-1/rules.d/org.clearlinux.swupd.rules
/usr/share/zsh/site-functions/_swupd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/swupd-client/f5b8c6b890f2c7664954577396afb1fed9aa550f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/swupd.1
/usr/share/man/man4/swupd-update.service.4
/usr/share/man/man4/swupd-update.timer.4
/usr/share/man/man4/update-triggers.target.4
/usr/share/man/man7/swupd-alias.7

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/swupd-update.timer
%exclude /usr/lib/systemd/system/timers.target.wants/swupd-cleanup.timer
/usr/lib/systemd/system/swupd-cleanup.service
/usr/lib/systemd/system/swupd-cleanup.timer
/usr/lib/systemd/system/swupd-update.service
/usr/lib/systemd/system/swupd-update.timer
/usr/lib/systemd/system/verifytime.service
