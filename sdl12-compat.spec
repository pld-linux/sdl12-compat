#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
Summary:	SDL1.2 compat library (SDL2 to SDL1.2 compatibility wrapper)
Summary(pl.UTF-8):	Biblioteka SDL1.2 (warstwa kompatybilności SDL2 z SDL1.2)
Name:		sdl12-compat
Version:	1.2.60
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
Source0:	https://github.com/libsdl-org/sdl12-compat/archive/refs/tags/release-%{version}.tar.gz
# Source0-md5:	a539a4a3ceb3d09b7bf312d96210443c
URL:		https://www.libsdl.org/
BuildRequires:	SDL2-devel
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig
Obsoletes:	SDL <= 1.2.15
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SDL (Simple DirectMedia Layer) is a library that allows you portable,
low level access to a video framebuffer, audio output, mouse, and
keyboard. It can support both windowed and DGA modes of XFree86, and
it is designed to be portable - applications linked with SDL can also
be built on Win32 and BeOS.

sdl12-compat is a replacement for SDL.

It attempts to look, feel and behave identically. The difference is
that it just converts the SDL-1.2 function calls into their SDL2
equivalents.

%description -l pl.UTF-8
SDL (Simple DirectMedia Layer) jest biblioteką udostępniającą
przenośny, niskopoziomowy dostęp do bufora ramki video, wyjścia audio,
myszy oraz klawiatury. Może obsługiwać zarówno okienkowy tryb XFree86
jak i DGA. Konstruując ją miano na uwadze przenośność: aplikacje
konsolidowane z SDL można również budować w systemach Win32 i BeOS.


sdl12-compat to zamiennik SDL.

Stara się wyglądać i zachowywać identycznie. Różnica jest taka, że
zamienia wywołania funkcji SDL-1.2 na odpowiedniki z SDL2.

%package devel
Summary:	Header files for libusb-compat library
Summary(es.UTF-8):	Archivos de desarrollo de libusb-compat
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libusb-compat
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da libusb-compat
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel
Obsoletes:	SDL-devel <= 1.2

%description devel
This package contains header files and other resources you can use to
incorporate SDL-1.2 into applications.

%description devel -l es.UTF-8
Bibliotecas de desarrolo para sdl12-compat.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe i inne zasoby pozwalające
wykorzystywać API sdl12-compat we własnych aplikacjach.

%description devel -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para sdl12-compat.

%package static
Summary:	sdl12-compat static library
Summary(es.UTF-8):	Archivos de desarrollo de sdl12-compat - estatico
Summary(pl.UTF-8):	Statyczna biblioteka sdl12-compat
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento da sdl12-compat - biblioteca estática
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	SDL-static <= 1.2

%description static
This is package with static sdl12-compat library.

%description static -l es.UTF-8
Bibliotecas de desarrolo para linusb-compat - estatico.

%description static -l pl.UTF-8
Statyczna biblioteka sdl12-compat.

%description static -l pt_BR.UTF-8
Bibliotecas de desenvolvimento para sdl12-compat - estático.

%prep
%setup -q -n %{name}-release-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{?with_static_libs:-DSTATICDEVEL=ON} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libSDL-1.2.so.?
%attr(755,root,root) %{_libdir}/libSDL-1.2.so.1.2.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sdl-config
%{_includedir}/SDL
%{_libdir}/libSDL-1.2.so
%{_libdir}/libSDL.so
%{_libdir}/libSDLmain.a
%{_pkgconfigdir}/sdl12_compat.pc
%{_aclocaldir}/sdl.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL.a
%endif
