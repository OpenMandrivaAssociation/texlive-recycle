# revision 15878
# category Package
# catalog-ctan /fonts/recycle
# catalog-date 2009-11-10 00:30:52 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-recycle
Version:	20091110
Release:	1
Summary:	A font providing the "recyclable" logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/recycle
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This single-character font is provided as MetaFont source, and
in Adobe Type 1 format. It is accompanied by a trivial LaTeX
package to use the logo at various sizes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/recycle/recycle.map
%{_texmfdistdir}/fonts/source/public/recycle/recycle.mf
%{_texmfdistdir}/fonts/tfm/public/recycle/recycle.tfm
%{_texmfdistdir}/fonts/type1/public/recycle/recycle.pfb
%{_texmfdistdir}/tex/latex/recycle/recycle.sty
%doc %{_texmfdistdir}/doc/fonts/recycle/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
