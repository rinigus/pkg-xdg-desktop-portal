%global pipewire_version 0.2.6

Name:    xdg-desktop-portal
Version: 1.6.0
Release: 1%{?dist}
Summary: Portal frontend service to flatpak

License: LGPLv2+
URL:     https://github.com/flatpak/xdg-desktop-portal/
Source0: https://github.com/flatpak/xdg-desktop-portal/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: pkgconfig(flatpak)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fuse)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
%{?systemd_requires}
BuildRequires: systemd
Requires:      dbus
# Required version for icon validator.
Recommends:    flatpak >= 1.2.0
# Required for the document portal.
Requires:      /usr/bin/fusermount

%description
xdg-desktop-portal works by exposing a series of D-Bus interfaces known as
portals under a well-known name (org.freedesktop.portal.Desktop) and object
path (/org/freedesktop/portal/desktop). The portal interfaces include APIs for
file access, opening URIs, printing and others.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The pkg-config file for %{name}.


%prep
%setup -q

%build
%configure --disable-docbook-docs --disable-libportal --disable-pipewire --disable-geoclue
%make_build


%install
%make_install
install -dm 755 %{buildroot}/%{_pkgdocdir}
install -pm 644 README.md %{buildroot}/%{_pkgdocdir}
# This directory is used by implementations such as xdg-desktop-portal-gtk.
install -dm 755 %{buildroot}/%{_datadir}/%{name}/portals

%find_lang %{name}


%files -f %{name}.lang
%doc %{_pkgdocdir}
%license COPYING
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.*.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.impl.portal.*.xml
%{_datadir}/dbus-1/services/org.freedesktop.portal.Desktop.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Documents.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.PermissionStore.service
%{_datadir}/%{name}
%{_libexecdir}/xdg-desktop-portal
%{_libexecdir}/xdg-document-portal
%{_libexecdir}/xdg-permission-store
%{_userunitdir}/%{name}.service
%{_userunitdir}/xdg-document-portal.service
%{_userunitdir}/xdg-permission-store.service

%files devel
%{_datadir}/pkgconfig/xdg-desktop-portal.pc


%changelog
* Fri Dec 20 2019 David King <amigadave@amigadave.com> - 1.6.0-1
- Update to 1.6.0

* Thu Dec 12 2019 David King <amigadave@amigadave.com> - 1.5.4-1
- Update to 1.5.4

* Thu Nov 28 2019 David King <amigadave@amigadave.com> - 1.5.3-1
- Update to 1.5.3

* Tue Oct 29 2019 David King <amigadave@amigadave.com> - 1.5.2-1
- Update to 1.5.2 (#1766780)

* Tue Oct 22 2019 David King <amigadave@amigadave.com> - 1.5.1-1
- Update to 1.5.1 (#1714704)

* Fri Oct 04 2019 David King <amigadave@amigadave.com> - 1.5.0-1
- Update to 1.5.0

* Mon Sep 16 2019 Kalev Lember <klember@redhat.com> - 1.4.2-3
- Avoid a hard dep on pipewire daemon

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Kalev Lember <klember@redhat.com> - 1.4.2-1
- Update to 1.4.2

* Thu Feb 14 2019 David King <amigadave@amigadave.com> - 1.2.0-3
- Drop icon validator Requires to Recommends

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 David King <amigadave@amigadave.com> - 1.2.0-1
- Update to 1.2.0 (#1669552)

* Wed Jan 16 2019 Kalev Lember <klember@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Tue Oct 09 2018 David King <amigadave@amigadave.com> - 1.0.3-1
- Update to 1.0.3

* Mon Sep 03 2018 David King <amigadave@amigadave.com> - 1.0.2-1
- Update to 1.0.2

* Mon Aug 20 2018 David King <amigadave@amigadave.com> - 1.0-1
- Update to 1.0

* Wed Aug 01 2018 Jan Grulich <jgrulich@redhat.com> - 0.99-2
- Rebuild PipeWire 0.2.2

* Tue Jul 24 2018 David King <amigadave@amigadave.com> - 0.99-1
- Update to 0.99

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 David King <amigadave@amigadave.com> - 0.11-1
- Update to 0.11 (#1545225)

* Wed Feb 14 2018 David King <amigadave@amigadave.com> - 0.10-1
- Update to 0.10 (#1545225)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Nov 19 2017 David King <amigadave@amigadave.com> - 0.9-1
- Update to 0.9 (#1514774)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 David King <amigadave@amigadave.com> - 0.8-1
- Update to 0.8 (#1458969)

* Fri Mar 31 2017 David King <amigadave@amigadave.com> - 0.6-1
- Update to 0.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 David King <amigadave@amigadave.com> - 0.5-1
- Update to 0.5

* Thu Dec 01 2016 David King <amigadave@amigadave.com> - 0.4-1
- Update to 0.4

* Fri Sep 02 2016 David King <amigadave@amigadave.com> - 0.3-1
- Update to 0.3

* Fri Jul 29 2016 David King <amigadave@amigadave.com> - 0.2-1
- Update to 0.2 (#1361575)

* Tue Jul 12 2016 David King <amigadave@amigadave.com> - 0.1-2
- Own the portals directory

* Mon Jul 11 2016 David King <amigadave@amigadave.com> - 0.1-1
- Initial Fedora packaging
