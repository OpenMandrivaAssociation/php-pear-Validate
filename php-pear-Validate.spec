%define	_class	Validate
%define	modname	%{_class}

Summary:	Validation class
Name:		php-pear-%{modname}
Version:	0.8.5
Release:	11
License:	BSD
Group:		Development/PHP
Url:		http://pear.php.net/package/Validate/
Source0:	http://download.pear.php.net/package/Validate-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

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
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/docs/*
%{_datadir}/pear/doc/Validate/LICENSE
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml
%{_datadir}/pear/doc/Validate/docs/*
%{_datadir}/pear/test/Validate/tests/*
