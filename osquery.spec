Summary:	osquery is an operating system instrumentation toolchain
Name:		osquery
Version:	1.5.0
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/facebook/osquery/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af772f7fe7b9b9a3e8ef2abfa69c2d04
Source1:	https://github.com/osquery/third-party/archive/%{version}/%{name}-third-party-%{version}.tar.gz
# Source1-md5:	940f351cef7965b0f57df70d54885ded
Patch0:		platform.patch
Patch1:		gcc-flags.patch
URL:		https://osquery.io/
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	cmake
BuildRequires:	cryptsetup-devel
BuildRequires:	device-mapper-devel
BuildRequires:	doxygen
BuildRequires:	gflags-devel
BuildRequires:	iptables-devel
BuildRequires:	libblkid-devel
BuildRequires:	libdpkg-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libuuid-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	rocksdb-devel
BuildRequires:	rocksdb-static
BuildRequires:	snappy-devel
BuildRequires:	snappy-static
BuildRequires:	thrift-devel
BuildRequires:	udev-devel
BuildRequires:	yara-devel
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
%patch0 -p1
%patch1 -p1

mv third-party-%{version}/* third-party

%build
install -d build
cd build
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
