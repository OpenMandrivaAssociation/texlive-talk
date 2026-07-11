%global tl_name talk
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	A LaTeX class for presentations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/talk
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/talk.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The talk document class allows you to create slides for screen
presentations or printing on transparencies. It also allows you to print
personal notes for your talk. You can create overlays and display
structure information (current section / subsection, table of contents)
on your slides. The main feature that distinguishes talk from other
presentation classes like beamer or prosper is that it allows the user
to define an arbitrary number of slide styles and switch between these
styles from slide to slide. This way the slide layout can be adapted to
the slide content. For example, the title or contents page of a talk can
be given a slightly different layout than the other slides. The talk
class makes no restrictions on the slide design whatsoever. The entire
look and feel of the presentation can be defined by the user. The style
definitions should be put in a separate sty file. Currently the package
comes with two sets of pre-defined slide styles (talk-simple.sty and
talk-sidebars.sty). Contributions from people who are artistically more
gifted than the author are more than welcome!

