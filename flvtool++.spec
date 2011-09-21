# TODO
# - CC/CFLAGS from our build
Summary:	Tool for hinting and manipulation of Macromedia Flash Video files
Summary(pl.UTF-8):	Narzędzie do obróbki plików Macromedia Flash Video
Name:		flvtool++
Version:	1.2.1
Release:	1
License:	BSD
Group:		Applications/Multimedia
Source0:	http://mirror.facebook.net/facebook/flvtool++/%{name}-%{version}.tar.gz
# Source0-md5:	a8c4c578b4c6741a94ca6eb197a01fe1
URL:		http://rubyforge.org/projects/flvtool2/
BuildRequires:	boost >= 1.33.1
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FLVTool++ is a manipulation tool for Macromedia Flash Video files
(FLV). It can calculate a lot of meta data, insert an onMetaData tag,
cut FLV files, add cue points (onCuePoint), show the FLV structure and
print meta data information in XML or YAML.

%description -l pl.UTF-8
FLVTool++ to narzędzie do obróbki plików Macromedia Flash Video (FLV).
Potrafi obliczać większość metadanych, wstawiać znaczniki onMetaData,
ciąć pliki FLV, dodawać punkty wskazań (onCuePoint), pokazywać
strukturę FLV i wypisywać informacje o metadanych w formacie XML lub
YAML.

%prep
%setup -qc

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p flvtool++ $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README
%attr(755,root,root) %{_bindir}/flvtool++
