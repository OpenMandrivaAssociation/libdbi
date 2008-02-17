%define	major 0
%define libname %mklibname dbi %{major}
%define develname %mklibname dbi -d

Summary:	Database Independent Abstraction Layer for C
Name:		libdbi
Version:	0.8.3
Release:	%mkrel 1
License:	LGPL
Group:		System/Libraries
URL:		http://libdbi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
BuildRequires:	openjade
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-dtd41-sgml
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package -n	%{libname}
Summary:	Database Independent Abstraction Layer for C
Group:          System/Libraries

%description -n	%{libname}
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

%package -n	%{develname}
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	dbi-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname dbi 0 -d}

%description -n	%{develname}
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the static library and header files.

%prep

%setup -q -n %{name}-%{version}

# fix dir perms
find -type d | xargs chmod 755

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# nuke installed docs...
rm -rf %{buildroot}%{_docdir}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README TODO doc/programmers-guide doc/driver-guide doc/*.pdf
%{_includedir}/dbi
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
