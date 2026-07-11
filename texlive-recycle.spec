%global tl_name recycle
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A font providing the recyclable logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/recycle
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/recycle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This single-character font is provided as Metafont source, and in Adobe
Type 1 format. It is accompanied by a trivial LaTeX package to use the
logo at various sizes.

