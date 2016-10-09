Name:           winetricks
Version:        20161005
Release:        2%{?dist}
Summary:        Work around common problems in Wine

License:        LGPLv2+
URL:            https://github.com/Winetricks/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Originally uploaded by Jose Hevia for OCAL 0.18
# https://openclipart.org/detail/107599/exec-wine
Source1:        https://openclipart.org/download/107599/exec-wine.svg

BuildArch:      noarch
BuildRequires:  desktop-file-utils

# runtime dependencies
Requires:       wine-common >= 1.9
Requires:       wine-wow
Requires:       cabextract gzip unzip wget which time
Requires:       hicolor-icon-theme

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.


%prep
%setup -q
sed -i -e s:steam:: -e s:flash:: tests/*

%build
# not needed

%install
%make_install
install -m0755 -d %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m0755 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -m0755 -d %{buildroot}%{_datadir}/applications
cat <<EOT >>%{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Winetricks
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=System;
StartupNotify=true
EOT

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :



%files
%license src/COPYING debian/copyright
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-2
- use apps subfolger for icon

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-1
- new version
- add copyright
- add icon

* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 20160724-1
- new version

* Mon Jul 11 2016 Raphael Groner <projects.rg@smart.ms> - 20160709-1
- initial
