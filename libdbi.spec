%define debug_package	%{nil}
%define major	1
%define libname %mklibname dbi %{major}
%define devname %mklibname dbi -d

Summary:	Database Independent Abstraction Layer for C
Name:		libdbi
Version:	0.9.0
Release:	6
License:	LGPLv2
Group:		System/Libraries
Url:		http://libdbi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	openjade

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package -n	%{libname}
Summary:	Database Independent Abstraction Layer for C
Group:		System/Libraries

%description -n	%{libname}
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package -n	%{devname}
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	dbi-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{devname}
This package contains the development library and header files.

%prep
%setup -q

# fix dir perms
find -type d | xargs chmod 755

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std 

# nuke installed docs...
rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/libdbi.so.%{major}*

%files -n %{devname}
%doc README TODO doc/programmers-guide doc/driver-guide doc/*.pdf
%{_includedir}/dbi
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

