Name:		unity-baselayout	
Version:	0.4
Release:	1%{?dist}
Summary:	Unitys filesystem structure and core file	

Group:		System Environment/Base	
License:	GPLv2
URL:		http://unity-linux.org

#Source0:	mkmntdirs.c
Source1:	crontab
Source2:	color_prompt
Source3:	aliases.conf
Source4:	blacklist.conf
Source5:	i386.conf
Source6:	kms.conf
Source7:	group
Source8:	inittab
Source9:	passwd
Source10:	profile
Source11:	protocols
Source12:	services

#BuildRequires:	
#Requires:	

%description
Unitys base file system structure and core files

%prep
%__rm -rf %{buildroot}
mkdir -p %{buildroot}

%build

#Do we need this?
#%__cc %{SOURCE0} -o %{buildroot}/mkmntdirs

# generate shadow
mkdir %{buildroot}/etc
cp %{SOURCE9} %{buildroot}/etc/
awk -F: '{
	pw = ":!:"
	if ($1 == "root") { pw = "::" }
	print($1 pw ":0:::::")
}' %{buildroot}/etc/passwd >> %{buildroot}/etc/shadow
#' fix syntax higlighting

%install
cd %{buildroot}
install -m 0755 -d \
	dev \
	dev/pts \
	dev/shm \
	etc \
	etc/apk \
	etc/conf.d \
	etc/crontabs \
	etc/init.d \
	etc/modprobe.d \
	etc/modules-load.d \
	etc/profile.d \
	etc/network \
	etc/network/if-down.d \
	etc/network/if-post-down.d \
	etc/network/if-pre-up.d \
	etc/network/if-up.d \
	etc/periodic/15min \
	etc/periodic/daily \
	etc/periodic/hourly \
	etc/periodic/monthly \
	etc/periodic/weekly \
	etc/xdg/menus \
	etc/skel \
	etc/sysctl.d \
	etc/xdg/autostart \
	home \
	media/cdrom \
	media/floppy \
	media/usb \
	mnt \
	proc \
	sys \
	bin \
	usr/bin \
	usr/doc \
	usr/include \
	sbin \
	usr/sbin \
	lib \
	usr/lib \
        usr/lib/firmware \
        usr/lib/mdev \
	usr/lib/X11 \
	usr/lib/pkcs11 \
	usr/libexec \
	usr/local/bin \
	usr/local/lib \
	usr/local/share \
	usr/share \
	usr/share/man \
	usr/share/doc \
	usr/share/aclocal \
	usr/share/applications \
	usr/share/pixmaps \
	usr/share/xsessions \
	var/cache/misc \
	var/lib/misc \
	var/lock/subsys \
	var/log \
	var/run \
	var/spool/cron \
	run \

install -d -m 0700 %{buildroot}/root 
install -d -m 1777 %{buildroot}/tmp %{buildroot}/var/tmp
#install -m755 %{buildroot}/mkmntdirs %{buildroot}/sbin/mkmntdirs

install -m644 %{SOURCE1} %{buildroot}/etc/crontabs/root 
install -m644 %{SOURCE2} %{buildroot}/etc/profile.d/

install -m644 \
	%{SOURCE3} \
	%{SOURCE4} \
	%{SOURCE5} \
	%{SOURCE6} \
	%{buildroot}/etc/modprobe.d/

echo "UTC" > %{buildroot}/etc/TZ
echo "localhost" > %{buildroot}/etc/hostname
echo "127.0.0.1 localhost localhost.localdomain" > %{buildroot}/etc/hosts
echo "af_packet" > %{buildroot}/etc/modules

cat > %{buildroot}/etc/shells <<EOF
# valid login shells
/bin/sh
/bin/ash
/bin/bash
EOF

cat > %{buildroot}/etc/motd <<EOF
Welcome to Unity!

The Unity Wiki contains a large amount of how-to guides and general
information about administrating Unity systems.
See <http://www.unity-linux.org>.

You can setup the system with the command: setup-unity

You may change this message by editing /etc/motd.

EOF

cat > %{buildroot}/etc/sysctl.conf <<EOF
# content of this file will override /etc/sysctl.d/*
EOF

cat > %{buildroot}/etc/sysctl.d/00-unity.conf <<EOF
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.conf.all.rp_filter = 1
kernel.panic = 120
EOF

cat > %{buildroot}/etc/fstab <<EOF
/dev/cdrom      /media/cdrom    iso9660 noauto,ro 0 0
/dev/usbdisk    /media/usb      vfat    noauto,ro 0 0
EOF

install -m644 \
	%{SOURCE7} \
	%{SOURCE8} \
	%{SOURCE10} \
	%{SOURCE11} \
	%{SOURCE12} \
	%{buildroot}/etc/ 


echo %{version} > %{buildroot}/etc/unity-release

# create /etc/issue
cat > %{buildroot}/etc/issue <<EOF
Welcome to Unity Linux %{version}
Kernel \\r on an \\m (\\l)
EOF


cat > %{buildroot}/etc/os-release <<EOF
NAME="Unity Linux"
ID=unity
VERSION_ID=%{version}
PRETTY_NAME="Unity Linux v%{version}"
HOME_URL="http://unity-linux.org"
BUG_REPORT_URL="http://bugs.unity-linux.org"
EOF

%post
if [ ! -L /var/spool/cron/crontabs ];
then
	ln -s /etc/crontabs /var/spool/cron/crontabs
fi
exit 0

if [ ! -e /etc/mtab ];
then
	ln -s /proc/mounts /etc/mtab
fi
exit 0

%files
%dir /bin
%dir /etc/network
%dir /usr/doc
%dir /usr/lib/X11
%dir /usr/share/man
%dir /usr/share/doc
%dir /usr/share/applications
%dir /usr/share/pixmaps
%dir /usr/share/xsessions
%dir /etc/xdg/autostart
/bin/
/usr/bin
/dev
/etc/
%dir /etc
%dir /etc/crontabs
%dir /etc/skel
%dir /etc/sysctl.d
/home
/lib
/usr/lib
/media
/mnt
/proc
/sbin
/usr/sbin
/sys
/usr
/var
/run
%config(noreplace) /etc/group
%config(noreplace) /etc/passwd
%config(noreplace) /etc/shadow
/etc/os-release
/etc/issue
/etc/unity-release
/etc/fstab
/etc/sysctl.d/00-unity.conf
/etc/sysctl.conf
/etc/motd
/etc/shells
/etc/TZ
/etc/crontabs/root
/etc/profile.d/

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> 0.4-1
- Initial release for Unity-Linux
