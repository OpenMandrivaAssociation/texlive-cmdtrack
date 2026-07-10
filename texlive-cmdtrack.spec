%global tl_name cmdtrack
%global tl_revision 78101

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Check used commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cmdtrack
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package keeps track of whether a command defined in a document
preamble is actually used somewhere in the document. After the package
is loaded in the preamble of a document, all \newcommand (and similar
command definitions) between that point and the beginning of the
document will be marked for logging. At the end of the document a report
of command usage will be printed in the TeX log, for example: "mdash was
used on line 25"; "ndash was never used".

