Summary:	ripMIME extract the attached files out of a MIME encoded email package
Summary(pl):	Narzêdzie wyci±gaj±ce za³±czniki z wiadomo¶ci kodowanych MIME
Name:		ripmime
Version:	1.2.16.7
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
URL:		http://www.pldaniels.com/ripmime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com/). ripMIME has
been written with one sole purpose in mind, to extract the attached
files out of a MIME encoded email package.

%description -l pl
ripMIME to ma³y program stworzony jako czê¶æ komercyjnego Xamime
(http://www.xamime.com/). ripMIME s³u¿y do wyci±gania plików
do³±czonych do wiadomo¶ci kodowanych MIME.

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
%doc *.gz
%attr(755,root,root) %{_bindir}/*
