Name:		texlive-recycle
Version:	15878
Release:	2
Summary:	A font providing the "recyclable" logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/recycle
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This single-character font is provided as MetaFont source, and
in Adobe Type 1 format. It is accompanied by a trivial LaTeX
package to use the logo at various sizes.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/recycle
%{_texmfdistdir}/fonts/source/public/recycle
%{_texmfdistdir}/fonts/tfm/public/recycle
%{_texmfdistdir}/fonts/type1/public/recycle
%{_texmfdistdir}/tex/latex/recycle
%doc %{_texmfdistdir}/doc/fonts/recycle

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
