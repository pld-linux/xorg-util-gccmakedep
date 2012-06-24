Summary:	gccmakedep utility - create dependencies in makefiles using gcc
Summary(pl):	Narz�dzie gccmakedep - tworzenie zale�no�ci w makefile'ach przy u�yciu gcc
Name:		xorg-util-gccmakedep
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/util/gccmakedep-%{version}.tar.bz2
# Source0-md5:	b533c0771dbbaf9b041ff35bb941d3a2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gccmakedep program calls 'gcc -M' to output makefile rules
describing the dependencies of each sourcefile, so that make knows
which object files must be recompiled when a dependency has changed.

%description -l pl
Program gccmakedep wywo�uje 'gcc -M', aby uzyska� regu�y do pliku
makefile opisuj�ce zale�no�ci wszystkich plik�w �r�d�owych, dzi�ki
kt�rym program make wie, kt�re pliki wynikowe nale�y przekompilowa� w
przypadku zmiany zale�nego pliku �r�d�owego.

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
%{_mandir}/man1/gccmakedep.1x*
