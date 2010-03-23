Summary:	mms stream downloader
Name:		mimms
Version:	3.2.1
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	http://launchpad.net/mimms/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
# Source0-md5:	ec629d8899551b4789ba15c17402c36f
URL:		https://launchpad.net/mimms
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	libmms
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mms stream downloader.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
        --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/mimms
%{_mandir}/man1/%{name}.1*
%dir %{py_sitescriptdir}/libmimms
%{py_sitescriptdir}/libmimms/*.py[co]
%{py_sitescriptdir}/mimms-*.egg-info
