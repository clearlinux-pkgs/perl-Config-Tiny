#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Config-Tiny
Version  : 2.30
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.30.tgz
Source0  : https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.30.tgz
Summary  : 'Read/Write .ini style files with as little code as possible'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-Config-Tiny-license = %{version}-%{release}
Requires: perl-Config-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package perl
Summary: perl components for the perl-Config-Tiny package.
Group: Default
Requires: perl-Config-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Config-Tiny package.


%prep
%setup -q -n Config-Tiny-2.30
cd %{_builddir}/Config-Tiny-2.30
pushd ..
cp -a Config-Tiny-2.30 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Config-Tiny
cp %{_builddir}/Config-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Config-Tiny/c44f2a5783a554864280167f63754ee2b1b58be1 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Config::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Config-Tiny/c44f2a5783a554864280167f63754ee2b1b58be1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
