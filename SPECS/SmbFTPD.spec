%global debug_package %{nil}
Name:           smbftpd
Version:        2.10
Release:        1%{?dist}
Summary:        smbftpd FTP daemon using Samba-like share management mechanism

License:        BSD
URL:            https://www.twbsd.org/cht/smbftpd/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  perl, gcc, make, byacc, binutils

%description
SmbFTPD is a FTP daemon modified from the FTP daemon of FreeBSD 5.4. Besides keep original FreeBSD ftpd functions, it enhances user permission control, integrate configuration files, and more useful features. It supports SSL/TLS ported from BSDftpd-ssl.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -D_GNU_SOURCE"
./configure \
    --prefix=%{_builddir}/%{name}-%{version}
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -c -m 755 -s %{_builddir}/%{name}-%{version}/smbftpd %{buildroot}%{_sbindir}
install -c -m 755 -s %{_builddir}/%{name}-%{version}/smbftpd-user %{buildroot}%{_bindir}
install -c -m 644 %{_builddir}/%{name}-%{version}/conf/smbftpd.conf %{buildroot}%{_sysconfdir}/%{name}
install -c -m 644 %{_builddir}/%{name}-%{version}/conf/smbftpd_share.conf %{buildroot}%{_sysconfdir}/%{name}

# Systemd service file
install -d -m755 %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/smbftpd.service << 'EOF'
[Unit]
Description = SmbFTPD
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
SyslogIdentifier = smbftpd
ExecStart=/usr/sbin/smbftpd -D -s /etc/smbftpd/smbftpd.conf
Type=forking

[Install]
WantedBy = multi-user.target
EOF

%files
%{_sbindir}/smbftpd
%{_bindir}/smbftpd-user
%{_unitdir}/smbftpd.service
%config(noreplace) %{_sysconfdir}/smbftpd/smbftpd.conf
%config(noreplace) %{_sysconfdir}/smbftpd/smbftpd_share.conf
%doc LICENSE Changelog

%changelog
* Wed Apr 24 2025 John Chen <johnpupu@gmail.com> - 2.10-1
- Initial Rocky Linux 9 packaging for SmbFTPD 2.10.
- Excludes support for --with-ssl, --with-mysql, and --with-pgsql based on configure and Makefile.
- Installs binaries to standard Rocky Linux locations.
- Service file (systemd unit) for SmbFTPD provided for easy integration.
- Provides LICENSE and Changelog as documentation.
