Name:          librest

%global        __meson_auto_features disabled
%global        basever 1.0

Version:       0.10.2
Release:       1
Summary:       A library for access to RESTful web services
Group:         Development/Libraries
License:       LGPLv2
URL:           http://www.gnome.org
Source0:       %{name}-%{version}.tar.bz2
Patch1:        meson-file-exists.patch

BuildRequires: meson
BuildRequires: cmake

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
#BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(json-glib-1.0)

BuildRequires: ca-certificates
Obsoletes:     rest <= 0.7.12

%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: rest-devel <= 0.7.12

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%meson \
    --buildtype=release \
    -Dintrospection=false \
    -Dca_certificates=true \
    -Dvapi=false \
    -Dexamples=false \
    -Dgtk_doc=false \
    -Dsoup2=false \
    -Dtests=false \
    %{nil}
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/librest-%{basever}.so.*
%{_libdir}/librest-extras-%{basever}.so.*

%files devel
%{_includedir}/rest-%{basever}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/librest-%{basever}.so
%{_libdir}/librest-extras-%{basever}.so
