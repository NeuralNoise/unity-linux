Name:		beecrypt	
Version:	4.2.1
Release:	1%{?dist}
Summary:	A general-purpose cryptography library

Group:		System Environment/Libraries
License:	LGPL2+
URL:		http://beecrypt.sourceforge.net/
#Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source0:	http://repository.timesys.com/buildsources/b/beecrypt/beecrypt-4.2.1/beecrypt-4.2.1.tar.gz	

BuildRequires: libtool, m4	
Requires:	libgomp5.1	

%description
BeeCrypt is an ongoing project to provide a strong and fast cryptography
toolkit. Includes entropy sources, random generators, block ciphers, hash
functions, message authentication codes, multiprecision integer routines
and public key primitives.

%package devel
Summary:	Development files for the beecrypt toolkit and library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The beecrypt-devel package includes header files and libraries necessary
for developing programs which use the beecrypt C toolkit and library. And
beecrypt is a general-purpose cryptography library.

%prep
%setup -q

%build
LIBS=-lgomp \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--enable-threads \
	--enable-shared \
	--without-java \
	--without-python \
	--with-cplusplus=no


make libaltdir=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
make libaltdir=%{_libdir} DESTDIR=%{buildroot} install
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_libdir}/*.a

ln -sf %{_includedir}/beecrypt/* %{buildroot}/%{_includedir}/

%files
%{_libdir}/libbeecrypt.so.7.0.0
%{_libdir}/libbeecrypt.so.7

%files devel
%{_includedir}
%{_libdir}/libbeecrypt.so

%changelog
* Mon Nov 30 2015 JMiahMan <JMiahMan@unity-linux.org> - 4.2.1-1
- Initial build for Unity-Linux
