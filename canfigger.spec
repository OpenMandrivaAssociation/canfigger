%global debug_package %{nil}
%global libname %mklibname %{name} 0
%global devname %mklibname -d %{name}

Name:		canfigger
Version:	0.3.1
Release:	1
Source0:	https://github.com/andy5995/canfigger/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A lightweight library designed to parse configuration files
URL:		https://github.com/andy5995/canfigger
License:	MIT
Group:		System/Libraries
BuildRequires:	fdupes
BuildRequires:	meson

%description
A lightweight C language library designed to parse configuration files.
It provides functionality to read them and represent their contents as a
linked list of key-value pairs, along with associated attributes for each pair.


#---- Library
%package -n %{libname}
Summary:	A lightweight library designed to parse configuration files
Group:		System/Libraries

%description -n %{libname}
%{summary}.


#---- Devel
%package -n %{devname}
Summary:	Development files for applications which use canfigger
Group:		Development/C
Requires:	%{libname} = %{version}

%description -n %{devname}
%{summary}.

%prep
%autosetup -p1

%build
%meson \
	-Ddocdir=%{_docdir}/%{libname}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_docdir}/%{libname}/html

%files -n %{libname}
%{_docdir}/%{libname}
%{_libdir}/lib%{name}.so.*


%files -n %{devname}
%{_includedir}/%{name}.h
%{_includedir}/%{name}_version.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
