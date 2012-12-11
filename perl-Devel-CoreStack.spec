%define upstream_name    Devel-CoreStack
%define upstream_version 1.3

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Try to generate a stack dump from a core file
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Devel-CoreStack/
Source0:	http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Try to generate a stack dump from a core file.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 1.300.0-2mdv2011.0
+ Revision: 681397
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.300.0-1mdv2011.0
+ Revision: 504941
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.3-6mdv2010.0
+ Revision: 430409
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.3-5mdv2009.0
+ Revision: 256629
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-3mdv2008.1
+ Revision: 136992
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 01 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3-2mdv2007.0
+ Revision: 89742
- use the mkrel macro
- Import perl-Devel-CoreStack

* Sat Nov 05 2005 Oden Eriksson <oeriksson@mandriva.com> 1.3-1mdk
- initial Mandriva package

