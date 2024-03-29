Summary:	gccmakedep utility - create dependencies in makefiles using gcc
Summary(pl.UTF-8):	Narzędzie gccmakedep - tworzenie zależności w makefile'ach przy użyciu gcc
Name:		xorg-util-gccmakedep
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	https://xorg.freedesktop.org/releases/individual/util/gccmakedep-%{version}.tar.xz
# Source0-md5:	9ff16cdec42436affb8b3d3505abdc08
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
The gccmakedep program calls 'gcc -M' to output makefile rules
describing the dependencies of each sourcefile, so that make knows
which object files must be recompiled when a dependency has changed.

%description -l pl.UTF-8
Program gccmakedep wywołuje 'gcc -M', aby uzyskać reguły do pliku
makefile opisujące zależności wszystkich plików źródłowych, dzięki
którym program make wie, które pliki wynikowe należy przekompilować w
przypadku zmiany zależnego pliku źródłowego.

%prep
%setup -q -n gccmakedep-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/gccmakedep
%{_mandir}/man1/gccmakedep.1*
