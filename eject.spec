Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datentr�ger aus und steuert Auswurf
Summary(es):	Expulsa medias expulsables y controla autoexpulsi�n
Summary(fr):	�jecte un support �jectable et commande l'�jection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(pt_BR):	Ejeta m�dias ejet�veis e controla auto-eje��o
Summary(ru):	���������, ������������� ������� �������� �� �����������
Summary(tr):	Eject yetene�i olan ayg�tlar� kontrol eder
Summary(uk):	��������, �� �������դ �ͦ�Φ ��Ӧ� � ����������ަ�
Name:		eject
Version:	2.0.13
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.pobox.com/~tranter/%{name}-%{version}.tar.gz
# Source0-md5: b796ad77beb4e7bdd08d6149701ab778
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5: dd66d948c94fe0f0b4483c51873e6e20
Source2:	%{name}-pl.po
Patch0:		%{name}-gettext.patch
URL:		http://eject.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm erm�glicht auf SPARC-Rechnern das Auswerfen von
Datentr�gern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l es
Este programa permite al usuario expulsar media que es autoexpulsable
como CD-ROMs, drives Jaz y Zip y floppy drives en m�quinas SPARC.

%description -l fr
Ce programme permet � l'utilisateur d'�jecter un support auto�jectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl
Program do automatycznego otwierania szuflad w urz�dzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l pt_BR
Este programa permite ao usu�rio ejetar m�dia que � auto-ejet�vel como
CD-ROMs, drives Jaz e Zip e floppy drives em m�quinas SPARC.

%description -l ru
��� ��������� ��������� ������������ ����������� ������� �������� ��
�����������, �������������� ����������� eject (����� ��� CD-ROM�,
Iomega Jaz ��� Zip �����, ������-����� �� SPARC-�������). Eject �����
����� ��������� ���������� CD ����������.

%description -l tr
Bu yaz�l�m paketi ile kullan�c�ya 'eject' yetene�i olan ayg�tlar�
kontrol olana�� verilmektedir. Bu yetene�i olan ayg�tlar aras�nda
CD-ROM'lar, Zip s�r�c�leri ve baz� disket s�r�c�leri yer al�r.

%description -l uk
�� �������� ������Ѥ �����������צ ������������ �ͦ�Φ ��Ӧ� �
����������ަ�, �� Ц��������� ���������� eject (��˦ �� CD-ROM�,
Iomega Jaz �� Zip �����, ���Ц-����� �� SPARC-�������). Eject ����
����� ��������� ������� CD ����������

%prep
%setup -q
%patch0 -p1

# standardize locale names
mv -f po/{de_DE,de}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{ja_JP.eucJP,ja}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

cp %{SOURCE2} po/pl.po

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING PROBLEMS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
