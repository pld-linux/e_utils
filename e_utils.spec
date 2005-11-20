Summary:	e_utils
Name:		e_utils
Version:	0.0.1
%define	_snap	20051116
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.bz2
# Source0-md5:	6d098dd1a076f7d81a0647f64810187c
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje
BuildRequires:	engrave-devel
BuildRequires:	enlightenmentDR17-devel
BuildRequires:	esmart-devel
BuildRequires:	ewl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e_utils

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/e17setroot

%attr(755,root,root) %{_bindir}/e_util_eapp_edit
#%{_datadir}/%{name}/data/e_utils_eapp_edit/*

%attr(755,root,root) %{_bindir}/emblem
#%{_datadir}/%{name}/data/emblem/*
%{_datadir}/enlightenmentDR17/config-apps/emblem.eap

%attr(755,root,root) %{_bindir}/entangle
#%{_datadir}/%{name}/data/entangle/*
%{_datadir}/enlightenmentDR17/config-apps/entangle.eap

%attr(755,root,root) %{_bindir}/exige
#%{_datadir}/%{name}/data/exige/*

%attr(755,root,root) %{_bindir}/ethemes
%{_datadir}/enlightenmentDR17/config-apps/ethemes.eap
