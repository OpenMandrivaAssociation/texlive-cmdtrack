Name:		texlive-cmdtrack
Version:	28910
Release:	1
Summary:	Check used commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmdtrack
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmdtrack.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package keeps track of whether a command defined in a
document preamble is actually used somewhere in the document.
After the package is loaded in the preamble of a document, all
\newcommand (and similar command definitions) between that
point and the beginning of the document will be marked for
logging. At the end of the document a report of command usage
will be printed in the TeX log, for example: - "mdash was used
on line 25"; - "ndash was never used".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cmdtrack/cmdtrack.sty
%doc %{_texmfdistdir}/doc/latex/cmdtrack/Makefile
%doc %{_texmfdistdir}/doc/latex/cmdtrack/README
%doc %{_texmfdistdir}/doc/latex/cmdtrack/cmdtrack.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cmdtrack/cmdtrack.dtx
%doc %{_texmfdistdir}/source/latex/cmdtrack/cmdtrack.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
