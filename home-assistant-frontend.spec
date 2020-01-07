#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant-frontend
Version  : 20191204.1
Release  : 68
URL      : https://files.pythonhosted.org/packages/4c/48/72b2f05eaea5d3c48e60a5087e73f5bf2f364eeeeeb44407e060b026bd00/home-assistant-frontend-20191204.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4c/48/72b2f05eaea5d3c48e60a5087e73f5bf2f364eeeeeb44407e060b026bd00/home-assistant-frontend-20191204.1.tar.gz
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
%setup -q -n home-assistant-frontend-20191204.1
cd %{_builddir}/home-assistant-frontend-20191204.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576189476
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
cp %{_builddir}/home-assistant-frontend-20191204.1/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.00d5eb387a8c2652b63c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.027f6e74dab1eb0095eb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.04472b20088a5b360d6e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.04cfacf36445f29930e0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.1ecf25df0d75fe008ecb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8edad7b250a5e6c300b5f8ea98d12beece4a886e
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.22a19eee220063cb667e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.266e4fdc0c231dd85907.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.2e736d4fa69c067a6543.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.2ea6c3b6d1175058db20.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.342f6906c213ca7d5bd4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.3a7a88d3a92da9cc4690.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.3ade6e7407ca41d5c21a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/56c1e62b2fb6d387e80c49b67e2ea5a5665cdc48
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.3fa16298e14b57fcb533.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.414fd2a0e00ddbe9005c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.42accceb9e2ef423f109.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.4454bdc0a95198d29758.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.4b37d125df833456c452.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.4efeeeb76c2989002b08.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.51d3cdd5511f7edbc2c5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.52a01f1993b7e431a6fe.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f8f68c0dc1713624a9d38c5484b464f62d190432
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.575c857cae4d06119976.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.5b46e1ca6ba614d8a23b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/6197d96aea2cd2173c7996ec09eb682c05e42b12
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.5cb092d2d9d9e67e70c3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.6122d120e76dc4ca7f50.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.61335dba9f730ce60049.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.61dace9bfef8563f305f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/ede281ca359aa558c7cc1f9cda6ed8d4155f916b
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.627c9bf02615be1f1a4e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.7727910e3a6f4aaa7093.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.7826b69d25d4828765d8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.793c06c68b7d88c09102.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.796e49557bd51ded65f7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.79775ea32ee5ea96e200.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.7e8d77f00f11344e5ddc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.7e992902d6b885ec0498.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.7f4edb586005c80ea898.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.82df314f99f81d0a6ee9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.8325a1effd053e889c9d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.837545aa8a43450a7d2a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.902a43d411b73707a0a7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.90ee75916d4bdbb909f6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.911ab5608bc81bf9867c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.91c22aa3c3bd8bcdd33c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.92222717185dbf6fc804.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.93521227bc38b3387645.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/06c536a5e7dfab19a03483cc868e9a92b3342ade
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.9980d83ad0306404370c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.9a1ced8042b7ccec2e8c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.9b519cebca350541dc80.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.a0ba013bd05949db417e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.a8f2d72bf5633f8351df.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.af52a52e1695ca91c052.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.b149faa63bab54d76b2d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.b28b160835ec37205545.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.c0a2f091982b3815a876.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.c315d53577ca3287aa16.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.c771e91b861244f59f5d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.cda425e17f15ea352a4e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.cf0cd5ab30a4bb89f7e3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.d1aa9a6c3b4daf2266b1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.d28452a141f010938a4c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.d2e072c01212c8d3485b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.d74ba3e1f0ea265b156c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.db7abe80e755b91409ca.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.e59319b96461f618ae09.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.e5c7c0d3d2ba7933c71a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.f2e82eb8626cde36ca87.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.f368507edd95c54dbfee.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.f37fb9a7a5ea04356312.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.f8cd74d9230fafa03355.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_es5/chunk.fa66c902d3afb6c2faea.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.01170beed3c6886c6ac5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.09796edd532fb595c4fa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.1bbe08763020e81c3e9e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.1f861ce2d592b59b3358.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.21e48929d9d69c5b505b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.24908ab7e936cc91d2a6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.2828810a76397408a559.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.2973c96ff038f01e1486.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.2c7743f073008b6d76c4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.2da1c2f71dc0b6131553.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.2fe77a8de2130f8fe4f1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.3118bed04854da711f05.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.34cbf7b6513e662ede40.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.3b7b5ebf548ef400ade0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.3c573089a5e1b7ec52fd.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.3d3f35dbc61d6f0979af.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.3e88a20f003bca52611f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.401877e437f7a3ad6f21.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.44cf81e3227a179cff84.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/435d3db816faac614d5584fc8df6d09ea9828b3a
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.4f1ac00401be88484ad5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/ede281ca359aa558c7cc1f9cda6ed8d4155f916b
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.505af2480450d3574044.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.50fbc90ce70a2ff15c52.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.57b8d3756e66233d1962.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.5807b9ed2d9a0f582a67.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.585dbf4b5c6b957b4b7e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.59e9c22af29a24e4837a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.5c52f308413abd4cb697.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.5c8921083c67f99e03bd.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.60ffd40b0e74d0503287.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.63d4f78d800a9969c521.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.66f6ca5c4796011d32df.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.69c45cc24afe37d063e4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/6197d96aea2cd2173c7996ec09eb682c05e42b12
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.6e5a8ef13c56c7ed16e0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.6ed459d5fce0cec7ed6a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.793a325b788d346f0db4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.7ac8e3f05b2fc5293eca.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.822dc6b6d40d76a54f95.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.82858443d26cf004db28.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.83392cf361f32f9e9886.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.83927d9fc7237bac47ad.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.83f51b2c2b22e9187549.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.84e099252cf1a2b074d0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.894aa89399b934bc2de1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.8f8c84f936bab91afe6e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.928785e5cb59a2f06bfe.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.95fb2026c2d2a5463799.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.96fefc38ea78a095447e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.99ac191c43bf83261cc0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.a08feae949c54f290b96.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.a0ffb641e05b2edd17c5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.a712594652212dff4757.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.a96dc1d031c892c4ff2e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.ac31550d3588efe8516a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.acdcd55daf593b5188e0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.aed2d072ed573744f666.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.b18293e58312a9999fed.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.b313c449771c6a0599e0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.bbd9440cbaa86f40d240.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.bdf30f156b0fd794b3cf.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.c054b58d9de566a00334.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.d305b87dbc0bd39e84cc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.d4c0a9c97a9726fab1e1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.dd76b3c674c6b898c51f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.e0f50d87c7912d7b681e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.e3f6aac31293ee033409.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.e6353d8e2b359920e818.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/126c94bc7bdb0095a12ad56ce6975fc7aa445ad5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.ee389ea2e0843f0f930a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.f1aa6222227159bb020f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.f4ca09a72fb301832701.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/06c536a5e7dfab19a03483cc868e9a92b3342ade
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.f4cafd1f701afa07b955.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.f53bd0137fe2810d5f1e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.f6937ffa40664c45d6d9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.fa2168fa5093ead0280f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.fa97b4a99c36f6be73ab.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.fae7355b44d2cbd568ae.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20191204.1/hass_frontend/frontend_latest/chunk.fb7a4413f6c20fd57f63.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
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
/usr/share/package-licenses/home-assistant-frontend/56c1e62b2fb6d387e80c49b67e2ea5a5665cdc48
/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
/usr/share/package-licenses/home-assistant-frontend/6197d96aea2cd2173c7996ec09eb682c05e42b12
/usr/share/package-licenses/home-assistant-frontend/61a077f273a486173670c71ba8deef1cf96ed6bc
/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
/usr/share/package-licenses/home-assistant-frontend/8edad7b250a5e6c300b5f8ea98d12beece4a886e
/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
/usr/share/package-licenses/home-assistant-frontend/ede281ca359aa558c7cc1f9cda6ed8d4155f916b
/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
/usr/share/package-licenses/home-assistant-frontend/f8f68c0dc1713624a9d38c5484b464f62d190432
/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
