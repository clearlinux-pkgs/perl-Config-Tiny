#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Config-Tiny
Version  : 2.23
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.23.tgz
Source0  : https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.23.tgz
Summary  : Read/Write .ini style files with as little code as possible
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-2.0
Requires: perl-Config-Tiny-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
See also: Changes and Changelog.ini.
Warning: WinZip 8.1 and 9.0 both contain an 'accidental' bug which stops
them recognizing POSIX-style directory structures in valid tar files.
You are better off using a reliable tool such as InfoZip:
ftp://ftp.info-zip.org/pub/infozip/

%package dev
Summary: dev components for the perl-Config-Tiny package.
Group: Development
Provides: perl-Config-Tiny-devel = %{version}-%{release}
Requires: perl-Config-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Config-Tiny package.


%package license
Summary: license components for the perl-Config-Tiny package.
Group: Default

%description license
license components for the perl-Config-Tiny package.


%prep
%setup -q -n Config-Tiny-2.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-Tiny
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-Tiny/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Config/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-Tiny/LICENSE
