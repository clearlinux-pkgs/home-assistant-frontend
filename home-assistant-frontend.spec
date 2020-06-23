#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant-frontend
Version  : 20200623.0
Release  : 126
URL      : https://files.pythonhosted.org/packages/8d/0f/b28406adc648f820dba457404db2da53d7075f3b69ea5cf8243bc0b7c312/home-assistant-frontend-20200623.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/0f/b28406adc648f820dba457404db2da53d7075f3b69ea5cf8243bc0b7c312/home-assistant-frontend-20200623.0.tar.gz
Summary  : The Home Assistant frontend
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: home-assistant-frontend-license = %{version}-%{release}
Requires: home-assistant-frontend-python = %{version}-%{release}
Requires: home-assistant-frontend-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Home Assistant Frontend
This is the repository for the official [Home Assistant](https://home-assistant.io) frontend.

%package license
Summary: license components for the home-assistant-frontend package.
Group: Default

%description license
license components for the home-assistant-frontend package.


%package python
Summary: python components for the home-assistant-frontend package.
Group: Default
Requires: home-assistant-frontend-python3 = %{version}-%{release}

%description python
python components for the home-assistant-frontend package.


%package python3
Summary: python3 components for the home-assistant-frontend package.
Group: Default
Requires: python3-core
Provides: pypi(home_assistant_frontend)

%description python3
python3 components for the home-assistant-frontend package.


%prep
%setup -q -n home-assistant-frontend-20200623.0
cd %{_builddir}/home-assistant-frontend-20200623.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592936508
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/home-assistant-frontend
cp %{_builddir}/home-assistant-frontend-20200623.0/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.032d05d6eab3467bb9af.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.04f80273f4a52ecb03dc.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.0a08d7300767fb1aa708.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.0cdf3ee13928181fa8c7.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.0de503e9d72e0a4be4ca.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.1a0257eb125b237ea90f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.2152c148d2c421ff2018.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.216321693a29eb45c3b3.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.250070b23a28ae874520.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.2a2f8a2d924f79115d1a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.32ded2da10052e0675ea.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.32fadfe2799ff8e5a5aa.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.33cc62516a8e55043f17.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.34bb19184895a1c51d40.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.36eeb0b1c531feec565e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.4318f644219659cb8f59.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.468fc6dafe5fdaa3d716.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.4a43dd96b6c09bdb6e56.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/3e99fe4555b051b96603c274976496d7262b4ca1
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.4cd666bb49c96dca2249.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.4ddf0c2b31d391ab38b2.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.50d521a8f2472e8cf464.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.52f4fcced217d791e27f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.56aeea0bdd8b19b83314.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.669015e31e0a92fdc585.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.67995bcfe4b5999b86e5.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.6a72ff841b0989621195.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.6a85ad3d4010e7c7d8a5.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.739f2ecb5e752c111045.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.84865d0791e14ac5268d.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.85b8cb77f6431818f39e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.876e1378c5ca86e69d4c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.8aeb21bab1f8b294b552.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.8f58c858034f6939dab6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/a1420ebb34855ee6ab1354615f4ece7d99864ad7
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.943fe7b959dbd3ee86f5.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.95dd5efe7707bb4dd421.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.9d71cc131eef2160744a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.a4dc968b7d0def47006a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.a5fc6649c0fe743e5dad.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.aa924c487221868f9f2e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.b0453de4da202bb1d895.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.b45c8b72335199d08fec.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.b711c8f3653bf1d73b02.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.ba2595a9465f2c8538b0.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.bc142fa7026fd2d7419b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.be515f4a78c47b35312c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.c1acc69fcceb77a07eb2.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.c2cd443d6ff32f22a4f4.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.c5d2a6b33d4660e1dc73.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.d17cf3a8fcf6a509ba3b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.d48cc35123883b3ee7fb.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.d4e8f5fbed78b874e734.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.d5528a1a7cd08323b030.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.e12beb51b2cbf0d6fcf6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.e1b874e1315972d5078e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.e44aaf1c1b296df3a5af.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.e909d2e7e94c2e9355a3.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.ea84c55ccdb6391fe3fe.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.eb7b2f9280053e500c4a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.f1459601ba215354fff1.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.f487a4a0c72ad9686151.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.f6656741b0eb9067ad79.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.f6be28d299ad9faed2ba.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.f8d55cfdb5c6bc0041ba.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.fec4a0ba5c0999cbe860.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_es5/chunk.ff3c5f74b8cbf13c774d.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.004dc663d6bb4d3682ef.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.0088ee0871e501d90e3b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.09a0f1d2892440f2f220.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.1065a29967a0053faac6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.12273bd78cabc984ae6e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.168a469b5736ea0731ac.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.16b81f9000e9b435386f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.1ce0ea54c4970a19937f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.239d4fa2c667ae308de0.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.256ad2f42d8dec7e1398.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.28caf11f7861a6dfe812.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.2f674b0f60a52770f357.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.30cdc3d650973c320e6d.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.368635e2b3dd1754c56f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.372c46e7fc04894dff4a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.3d5b3e2cf7202d231a56.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.410c79bd7879fef4866a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.471506854d305ef3d5cb.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4968a547ad6b535e4c70.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4a66f2465361b3d1d02c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4b4903383cb9687cdcf6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4bfaf7a6d6402ac1ead4.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4c8d284c22a509396e1c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.4f105b6d0d4784dd204d.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.512b4eb3eef6b9d4cb63.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.51866461e7ce1a29ac28.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.523915a4f99bd56bc1f2.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.54283593412d8189d382.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.54b8a7a75ab17bdf128c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.57a77138d4d8bf4f5813.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.582f5f2804334ddcdf16.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.597d780916747c005e4f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.59846a70a439e5e9c54a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.62b9e52ead05298e05b0.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/3e99fe4555b051b96603c274976496d7262b4ca1
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.66101cee67736eb5202b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.66b19a486f2627de33a6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.6a66bb47f0218df81d49.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.72f95b82e702ae0f9d7f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.74c1a153ac332899ccfe.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.76e7e9115d5846e095b6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.7b2c007eb8f3bc73bf48.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.7c1482682ac431ef9f4f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.7d9342c03c9da98d8969.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.847838a3365c9f2ec737.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.87164146ab23ff0501c2.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.883ba83b95dbb4933871.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.938c8f76bf9940fc1b69.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.97f7afa4bbb41462f14e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.9a7dd3b5fe93e058447b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.9c70144a9d9c8f08d246.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/a1420ebb34855ee6ab1354615f4ece7d99864ad7
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.9e104e412a64f5171177.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.a00beee46299bcd53154.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.a174335e9044019afa62.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.a22156751d8767b92fb6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.a520f48cd792136836f7.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/bc57faaf465e3d0f534c043605a17f39684ffeb0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.ab023bad3e0c4e87e815.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b0140a344dda0774bd8e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b0fcf1206c867d0407f7.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b2cc904974b1dc9ce908.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b4679da62e4bbd6ae64a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b491b9e03cba178f7ea0.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.b748688169291939e598.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.bdb8fb3a722b941f2a79.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.bdd101bde834834e7f99.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.c44e8ac08c2305ef7306.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.c92ee2f7778d6ccf1e1b.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.ca543903cc3cbd272e4e.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.cdec47c0913ac79048a8.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.ce374bdbe373c8df0b9d.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.d7468ea22b3068de248c.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.d9e4190262befa0c3c01.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.de9f382b6b341adc8444.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.df646f790b65bfbb9a2f.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.e7c10626f6655eb484a1.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.e8af36dc3064acb90488.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.e93638f43f41c0833051.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.ebb81d1e909930214b76.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.f39facafb4de3a4ca69a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200623.0/hass_frontend/frontend_latest/chunk.f4081eb099b5ac858def.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
/usr/share/package-licenses/home-assistant-frontend/3e99fe4555b051b96603c274976496d7262b4ca1
/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
/usr/share/package-licenses/home-assistant-frontend/87b094c5dfe6598f37df2222986b534be56e0786
/usr/share/package-licenses/home-assistant-frontend/a1420ebb34855ee6ab1354615f4ece7d99864ad7
/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
/usr/share/package-licenses/home-assistant-frontend/bc57faaf465e3d0f534c043605a17f39684ffeb0
/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
/usr/share/package-licenses/home-assistant-frontend/d0670e34b874eb9d45b70c95b52f99d3058579d2
/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
