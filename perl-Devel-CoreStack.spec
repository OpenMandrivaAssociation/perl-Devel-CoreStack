%define upstream_name    Devel-CoreStack
%define upstream_version 1.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Try to generate a stack dump from a core file
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Devel-CoreStack/
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
try to generate a stack dump from a core file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS="vendor" < /dev/null
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{perl_vendorlib}/Devel/CoreStack.pm
%{_mandir}/man3/*
