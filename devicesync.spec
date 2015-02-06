%define svn     893106
Name:           devicesync
Version:        0.1
Summary:        An application that lets you transfer data between devices
Release:        3
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.kde.org
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.%{svn}.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  kdelibs4-devel
BuildRequires:  libmtp-devel
BuildRequires:  taglib-devel
Requires:       kdebase4-runtime

%description
An application that lets you transfer data between devices

%files
%defattr(-,root,root)
%{_kde_bindir}/devicesync
%{_kde_libdir}/kde4/devicesync_localstorageplugin.so
%{_kde_libdir}/kde4/devicesync_mtpplugin.so
%{_kde_datadir}/applications/kde4/devicesync.desktop
%{_kde_appsdir}/devicesync
%{_kde_datadir}/config.kcfg/devicesync.kcfg
%doc %{_kde_docdir}/HTML/en/devicesync
%{_kde_iconsdir}/hicolor/*/apps/devicesync.png
%{_kde_datadir}/kde4/services/devicesync_localstorage.desktop
%{_kde_datadir}/kde4/services/devicesync_mtp.desktop
%{_kde_datadir}/kde4/servicetypes/devicesync_plugin.desktop


#------------------------------------------------

%define libdevicesynccore_major 4
%define libdevicesynccore %mklibname devicesynccore %libdevicesynccore_major

%package -n %libdevicesynccore
Summary: %name core library
Group: System/Libraries

%description -n %libdevicesynccore
%name core library.

%files -n %libdevicesynccore
%defattr(-,root,root)
%_kde_libdir/libdevicesynccore.so.%{libdevicesynccore_major}*

#-----------------------------------------------------------------------------

%package devel
Group: Development/KDE and Qt
Summary: Header files and documentation for compiling %name applications
Requires: kdelibs4-devel
Requires: %libdevicesynccore = %version

%description devel
This package includes the header files you will need to compile applications
for %name.

%files devel
%defattr(-,root,root,-)
%{_kde_libdir}/libdevicesynccore.so
%{_kde_includedir}/devicesync

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name

%build

%cmake_kde4
%make


%install
rm -rf %buildroot
cd build
make DESTDIR=%buildroot install
cd ..

%clean
rm -rf %{buildroot}



%changelog
* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 0.1-2mdv2012.0
+ Revision: 707255
- rebuild for new libmtp

* Sat Dec 06 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1-1mdv2009.1
+ Revision: 310922
- import devicesync


