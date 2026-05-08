Summary:	mms stream downloader
Name:		mimms
Version:	3.2.1
Release:	3
License:	GPL v3
Group:		Applications
Source0:	http://launchpad.net/mimms/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	ec629d8899551b4789ba15c17402c36f
Patch0:		mimms-python3.patch
URL:		https://launchpad.net/mimms
BuildRequires:	python3
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
Requires:	libmms
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mms stream downloader.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mimms
%{_mandir}/man1/%{name}.1*
%dir %{py3_sitescriptdir}/libmimms
%{py3_sitescriptdir}/libmimms/*.py
%dir %{py3_sitescriptdir}/libmimms/__pycache__
%{py3_sitescriptdir}/libmimms/__pycache__/*.pyc
%{py3_sitescriptdir}/mimms-*.egg-info
