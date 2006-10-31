# TODO: webapps
Summary:	phpToDo - todo list written in PHP with MySQL
Summary(pl):	phpToDo - lista rzeczy do zrobienia napisana w PHP i MySQL-u
Name:		phpToDo
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		Applications/Databases/Interfaces
Source0:	ftp://ftp.ftlight.net/pub/phptodo/%{name}-%{version}.tar.gz
# Source0-md5:	45103015d4c2adf46de4d5975269ec99
Source1:	%{name}.conf
URL:		http://php-todo.sourceforge.net/
Requires:	mysql
Requires:	php-mysql >= 4.1.0
Requires:	webserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phptododir	%{_datadir}/%{name}

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
install -d $RPM_BUILD_ROOT{%{_phptododir}/img,/etc/httpd}

install *.php *.css	$RPM_BUILD_ROOT%{_phptododir}
install img/*.png	$RPM_BUILD_ROOT%{_phptododir}/img

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /etc/httpd/httpd.conf ] && ! grep -q "^Include.*%{name}.conf" /etc/httpd/httpd.conf; then
	echo "Include /etc/httpd/%{name}.conf" >> /etc/httpd/httpd.conf
elif [ -d /etc/httpd/httpd.conf ]; then
	ln -sf /etc/httpd/%{name}.conf /etc/httpd/httpd.conf/99_%{name}.conf
fi
if [ -f /var/lock/subsys/httpd ]; then
	/usr/sbin/apachectl restart 1>&2
fi

%preun
if [ "$1" = "0" ]; then
	umask 027
	if [ -d /etc/httpd/httpd.conf ]; then
		rm -f /etc/httpd/httpd.conf/99_%{name}.conf
	else
		grep -v "^Include.*%{name}.conf" /etc/httpd/httpd.conf > \
			/etc/httpd/httpd.conf.tmp
		mv -f /etc/httpd/httpd.conf.tmp /etc/httpd/httpd.conf
		if [ -f /var/lock/subsys/httpd ]; then
			/usr/sbin/apachectl restart 1>&2
		fi
	fi
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL README TODO sql/*
%config(noreplace) %verify(not md5 mtime size) /etc/httpd/%{name}.conf
%dir %{_phptododir}
%attr(664,root,http) %config(noreplace) %{_phptododir}/*.php
%{_phptododir}/*.css
%dir %{_phptododir}/img
%{_phptododir}/img/*.png
