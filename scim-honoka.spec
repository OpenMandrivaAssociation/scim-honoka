%define version  0.9.1
%define release  %mkrel 3
%define src_name honoka

%define scim_version   1.4.3

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

Name:       scim-honoka
Summary:    Honoka is an SCIM IMEngine module for Japanese
Version:    %{version}
Release:    %{release}
Group:      System/Internationalization
License:    GPL
URL:        http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%5D%5D
Source0:    %{src_name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Provides:      honoka, libhonoka
Obsoletes:     honoka, libhonoka
Requires:      %{libname} = %{version}
Requires:      scim >= %{scim_version}
BuildRequires: scim-devel >= 1.4.7-3mdk
BuildRequires: automake
BuildRequires: libltdl-devel

%description
Honoka is an SCIM IMEngine module for Japanese.


%package -n %{libname}
Summary:    Scim-honoka library
Group:      System/Internationalization
Provides:   %{libname_orig} = %{version}-%{release}

%description -n %{libname}
scim-honoka library.

%package -n %{develname}
Summary:    Headers of scim-honoka for development
Group:      Development/C
Requires:   %{libname} = %{version}
Provides:   %{name}-devel = %{version}-%{release}
Provides:   %{libname_orig}-devel = %{version}-%{release}
Obsoletes:  %libname-devel

%description -n %{develname}
Headers of %{name} for development.


%prep
%setup -q -n %{src_name}-%{version}
cp /usr/share/automake-1.10/mkinstalldirs .

%build
[[ -f configure ]] || ./bootstrap

%configure2_5x
# (tv) parallel build is broken:
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang honoka

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f honoka.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/scim/icons/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.so.*
%{scim_plugins_dir}/IMEngine/*.so
%{scim_plugins_dir//SetupUI/*.so

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_includedir}/honoka/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/honoka.pc
%{_libdir}/scim-%{scim_major}/*/*.a
%{_libdir}/scim-%{scim_major}/*/*.la
