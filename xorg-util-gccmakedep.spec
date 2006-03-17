Summary:	gccmakedep utility
Summary(pl):	Narzêdzie gccmakedep
Name:		xorg-util-gccmakedep
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/util/gccmakedep-X11R7.0-%{version}.tar.bz2
# Source0-md5:	328eea864d27b2d3a88ceb2fa66eca6d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gccmakedep utility.

%description -l pl
Narzêdzie gccmakedep.

%prep
%setup -q -n gccmakedep-X11R7.0-%{version}

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
