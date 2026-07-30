%define upstream_name    Devel-CoreStack
%define upstream_version 1.3
Name:		perl-%{upstream_name}
Version:	1.3
Release:	1

Summary:	Try to generate a stack dump from a core file
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Devel-CoreStack/
Source0:	https://cpan.metacpan.org/authors/id/A/AD/ADESC/Devel-CoreStack-1.3.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Try to generate a stack dump from a core file.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS="vendor" < /dev/null
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(-, root, root, 0755)
%{perl_vendorlib}/Devel/CoreStack.pm
%{_mandir}/man3/*

