#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	C3-Adopt-NEXT
Summary:	Class::C3::Adopt::NEXT - make NEXT suck less
#Summary(pl.UTF-8):	
Name:		perl-Class-C3-Adopt-NEXT
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	18153deca0c0dcb9b55bcf2581f1874f
URL:		http://search.cpan.org/dist/Class-C3-Adopt-NEXT/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is intended as a drop-in replacement for NEXT, supporting the same
interface, but using Class::C3 to do the hard work. You can then write new
code without NEXT, and migrate individual source files to use Class::C3 or
method modifiers as appropriate, at whatever pace you're comfortable with.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/C3/Adopt
%{_mandir}/man3/*
