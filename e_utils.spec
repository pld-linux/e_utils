Summary:	e_utils - useful utilities for Enlightenment DR17
Summary(pl):	e_utils - przydatne narzêdzia dla Enlightenmenta DR17
Name:		e_utils
Version:	0.0.1
%define	_snap	20060312
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.bz2
# Source0-md5:	c2ddb92830739da17ddc9f03821abace
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
e_utils - useful utilities for Enlightenment DR17.

%description -l pl
e_utils - przydatne narzêdzia dla Enlightenmenta DR17.

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
%attr(755,root,root) %{_bindir}/e17genmenu

%attr(755,root,root) %{_bindir}/e17setroot

%attr(755,root,root) %{_bindir}/e_util_eapp_edit
#%{_datadir}/%{name}/data/e_utils_eapp_edit

%attr(755,root,root) %{_bindir}/emblem
#%{_datadir}/%{name}/data/emblem
%{_datadir}/enlightenmentDR17/config-apps/emblem.eap

%attr(755,root,root) %{_bindir}/entangle
#%{_datadir}/%{name}/data/entangle
%{_datadir}/enlightenmentDR17/config-apps/entangle.eap

%attr(755,root,root) %{_bindir}/exige
#%{_datadir}/%{name}/data/exige

%attr(755,root,root) %{_bindir}/ethemes
%{_datadir}/enlightenmentDR17/config-apps/ethemes.eap
