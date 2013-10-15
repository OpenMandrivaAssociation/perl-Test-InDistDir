%define upstream_name    Test-InDistDir
%define upstream_version 1.112071

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Test environment setup for development with IDE
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module helps run test scripts in IDEs like Komodo.

When running test scripts in an IDE i have to set up a project file
defining the dist dir to run tests in and a lib dir to load additional
modules from. Often I didn't feel like doing that, especially when i only
wanted to do a small patch to a dist. In those cases i added a BEGIN block
to mangle the environment for me.

This module basically is that BEGIN block. It automatically moves up one
directory when it cannot see the test script in "t/$scriptname" and
includes 'lib' in @INC when there's no blib present. That way the test ends
up with almost the same environment it'd get from EUMM/prove/etc., even
when it's actually run inside the t/ directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*
