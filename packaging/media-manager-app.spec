Name:       media-manager-app
Summary:    A HTML Media Manager application
Version:    1.0.1
Release:    1
Group:      Applications/System
License:    ASL 2.0
URL:        http://www.tizen.org2
Source0:    %{name}-%{version}.tar.bz2
#BuildRequires:  common
BuildRequires:  zip
Requires:   lightmediascanner lightmediascanner-test
Requires:   rygel
Requires:   rygel-lms-plugins
Requires:   media-manager

%description
A proof of concept pure html5 UI for Media Manager.

%prep
%setup -q -n %{name}-%{version}

%build
make wgtPkg

%install
make install_obs "OBS=1" DESTDIR="%{?buildroot}"

%post
if [ -f /opt/usr/apps/.preinstallWidgets/preinstallDone ]; then
    pkgcmd -i -t wgt -p /opt/usr/apps/.preinstallWidgets/DNA_MediaManager.wgt -q;
fi

%postun
pkgcmd -u -n JLRPOCX003.MediaManager -q

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/DNA_MediaManager.wgt

