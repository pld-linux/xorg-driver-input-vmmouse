Summary:	VMMouse protocol for VMware virtual machines
Summary(pl.UTF-8):	Sterownik protokołu VMMouse dla maszyn wirtualnych VMware
Name:		xorg-driver-input-vmmouse
Version:	12.5.1
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-vmmouse-%{version}.tar.bz2
# Source0-md5:	1e2feafb8e4f1b670aeb39bcac9fbb18
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
%requires_xorg_xserver_xinput
Requires:	xorg-xserver-server >= 1.0.99.901
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
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/vmmouse_drv.so
%{_mandir}/man4/vmmouse.4*
