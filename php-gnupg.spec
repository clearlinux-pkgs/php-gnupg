#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-gnupg
Version  : 1.5.1
Release  : 33
URL      : https://pecl.php.net/get/gnupg-1.5.1.tgz
Source0  : https://pecl.php.net/get/gnupg-1.5.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-gnupg-lib = %{version}-%{release}
Requires: php-gnupg-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : gnupg
BuildRequires : gpgme-dev

%description
# PHP GnuPG
The php-gnupg is a wrapper for GpgME library that provides access to GnuPG.

%package lib
Summary: lib components for the php-gnupg package.
Group: Libraries
Requires: php-gnupg-license = %{version}-%{release}

%description lib
lib components for the php-gnupg package.


%package license
Summary: license components for the php-gnupg package.
Group: Default

%description license
license components for the php-gnupg package.


%prep
%setup -q -n gnupg-1.5.1
cd %{_builddir}/gnupg-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-gnupg
cp %{_builddir}/gnupg-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-gnupg/58e51807a8d0a189e596e76757ae35bad9bcf830
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/gnupg.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-gnupg/58e51807a8d0a189e596e76757ae35bad9bcf830
