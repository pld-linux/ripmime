Summary:	ripMIME extract the attached files out of a MIME encoded email package
Summary(pl):	NarzÍdzie wyci±gaj±ce za≥±czniki z wiadomo∂ci kodowanych MIME
Name:		ripmime	
Version:	1.2.12
Release:	1
License:	BSD
Group:		Networking/Utilities
Group(cs):	SÌªovÈ/Utility
Group(da):	NetvÊrks/VÊrkt¯j
Group(de):	Netzwerkwesen/Dienstprogramme
Group(es):	Red/Utilitarios
Group(fr):	RÈseau/Utilitaires
Group(is):	Net/TÛl
Group(it):	Rete/Utility
Group(no):	Nettverks/Verkt¯y
Group(pl):	Sieciowe/NarzÍdzia
Group(pt_BR):	Rede/Utilit·rios
Group(pt):	Rede/Utilidades
Group(ru):	Û≈‘ÿ/ı‘…Ã…‘Ÿ
Group(sl):	Omreæni/PripomoËki
Group(sv):	N‰tverk/Verktyg
Group(uk):	Ì≈“≈÷¡/ı‘…Ã¶‘…
Source0:	http://www.pldaniels.com/ripmime/%{name}-%{version}.tar.gz
URL:		http://www.pldaniels.com/ripmime/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ripMIME is a small program which has been developed as part of the
commercial Xamime development (http://www.xamime.com/). ripMIME has
been written with one sole purpose in mind, to extract the attached
files out of a MIME encoded email package.

%description -l pl
ripMIME to ma≥y program stworzony jako czÍ∂Ê komercyjnego Xamime
(http://www.xamime.com/). ripMIME s≥uøy do wyci±gania plikÛw
do≥±czonych do wiadomo∂ci kodowanych MIME.

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
