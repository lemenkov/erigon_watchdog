# SPDX-FileCopyrightText: 2025 Peter Lemenkov <lemenkov@gmail.com>
# SPDX-License-Identifier: MIT

Name:           erigon_watchdog
Version:        2.0.2
Release:        %autorelease
Summary:        A simple watchdog application for Erigon
License:        MIT
URL:            https://github.com/lemenkov/erigon_watchdog
VCS:            git:%{url}.git
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  systemd-rpm-macros
Requires:       polkit
Requires:       python3-dbus

%description
%{summary}.

%prep
%autosetup -p1

%install
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 0600 %{name}.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -D -p -m 0644 10-erigon-watchdog.rules %{buildroot}%{_datadir}/polkit-1/rules.d/10-erigon-watchdog.rules

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_datadir}/polkit-1/rules.d/10-erigon-watchdog.rules
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog
%autochangelog
