Name:		texlive-talk
Version:	42428
Release:	2
Summary:	A LaTeX class for presentations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/talk
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The talk document class allows you to create slides for screen
presentations or printing on transparencies. It also allows you
to print personal notes for your talk. You can create overlays
and display structure information (current section /
subsection, table of contents) on your slides. The main feature
that distinguishes talk from other presentation classes like
beamer or prosper is that it allows the user to define an
arbitrary number of slide styles and switch between these
styles from slide to slide. This way the slide layout can be
adapted to the slide content. For example, the title or
contents page of a talk can be given a slightly different
layout than the other slides. The talk class makes no
restrictions on the slide design whatsoever. The entire look
and feel of the presentation can be defined by the user. The
style definitions should be put in a separate sty file.
Currently the package comes with only one set of pre-defined
slide styles (greybars.sty). Contributions from people who are
artistically more gifted than the author are more than
welcome!.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/talk/sidebars.sty
%{_texmfdistdir}/tex/latex/talk/talk.cls
%doc %{_texmfdistdir}/doc/latex/talk/README
%doc %{_texmfdistdir}/doc/latex/talk/example.tex
%doc %{_texmfdistdir}/doc/latex/talk/talkdoc.pdf
%doc %{_texmfdistdir}/doc/latex/talk/talkdoc.tex
#- source
%doc %{_texmfdistdir}/source/latex/talk/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
