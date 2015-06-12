Name:       media-manager-app
Summary:    A HTML Media Manager application
Version:    1.0.1
Release:    1
Group:      Applications/Multimedia
License:    Apache-2.0
URL:        http://www.tizen.org2
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  common-apps
BuildRequires:  zip
Requires:   pkgmgr
Requires:   lightmediascanner lightmediascanner-test
Requires:   rygel
Requires:   rygel-lms-plugin
Requires:   media-manager

%description
A proof of concept pure html5 UI for Media Manager.

%prep
%setup -q -n %{name}-%{version}

%build
make wgtPkg

%install
rm -rf %{buildroot}
make install_obs "OBS=1" DESTDIR="%{?buildroot}"

%post
su app -c "pkgcmd -i -t wgt -p /opt/usr/apps/.preinstallWidgets/OPENIVI003.MediaManager.wgt -q"

%postun
su app -c "pkgcmd -u -n OPENIVI003 -q"

%files
%defattr(-,root,root,-)
/opt/usr/apps/.preinstallWidgets/OPENIVI003.MediaManager.wgt
%dir /home/app/.cache/media-manager-artwork/
/home/app/.cache/media-manager-artwork/simpleserver.py

