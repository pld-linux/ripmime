Summary:	ripMIME extract the attached files out of a MIME encoded email package
Summary(pl.UTF-8):	Narzędzie wyciągające załączniki z wiadomości kodowanych MIME
Name:		ripmime
Version:	1.4.0.3
Release:	2
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
# Source0-md5:	62fb998da33b93cd9910c4a819e9b874
URL:		http://www.pldaniels.com/ripmime/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com/). ripMIME has
been written with one sole purpose in mind, to extract the attached
files out of a MIME encoded email package.

%description -l pl.UTF-8
ripMIME to mały program stworzony jako część komercyjnego Xamime
(http://www.xamime.com/). ripMIME służy do wyciągania plików
dołączonych do wiadomości kodowanych MIME.

%prep
%setup  -q
%{__sed} -i -e '6s,ripMIME,ripmime,g' ripmime.1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -I.."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install ripmime $RPM_BUILD_ROOT%{_bindir}
install ripmime.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG INSTALL LICENSE README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/ripmime.1*
