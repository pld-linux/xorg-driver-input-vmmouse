Summary:	VMMouse protocol for VMware virtual machines
Summary(pl.UTF-8):	Sterownik protokołu VMMouse dla maszyn wirtualnych VMware
Name:		xorg-driver-input-vmmouse
Version:	12.7.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
# Source0-md5:	dc77181330f983c7d0ec1ea1592c2ca7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.6.0
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.6.0
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The VMMouse driver enables support for the special VMMouse protocol
that is provided by VMware virtual machines to give absolute pointer
positioning.

%description -l pl.UTF-8
Sterownik VMMouse dodaje obsługę specjalnego protokołu VMMouse
udostępnianego przez maszyny wirtualne VMware do przekazywania
bezwzględnego położenia wskaźnika.

%prep
%setup -q -n xf86-input-vmmouse-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/vmmouse_detect
%attr(755,root,root) %{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_datadir}/X11/xorg.conf.d/50-vmmouse.conf
/lib/udev/rules.d/69-xorg-vmmouse.rules
%{_mandir}/man1/vmmouse_detect.1*
%{_mandir}/man4/vmmouse.4*
