Summary:	ripMIME extract the attached files out of a MIME encoded email package
Name:		ripmime	
Version:	1.2.7
Release:	1
License:	BSD
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
URL:		http://www.pldaniels.com/ripmime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com). ripMIME has
been written with one sole purpose in mind, to extract the attached
files out of a MIME encoded email package.

%prep
%setup  -q

%build
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install ripmime	$RPM_BUILD_ROOT%{_bindir}

gzip -9nf CHANGELOG INSTALL LICENSE README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  *.gz
%attr(755,root,root) %{_bindir}/* 
