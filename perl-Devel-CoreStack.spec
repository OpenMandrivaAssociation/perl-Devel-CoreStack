%define rname Devel-CoreStack

Summary:	Try to generate a stack dump from a core file
Name:		perl-%{rname}
Version:	1.3
Release:	%mkrel 5
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Devel-CoreStack/
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADESC/Devel-CoreStack-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
try to generate a stack dump from a core file.

%prep

%setup -q -n %{rname}-%{version}

%build
perl Makefile.PL INSTALLDIRS="vendor" < /dev/null

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{perl_vendorlib}/Devel/CoreStack.pm
%{_mandir}/man3/*


