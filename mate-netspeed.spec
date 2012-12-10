Summary:	MATE applet that shows traffic on a network device
Name:		mate-netspeed
Version:	1.4.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd44-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-2.0)

%description
netspeed is a little MATE applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-scrollkeeper

%make LIBS='-lm'

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_libexecdir}/mate_netspeed_applet2
%{_libexecdir}/matecomponent/servers/*
%{_iconsdir}/hicolor/*/*/*



%changelog
* Thu Jun 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 803059
- imported package mate-netspeed

