#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : httpx
Version  : 0.18.2
Release  : 13
URL      : https://files.pythonhosted.org/packages/c6/57/4db75d83f350813414c2f52318862f52ce29bc0ebaa97b71c9202af32d79/httpx-0.18.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/c6/57/4db75d83f350813414c2f52318862f52ce29bc0ebaa97b71c9202af32d79/httpx-0.18.2.tar.gz
Summary  : The next generation HTTP client.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: httpx-license = %{version}-%{release}
Requires: httpx-python = %{version}-%{release}
Requires: httpx-python3 = %{version}-%{release}
Requires: async_generator
Requires: certifi
Requires: h2
Requires: httpcore
Requires: sniffio
BuildRequires : buildreq-distutils3
BuildRequires : certifi
BuildRequires : h2
BuildRequires : httpcore
BuildRequires : sniffio

%description
<p align="center">
<a href="https://www.python-httpx.org/"><img width="350" height="208" src="https://raw.githubusercontent.com/encode/httpx/master/docs/img/butterfly.png" alt='HTTPX'></a>
</p>

%package license
Summary: license components for the httpx package.
Group: Default

%description license
license components for the httpx package.


%package python
Summary: python components for the httpx package.
Group: Default
Requires: httpx-python3 = %{version}-%{release}

%description python
python components for the httpx package.


%package python3
Summary: python3 components for the httpx package.
Group: Default
Requires: python3-core
Provides: pypi(httpx)
Requires: pypi(certifi)
Requires: pypi(httpcore)
Requires: pypi(rfc3986)
Requires: pypi(sniffio)

%description python3
python3 components for the httpx package.


%prep
%setup -q -n httpx-0.18.2
cd %{_builddir}/httpx-0.18.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624044566
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/httpx
cp %{_builddir}/httpx-0.18.2/LICENSE.md %{buildroot}/usr/share/package-licenses/httpx/2f9a422e6ae22185bd3e9cdaec727ac95ab47bbb
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/httpx/2f9a422e6ae22185bd3e9cdaec727ac95ab47bbb

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
