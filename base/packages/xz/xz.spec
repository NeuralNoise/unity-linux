%global _arch %(uname -m)
%define _target_platform %{_arch}-unity-linux-musl
%define _libdir /usr/lib64
%define _lib /lib64

Name:		xz	
Version:	5.2.1
Release:	1%{?dist}
Summary:	LZMA compression utilities

Group:		Applications/File
License:	GPLv2+ and Public Domain
URL:		http://tukaani.org/%{name}/
Source0:	http://tukaani.org/%{name}/%{name}-%{version}.tar.xz

Requires:	%{name}-libs = %{version}-%{release}

%description
XZ Utils are an attempt to make LZMA compression easy to use on free (as in
freedom) operating systems. This is achieved by providing tools and libraries
which are similar to use than the equivalents of the most popular existing
compression algorithms.

LZMA is a general purpose compression algorithm designed by Igor Pavlov as
part of 7-Zip. It provides high compression ratio while keeping the
decompression speed fast.

%package 	libs
Summary:	Libraries for decoding LZMA compression
Group:		System Environment/Libraries
License:	Public Domain

%description 	libs
Libraries for decoding files compressed with LZMA or XZ utils.


%package        devel
Summary:        Development libraries for decoding LZMA compression
Group:          Development/Libraries
License:        Public Domain
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig

%description    devel
Development libraries for decoding files compressed with LZMA or XZ utils.

%prep
%setup -q


%build
./configure \
	--prefix=/usr \
	--disable-rpath \
	--disable-werror \
	--libdir=%{_libdir} \
	--disable-static 

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS COPYING COPYING.GPLv2 NEWS README THANKS TODO

%{_bindir}/lzdiff
%{_bindir}/xzegrep
%{_bindir}/lzless
%{_bindir}/xzdiff
%{_bindir}/lzgrep
%{_bindir}/xzless
%{_bindir}/xzmore
%{_bindir}/lzcat
%{_bindir}/xz
%{_bindir}/xzfgrep
%{_bindir}/lzcmp
%{_bindir}/unlzma
%{_bindir}/lzfgrep
%{_bindir}/lzmainfo
%{_bindir}/lzegrep
%{_bindir}/unxz
%{_bindir}/xzgrep
%{_bindir}/xzcmp
%{_bindir}/lzmadec
%{_bindir}/xzcat
%{_bindir}/xzdec
%{_bindir}/lzma
%{_bindir}/lzmore
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_mandir}/man*/*.*

%files libs
%{_libdir}/liblzma.so.5
%{_libdir}/liblzma.so.5.2.1

%files devel
%{_includedir}/lzma/*.h
%{_includedir}/lzma.h
%dir %{_includedir}/lzma
%{_libdir}/*.so
%{_libdir}/pkgconfig/liblzma.pc
%{_docdir}/xz/

%changelog
* Mon Dec 07 2015 JMiahMan <JMiahMan@unity-linux.com> - 5.2.1-1
- Rebuild for rpm4

