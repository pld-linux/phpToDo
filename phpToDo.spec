Summary:	phpToDo - todo list written in PHP with MySQL
Summary(pl):	phpToDo - lista rzeczy do zrobienia napisana w PHP i MySQL-u
Name:		phpToDo
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	ftp://ftp.ftlight.net/pub/phptodo/%{name}-%{version}.tar.gz
URL:		http://php-todo.sourceforge.net/
Requires:	mysql
Requires:	php-mysql >= 4.1.0
Requires:	webserver
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phptododir	/home/services/httpd/html/phptodo

%description
phpToDo is a simple todo list written in PHP with a MySQL backend. It
provides a very simple and efficient way of keeping track of things to
do, and it sorts tasks by their priorities. The user interface is
designed to make usage as easy and efficient as possible.

%description -l pl
phpToDo jest prost± list± rzeczy "ToDo" napisan± w PHP z backendem w
MySQL. Posiada bardzo prosty i efektywny sposób na ¶ledzenie rzeczy do
zrobienia oraz sortowania zadañ wed³ug priorytetów. Interfejs jest
zrobiony aby byæ jak najprostszym.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_phptododir}/img

install *.php *.css	$RPM_BUILD_ROOT%{_phptododir}
install img/*.png	$RPM_BUILD_ROOT%{_phptododir}/img

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO sql/*
%dir %{_phptododir}
%attr(664,root,http) %config(noreplace) %{_phptododir}/*.php
%{_phptododir}/*.css
%{_phptododir}/img/*.png
