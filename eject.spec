Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datentr�ger aus und steuert Auswurf 
Summary(fr):	�jecte un support �jectable et commande l'�jection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(tr):	Eject yetene�i olan ayg�tlar� kontrol eder
Name:		eject
Version:	2.0.2
Release:	4
License:	GPL
Group:		Utilities/System
Group(pl):	Narz�dzia/System
Source0:	http://metalab.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz
URL:		http://www.pobox.com/~tranter/eject.html
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

%build
make CFLAGS="-Wall $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s eject $RPM_BUILD_ROOT%{_bindir}/eject
install eject.1 $RPM_BUILD_ROOT%{_mandir}/man1/eject.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README ChangeLog
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/eject
%{_mandir}/man1/*
