%global debug_package %{nil}
%global libname %mklibname %{name}
%global devname %mklibname -d %{name}

Name:		canfigger
Version:	0.3.2
Release:	1
URL:		https://github.com/andy5995/canfigger
Source0:	%{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A lightweight library designed to parse configuration files
License:	MIT
Group:		System/Libraries
BuildRequires:	meson
BuildSystem:	meson

%description
A lightweight C language library designed to parse configuration files.
It provides functionality to read them and represent their contents as a
linked list of key-value pairs, along with associated attributes for each pair.

#---- Documentation
%package -n %{name}-docs
Summary:  Documentation for the canfigger library
Group:    Documentation

%description -n %{name}-docs
%{summary}.

%files -n %{name}-docs
%{_docdir}/%{name}


#---- Library
%package -n %{libname}
Summary:	A lightweight library designed to parse configuration files
Group:		System/Libraries

%description -n %{libname}
%{summary}.

%files -n %{libname}
%{_libdir}/lib%{name}.so.*


#---- Devel
%package -n %{devname}
Summary:	Development files for applications which use canfigger
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
%{summary}.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
