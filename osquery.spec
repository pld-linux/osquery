Summary:	osquery is an operating system instrumentation toolchain
Name:		osquery
Version:	1.5.0
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	https://github.com/facebook/osquery/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af772f7fe7b9b9a3e8ef2abfa69c2d04
URL:		https://osquery.io/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
osquery exposes an operating system as a high-performance relational
database. This allows you to write SQL-based queries to explore
operating system data. With osquery, SQL tables represent abstract
concepts such as running processes, loaded kernel modules, open
network connections, browser plugins, hardware events or file hashes.

%prep
%setup -q

%build
%{__make} deps

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
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
