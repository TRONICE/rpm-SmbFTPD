# SmbFTPD RPM Packaging for Rocky Linux 9

This repository contains the RPM **spec file** for building and packaging [SmbFTPD](https://www.twbsd.org/cht/smbftpd/) on **Rocky Linux 9**.

## Overview

- **SmbFTPD** is an enhanced FTP daemon based on FreeBSD ftpd, providing Samba-like share control, advanced user permissions, PAM authentication, and IPv6 support.
- **The source archive (`smbftpd-2.10.tar.gz`) is retrieved from [SourceForge](https://sourceforge.net/projects/smbftpd/)**
- A SHA256 checksum file (`smbftpd-2.10.tar.gz.sha256`) is also provided to verify the integrity of the source tarball.
- **This RPM spec is written for Rocky Linux 9** and does **not** enable MySQL, PostgreSQL, or SSL/TLS features (i.e., no `--with-mysql`, `--with-pgsql`, or `--with-ssl` options).

## Prerequisites

Before building the RPM, make sure you have the necessary tools installed:

```sh
sudo dnf groupinstall "Development Tools"
sudo dnf install rpm-build byacc
```

## Download and Verify Source

1. Download the SmbFTPD source tarball :

   ```sh
   wget https://master.dl.sourceforge.net/project/smbftpd/SmbFTPD/2.10/smbftpd-2.10.tar.gz\?viasf\=1 -O smbftpd-2.10.tar.gz
   ```

2. **Verify the tarball checksum:**

   ```sh
   sha256sum -c smbftpd-2.10.tar.gz.sha256
   ```

   Output should show:

   ```
   smbftpd-2.10.tar.gz: OK
   ```

3. Copy the tarball into your `SOURCES` folder:

   ```sh
   cp smbftpd-2.10.tar.gz ~/rpmbuild/SOURCES/
   ```

## Building the RPM

1. Clone this repository and ensure the spec file is in your `~/rpmbuild/SPECS` folder:

   ```sh
   git clone https://github.com/TRONICE/rpm-SmbFTPD
   cd rpm-SmbFTPD
   cp SmbFTPD.spec ~/rpmbuild/SPECS/
   ```

2. **Build the RPM:**

   ```sh
   rpmbuild -ba ~/rpmbuild/SPECS/SmbFTPD.spec
   ```

   The built RPMs will be in `~/rpmbuild/RPMS/` and `~/rpmbuild/SRPMS/`.

## Installing & Enabling SmbFTPD

After successful build, install with:

```sh
sudo dnf install ~/rpmbuild/RPMS/x86_64/smbftpd-2.10-1*.rpm
```

Enable and start the SmbFTPD service (systemd unit):

```sh
sudo systemctl enable smbftpd
```

Configuration files are installed to:

- `/etc/smbftpd/smbftpd.conf`
- `/etc/smbftpd/smbftpd_share.conf`

You may edit these files to suit your environment.

## Notes

- This package intentionally excludes MySQL, PostgreSQL, and SSL support.
- Only core dependencies (`gcc`, `make`, `byacc`) are required for building.
- For more about SmbFTPD, refer to [SmbFTPD](https://www.twbsd.org/cht/smbftpd/).

------

 **Target Distro:** Rocky Linux 9
