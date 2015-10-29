Name:       libxpm
Version:    3.5.11
Release:    1%{?dist}
Summary:    X.Org Pixmap library.
Group:      Development/Libraries
License:    MIT
URL:        http://xorg.freedesktop.org/
Source0:    http://xorg.freedesktop.org/releases/individual/lib/libXpm-%{version}.tar.bz2

BuildRequires: libxt util-macros
BuildRequires: libx11-devel libxext-devel
Requires: mdocml-docs

%description
X.Org Pixmap library..

%package devel                                                          
Summary: Development tools for %{name}.
Group: Development/Libraries                                             
Requires: %{name} = %{version}-%{release}                                
                                                                         
%description devel                                                       
This package contains the header files and development documentation     
for %{name}. If you like to develop programs using %{name}, you will need
to install %{name}-devel. 

%prep
%setup -q -n libXpm-%{version}

%build
#Remove OLD config.sub                                                         
for i in $(find . -name config.guess 2>/dev/null) $(find . -name config.sub 2>/dev/null) ; do \
        [ -f /usr/share/automake-1.15/$(basename $i) ] && %{__rm} -f $i && %{__cp} -fv /usr/share/automake-1.15/$(basename $i) $i ; \
done

ac_cv_search_gettext=no \
./configure \
	--prefix=/usr \
	--sysconfdir=/etc \
                                     
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete

#mv pc file to correct location
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*
%{_libdir}/*.so.*.*.*
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/sxpm.1*

%files devel
%{_libdir}/lib*.so
%{_includedir}/X11/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
