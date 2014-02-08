%define		_class		Validate
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.8.5
Release:	2
Summary:	Validation class
License:	BSD
Group:		Development/PHP
URL:		http://pear.php.net/package/Validate/
Source0:	http://download.pear.php.net/package/Validate-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Package to validate various datas. It includes :
- numbers (min/max, decimal or not),
- email (syntax, domain check),
- string (predifined type alpha upper and/or lowercase, numeric,...),
- date (min, max),
- Credit cards,
- possibility valid multiple data with a single method call
  (::multiple).

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-2mdv2011.0
+ Revision: 667647
- mass rebuild

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 587646
- update to new version 0.8.4

* Thu Sep 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.3-1mdv2011.0
+ Revision: 576926
- update to new version 0.8.3

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.8.2-3mdv2010.1
+ Revision: 466332
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.8.2-2mdv2010.0
+ Revision: 426673
- rebuild

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.8.2-1mdv2009.1
+ Revision: 368257
- Update php pear Validate to 0.8.2 version

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2mdv2009.1
+ Revision: 321933
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-1mdv2009.0
+ Revision: 272600
- 0.8.1

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.0-3mdv2009.0
+ Revision: 224888
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-2mdv2008.1
+ Revision: 178552
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.0-1mdv2008.0
+ Revision: 15548
- 0.7.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.3-1mdv2007.0
+ Revision: 81248
- Import php-pear-Validate

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.3-1mdk
- 0.6.3

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-1mdk
- 0.6.2
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.1-1mdk
- initial Mandriva package (PLD import)


