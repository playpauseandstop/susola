Name:           susola
Version:        0.1
Release:        1
Summary:        Different useful scripts for use on openSUSE Linux or other Linux distributions.
Group:          System/Console
License:        BSD License
Url:            http://github.com/playpauseandstop/susola
Requires:       zypper python
Source:         http://github.com/playpauseandstop/%{name}/tarball/%{versio}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Different useful scripts for use on openSUSE Linux or other Linux
distributions.

Contents:
---------
    zypper-bin - Batch install packages.
    zypper-brm - Batch remove packages.
    zypper-iuc - Install update candidates.
    zypper-mrum - Enable, refresh, update and disable repo.
    zypper-ur - Update all repositories to next version.

Authors:
--------
    Igor Davydenko

%prep
%setup

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin

install -s -m 755 zypper-bin $RPM_BUILD_ROOT/usr/bin/zypper-bin
install -s -m 755 zypper-brm $RPM_BUILD_ROOT/usr/bin/zypper-brm
install -s -m 755 zypper-iuc $RPM_BUILD_ROOT/usr/bin/zypper-iuc
install -s -m 755 zypper-mrum $RPM_BUILD_ROOT/usr/bin/zypper-mrum
install -s -m 755 zypper-ur $RPM_BUILD_ROOT/usr/bin/zypper-ur

%clean
rm -rf $RPM_BUILD_ROOT

%post
%postun

%files
%defattr(-,root,root)
%doc README.rst LICENSE

/usr/bin/zypper-bin
/usr/bin/zypper-brm
/usr/bin/zypper-iuc
/usr/bin/zypper-mrum
/usr/bin/zypper-ur

%changelog
* Tue Sep 28 2010 Igor Davydenko <playpauseandstop@gmail.com>
  Initial release.
