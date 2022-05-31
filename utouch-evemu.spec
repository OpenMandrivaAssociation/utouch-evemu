%define major 3
%define libname	%mklibname	%{name} %{major}
%define develname	%mklibname	%{name} -d

%define oname evemu
 
Name:           utouch-evemu
Version:        2.7.0
Release:        1
License:        GPL-3.0
Summary:        Event emulation for the uTouch stack
URL:		https://www.freedesktop.org/wiki/Evemu/
Source0:	https://www.freedesktop.org/software/%{oname}/%{oname}-%{version}.tar.xz
Group:          Graphical desktop/Other

BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(libevdev)
BuildRequires:	xmlto
BuildRequires:	asciidoc

Requires:	%{libname} = %{version}-%{release}
 
%description
uTouch-evemu is a part of the effort to produce an MT device and gesture test
framework, and provides tools to emulate kernel evdev devices.
 
%package -n %{libname}
Summary:        Event emulation for the uTouch stack
Group:          System/Libraries
 
%description -n %{libname}
uTouch-evemu is a part of the effort to produce an MT device and gesture test
framework, and provides tools to emulate kernel evdev devices.
 
%package -n %{develname}
Summary:        Event emulation for the uTouch stack
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Provides:		%{name}-devel = %{version}-%{release}
 
%description -n %{develname}
uTouch-evemu is a part of the effort to produce an MT device and gesture test
framework, and provides tools to emulate kernel evdev devices.
 
This package provides the development files.
 
%prep
%autosetup -n %{oname}-%{version}
 
%build
%configure \
  --disable-static
%make_build
 
%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
 
 
%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/evemu-*
%{_mandir}/man1/evemu-*
%{python_sitelib}/evemu
 
%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*
 
%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
 


%changelog
* Tue Nov 01 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.6-1
+ Revision: 709286
- imported package utouch-evemu


* Sat Oct 29 2011 Matthew Dawkins <mdawkins@unity-linux.org> 1.0.6-1-unity2011
- import for Unity
