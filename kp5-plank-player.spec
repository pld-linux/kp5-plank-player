#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.0
%define		qtver		5.15.2
%define		kpname		plank-player
Summary:	Multimedia Player for playing local files on Plasma Bigscreen
Name:		kp5-%{kpname}
Version:	5.27.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ff2d8e640e2ee57f49ae54f9cb679100
URL:		http://www.kde.org/
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext
BuildRequires:	gstreamer-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kirigami2-devel
BuildRequires:	ninja
BuildRequires:	pipewire-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Multimedia Player for playing local files on Plasma Bigscreen.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/plank-player
%{_desktopdir}/org.plank.player.desktop
%{_iconsdir}/hicolor/128x128/apps/plank-player.png
%{_iconsdir}/hicolor/256x256/apps/plank-player.png
%{_datadir}/metainfo/org.kde.invent.plank_player.metainfo.xml
