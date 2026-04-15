%define		package	Process
%define		php_min_version 8.2
Summary:	Symfony Process Component
Summary(pl.UTF-8):	Komponent Symfony Process
Name:		php-symfony-Process
Version:	7.2.9
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/process/archive/v%{version}/process-%{version}.tar.gz
# Source0-md5:	020560f28cf33035e3cc51eb7ba944e5
URL:		https://symfony.com/doc/current/components/process.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
Obsoletes:	php-symfony2-Process < 7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Process Component executes commands in sub-processes.

%description -l pl.UTF-8
Komponent Process uruchamia polecenia w podprocesach.

%prep
%setup -q -n process-%{version}

%{__rm} Pipes/WindowsPipes.php

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Process
%{php_data_dir}/Symfony/Component/Process/*.php
%{php_data_dir}/Symfony/Component/Process/Exception
%{php_data_dir}/Symfony/Component/Process/Messenger
%{php_data_dir}/Symfony/Component/Process/Pipes
