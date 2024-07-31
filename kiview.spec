Name:           kiview
Version:        1.1
Release:        2
License:        GPL-3.0
Summary:        Quick preview of files and folder in Dolphin
Url:            https://github.com/Nyre221/Kiview
Source0:        https://invent.kde.org/danagost/Kiview/-/archive/v%{version}/Kiview-v%{version}.tar.bz2
Group:          Application,KDE,Qt,Utility

BuildRequires: appstream
BuildRequires: cmake
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
#BuildRequires: qqc2-desktop-style-devel
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineQuick)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: unzip


Requires: glibc
Requires: qt6-qtwebengine
Requires: kf6-kirigami
Requires: kf6-ki18n
Requires: kf6-kcoreaddons
R#equires: qqc2-desktop-style
Requires: gstreamer1.0-libav
Requires: gstreamer1.0-plugins-bad
Requires: wl-clipboard
#FIXME# In extra repo so lets make it recommends for now.
Recommends: xclip


%description
Kiview gives the user the ability to quickly preview different file types without the need to launch the default application.

Supported file types:
.txt,.sh,.pdf,.doc,.docx,.odt,.ods,.xlsx,.xls,.csv,.odp,.ppt,.pptx,.png,.jpg,.jpeg,.kra,.svgz,.svg,.mp4,.mp3,.webm,.zip,.gz,.xz,.rar

Known Issues:
Currently due to the way it integrates with dolphin, the last item copied to the clipboard is modified and then restored.
This isn't a problem if it's just text, but unfortunately it can't restore the contents if the last item copied was a folder or file.

%prep
%autosetup -n Kiview-v%{version} -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr .
%make_build


%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/applications/io.github.nyre221.kiview.desktop
%{_datadir}/icons/hicolor/128x128/apps/io.github.nyre221.kiview.svg
%{_datadir}/metainfo/io.github.nyre221.kiview.appdata.xml
