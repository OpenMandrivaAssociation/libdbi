%define major 1
%define libname %mklibname dbi %{major}
%define develname %mklibname dbi -d

Summary:	Database Independent Abstraction Layer for C
Name:		libdbi
Version:	0.8.4
Release:	5
License:	LGPL
Group:		System/Libraries
URL:		http://libdbi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/libdbi/%{name}-%{version}.tar.gz
BuildRequires:	openjade
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-dtd41-sgml

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

%package -n	%{develname}
Summary:	Library and header files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	dbi-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{develname}
libdbi implements a database-independent abstraction layer in C, similar to the
DBI/DBD layer in Perl. Writing one generic set of code, programmers can
leverage the power of multiple databases and multiple simultaneous database
connections by using this framework.

This package contains the static library and header files.

%prep
%setup -q

# fix dir perms
find -type d | xargs chmod 755

%build
%configure2_5x --disable-static

%make

%install
%makeinstall_std STRIP=/bin/true

# nuke installed docs...
rm -rf %{buildroot}%{_docdir}

%files -n %{libname}
%doc AUTHORS ChangeLog INSTALL README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README TODO doc/programmers-guide doc/driver-guide doc/*.pdf
%{_includedir}/dbi
%{_libdir}/*.so


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-2mdv2011.0
+ Revision: 661455
- mass rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-1mdv2011.0
+ Revision: 609637
- 0.8.4
- new major (1)

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-5mdv2011.0
+ Revision: 601039
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-4mdv2010.1
+ Revision: 519019
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.8.3-3mdv2010.0
+ Revision: 429719
- rebuild

* Fri Jul 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-2mdv2009.0
+ Revision: 233726
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Feb 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.3-1mdv2008.1
+ Revision: 169619
- fix build deps (docbook-dtd41-sgml)
- fix build deps (docbook-style-dsssl)
- fix deps
- 0.8.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2008.0
+ Revision: 81033
- 0.8.2


* Fri Dec 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2007.0
+ Revision: 93762
- Import libdbi

* Wed Aug 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdk
- 0.8.1

* Fri Sep 02 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-1mdk
- 0.8.0

* Wed May 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdk
- rpmlint fixes

* Thu Apr 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdk
- rebuilt against new postgresql libs

* Fri Jun 18 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

