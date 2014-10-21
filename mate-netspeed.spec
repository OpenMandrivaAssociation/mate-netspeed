%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	MATE applet that shows traffic on a network device
Name:		mate-netspeed
Version:	1.8.0
Release:	2
Group:		Graphical desktop/GNOME
License:	GPLv2+
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)

%description
netspeed is a little MATE applet that shows the traffic on a
specified network device (for example eth0) in kbytes/s.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x

%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README TODO
%{_libexecdir}/mate-netspeed-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.NetspeedApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/netspeed-menu.xml
%{_iconsdir}/hicolor/*/*/*

