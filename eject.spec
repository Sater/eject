Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datentr�ger aus und steuert Auswurf 
Summary(fr):	�jecte un support �jectable et commande l'�jection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(tr):	Eject yetene�i olan ayg�tlar� kontrol eder
Name:		eject
Version:	2.0.12
Release:	2
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	http://members.home.net/jefftranter/%{name}-%{version}.tar.gz
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-DESTDIR_fix.patch
URL:		http://sourceforge.net/projects/eject/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm erm�glicht auf SPARC-Rechnern das Auswerfen von
Datentr�gern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l fr
Ce programme permet � l'utilisateur d'�jecter un support auto�jectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl
Program do automatycznego otwierania szuflad w urz�dzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l tr
Bu yaz�l�m paketi ile kullan�c�ya 'eject' yetene�i olan ayg�tlar�
kontrol olana�� verilmektedir. Bu yetene�i olan ayg�tlar aras�nda
CD-ROM'lar, Zip s�r�c�leri ve baz� disket s�r�c�leri yer al�r.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf AUTHORS ChangeLog NEWS PORTING PROBLEMS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
