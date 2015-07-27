Summary:	osquery is an operating system instrumentation toolchain
Name:		osquery
Version:	1.5.1
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/facebook/osquery/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	260cb34190316cf38d879ffe33eb1d76
Source1:	https://github.com/osquery/third-party/archive/%{version}/%{name}-third-party-%{version}.tar.gz
# Source1-md5:	40da5c78ae344d5869fa5ef0e3946246
Patch1:		gcc-flags.patch
URL:		https://osquery.io/
BuildRequires:	bison
BuildRequires:	boost-devel >= 1.55.0
BuildRequires:	byacc
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	cryptsetup-devel >= 1.6.7
BuildRequires:	device-mapper-devel
BuildRequires:	doxygen
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gflags-devel >= 2.1.1
BuildRequires:	gmock-devel
BuildRequires:	iptables-devel >= 1.4.21
BuildRequires:	libblkid-devel
BuildRequires:	libdpkg-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	pkg-config >= 0.28
BuildRequires:	python
BuildRequires:	python-argparse
BuildRequires:	python-jinja2
BuildRequires:	python-psutil
BuildRequires:	readline-devel
BuildRequires:	rocksdb-devel >= 3.10.2
BuildRequires:	rocksdb-static >= 3.10.2
BuildRequires:	snappy-devel >= 1.1.1
BuildRequires:	snappy-static >= 1.1.1
BuildRequires:	thrift-devel >= 0.9.1
BuildRequires:	udev-devel >= 1:095
BuildRequires:	yara-devel >= 3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# build fails with CC having spaces
%undefine	with_ccache

%description
osquery exposes an operating system as a high-performance relational
database. This allows you to write SQL-based queries to explore
operating system data. With osquery, SQL tables represent abstract
concepts such as running processes, loaded kernel modules, open
network connections, browser plugins, hardware events or file hashes.

%prep
%setup -q -a1
%patch1 -p1

mv third-party-*/* third-party

%build
install -d build
cd build

OSQUERY_PLATFORM="pld;%{pld_release}" \
OSQUERY_BUILD_VERSION=%{version} \
BUILD_LINK_SHARED=True \
SDK_VERSION=%{version} \
SKIP_TESTS=True \
%cmake \
	..
%{__make} \
	CTEST_OUTPUT_ON_FAILURE=1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/osqueryctl
%attr(755,root,root) %{_bindir}/osqueryd
%attr(755,root,root) %{_bindir}/osqueryi
%{_datadir}/%{name}
%dir /var/log/%{name}
