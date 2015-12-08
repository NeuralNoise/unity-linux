%define _target_platform %{_arch}-unity-linux-musl

Name:           gmp
Version:        6.0.0 
Release:        1%{?dist}
Summary:        A free library for arbitrary precision arithmetic

Group:          System Environment/Libraries
License:        LGPLv3+ or GPLv2+
URL:            http://gmplib.org/
Source0:        ftp://ftp.gmplib.org/pub/gmp-%{version}/gmp-%{version}a.tar.bz2

BuildRequires: binutils-devel
#Requires:       

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

%package devel
Summary: Development tools for the GNU MP arbitrary precision library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libraries, header files and documentation for using the GNU MP 
arbitrary precision library in applications.

%package static
Summary: Development tools for the GNU MP arbitrary precision library
Group: Development/Libraries
Requires: %{name}-devel = %{epoch}:%{version}-%{release}

%description static
The static libraries for using the GNU MP arbitrary precision library 
in applications.

%prep
%setup -q


%build
./configure \
	--host=%{_target_platform} \
	--prefix=/usr \
	--infodir=/usr/share/info \
	--mandir=/usr/share/man \
	--localstatedir=/var/state/gmp \
	--enable-cxx \
	--with-pic \
	--libdir=%{_libdir} \

make ARCH=%{_arch}
make check


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%__rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%__rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%defattr(-,root,root,-)
%{_libdir}/libgmp.so.*
%{_libdir}/libgmpxx.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_includedir}/*.h
%{_infodir}/gmp.info*

%files static
%defattr(-,root,root,-)
%{_libdir}/libgmp.a
%{_libdir}/libgmpxx.a

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> 6.0.0-1
- Initial Release for Unity Linux
