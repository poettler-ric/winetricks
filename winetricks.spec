Name:           winetricks
Version:        20160724
Release:        1%{?dist}
Summary:        Work around common problems in Wine

License:        LGPLv2+
URL:            https://github.com/Winetricks/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  desktop-file-utils

# runtime dependencies
Requires:       wine-common >= 1.9
Requires:       wine-wow
Requires:       cabextract gzip unzip wget which time

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


%files
%license src/COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 20160724-1
- new version

* Mon Jul 11 2016 Raphael Groner <projects.rg@smart.ms> - 20160709-1
- initial
