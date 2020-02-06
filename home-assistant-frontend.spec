#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant-frontend
Version  : 20200130.2
Release  : 75
URL      : https://files.pythonhosted.org/packages/d9/99/e8432fc1b83284d470ed86f53ccc0b7c06890416ae725b6b63e16f1767f2/home-assistant-frontend-20200130.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/99/e8432fc1b83284d470ed86f53ccc0b7c06890416ae725b6b63e16f1767f2/home-assistant-frontend-20200130.2.tar.gz
Summary  : The Home Assistant frontend
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: home-assistant-frontend-license = %{version}-%{release}
Requires: home-assistant-frontend-python = %{version}-%{release}
Requires: home-assistant-frontend-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# Home Assistant Polymer [![Build Status](https://travis-ci.org/home-assistant/home-assistant-polymer.svg?branch=master)](https://travis-ci.org/home-assistant/home-assistant-polymer)

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

%description python3
python3 components for the home-assistant-frontend package.


%prep
%setup -q -n home-assistant-frontend-20200130.2
cd %{_builddir}/home-assistant-frontend-20200130.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581013283
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/home-assistant-frontend
cp %{_builddir}/home-assistant-frontend-20200130.2/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.01a3079183c495d04a71.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.041de7269988b9b9c4ce.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.06ccf0eb0d12183e8eaa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.12d735747c223d0d8b20.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1324210c9681e4477ff6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1341d9a142b7339a6f96.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.143959b5d59a3a27ad7f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1663ff429039d4034fa5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1a24201fc2f963de8da4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1abbea28bef2c7d51897.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1cb5f57b22100d00c64d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.1f0ffc230a3bd4921dfd.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.2f330f9f896fd3930de7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.30752d647567227f3542.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.3d804923bcfb4e9a7271.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.410f73ee0d01d7f64937.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.417f64df114ec4c70eae.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.44d791df1db4ed33c1e1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.4552ed03fba6f4d72756.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.49528f2d995384970d18.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.4ba85d24515be79a4b3b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.51424132d55e60027a41.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.5343ae27d9a7a71d0fa2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.57caf0349bfbedf65aa3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.6199c843893b490bc09e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.64fa3709cded240da2a9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.67db7fc43e520110a4b0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.693331f275707c4fed29.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.6a03d58d61f8200ec9ff.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.781c87e778ed34f07451.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.7d76d8599c77fb46da4f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.7ede91abbc3f2a5b73b1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.82081e17d48f05447165.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.835151ac5b6ef8ce4d17.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.8552b7560e00a39e2208.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.894efe111c6f707650c3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.8a89cbd4ed58a1afa202.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/971648e1257541060d2781192eadbbd4b25bbd4f
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.8b6d68e56605932853e6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.8e0a92c3f684b2e4f655.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.95fb10bf24528445f9f4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.99b42ced621bd1877f6b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.9fafe053e2975cd88b06.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.a1fefddac7e8db457e70.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.a4b61b49b6a8572ee3b2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.aba177a9df58d68eb5c9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.b0a94c173c8727e08fc4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.b50fbb94142626b5568c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.c39de3235856312c0319.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.c4597d555908c93dc6f2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.cb6f09fa0cc5e062ee93.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.cb9f75e5dc3e1db8df9f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.d7743ddb444f304d53cc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.dc314d189861a35120cc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.dcc1dc90b745be222503.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.dfed0422dd11e6e891a1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.e246b3feab6b35eebb85.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.e5fdb161fe814488b0e4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.e9b1e0c5b28ca9645c1f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.ed9caa63536f3ad358ed.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.ee62ce8aa73c14d79f62.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.f22ddf2307751aae9df9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8edad7b250a5e6c300b5f8ea98d12beece4a886e
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.f48c1de547efaecaf6f8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.f5be89d7f34691bf8963.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.f7de466d291fd88b8d4b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/06c536a5e7dfab19a03483cc868e9a92b3342ade
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.f9e4e26081f2f1fd8d61.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.fd35e17a058ae36e8689.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.fd6ba635d95fdebd4dc0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.fea26fa1ddb6230f5858.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_es5/chunk.ff57f2f477a8f19c05bb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.00432fbc3347d829f2b7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.0338158b8f5d5b3eb7ce.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.035c6e01be207e5c1141.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.092cc558764b2ba3fe94.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.0b3cce704254b01c383f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.0b56701a8f48531cebae.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.0bc72c40d26829a68536.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.0cd6fa2c99d65d85e4a9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.18529691b29db47e8afa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.1e0a3e338ab5f5cc52b1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.20f2329d6a9fcea206f3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.214224d0eee351fdac7a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.232e8e3f43c56c6be54c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.23b61b51d71b21a39282.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.2493af3aa631ac35701a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.25659d1a232ca90eb556.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.27aa6068fb2a08ca8a38.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.2865c173d1be1611bdce.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.291589b30f507eb2f07d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.2d6c1ad6fbfa6122109f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.2e4a70fc58fa44ff1411.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.3053b48855b962c2875a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.311c0f6c43a593b851bf.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.337c798b3120559a0604.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.392dc68f638a0619f5b9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.44c7b7826de1daacf132.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.46c13366bf204145764f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.5168f20e717854a58e9a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.52268ed4c9d120de5382.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.5332cfa7d7180d658940.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.56a573dad1b8e4d4b82e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.59585b065afea7a84e53.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.626667fbd2a92e391996.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.6509ae4d73557f35a1f3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.72693184a2371773fe63.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/06c536a5e7dfab19a03483cc868e9a92b3342ade
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.733c539ff3455add0d63.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.8522dcfb85ba688e88dc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.89f20f53a6e73a4d9364.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.8d32cf6b81f3174be430.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.9608c696bffe9cbc2d62.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.962a3980f5eea13f152d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.97fe276acb67430a66c8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.98deff9a9670843bc85f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.99b2a40a7c846af1c03a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.99cd1c19395c8c6edfbc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.abca5d12e7bedd63682d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.b600ffd394980d032c73.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.b8b2571539015eda8094.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.b9e40a58b9fedf8938e9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.bc8e3c98f6add7bf2e79.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.bcc2d05176d41935ae5c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.bda08a9d7578a21dcb4d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.be95415dcd69c1732ee4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.c34c4579616bd2cd2417.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.ced01f42cf60f05e7f6b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.cfc4770b472c941c0b45.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d0559bdb49093133c747.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d1c7579d22b4d25389a2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d1d96ba7aa8d71cd9e04.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d35fbecf92c9470d13bb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d52abc5367dac9eba9f5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.d5f1a475d505efe5ff18.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.dcf81e22416487f5c895.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.e124eaa404ffc9e02823.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.e4fd25166e0403d106a5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.e6fcf7c01a8100e8235b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.ecc716aa7cb7138b8080.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.eddbe37b1084a63f9caa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.f4ce3eb7622bd189cc9b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.fa5a9d3817d60be99b45.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.fe095fe5420e8e05e34f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/435d3db816faac614d5584fc8df6d09ea9828b3a
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.fee345d34cf482930d9e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200130.2/hass_frontend/frontend_latest/chunk.fffcd53d158d7c103115.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant-frontend/06c536a5e7dfab19a03483cc868e9a92b3342ade
/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
/usr/share/package-licenses/home-assistant-frontend/435d3db816faac614d5584fc8df6d09ea9828b3a
/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
/usr/share/package-licenses/home-assistant-frontend/8edad7b250a5e6c300b5f8ea98d12beece4a886e
/usr/share/package-licenses/home-assistant-frontend/971648e1257541060d2781192eadbbd4b25bbd4f
/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
