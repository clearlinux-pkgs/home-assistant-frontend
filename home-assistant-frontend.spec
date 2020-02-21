#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant-frontend
Version  : 20200220.1
Release  : 79
URL      : https://files.pythonhosted.org/packages/2c/79/61d989fb2d326232edd5efc7a6b755a08e3517a6471e21485fa7fcbaa55c/home-assistant-frontend-20200220.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2c/79/61d989fb2d326232edd5efc7a6b755a08e3517a6471e21485fa7fcbaa55c/home-assistant-frontend-20200220.1.tar.gz
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
%setup -q -n home-assistant-frontend-20200220.1
cd %{_builddir}/home-assistant-frontend-20200220.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582300615
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
cp %{_builddir}/home-assistant-frontend-20200220.1/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/app.df1d19bb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/59e2b1ab14f759f2cace1268a4a922545c4f821b
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.01a54f7bab25b7fa6059.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.07a1407d761f032f7bf8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.07ca0f12ba580a4907b8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.0a51db90259d73eb2d04.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.0bcf9c0a41d289315266.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.0f393159ca0a1c56cd52.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.15d33674605086bbbcc6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.173b4f708414503f7c08.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.1b657c111602849feace.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.26a1649d6cb34f578671.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.2a94cb2d3b26468c1b45.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.2b9b9730d61dbdcf9460.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.2d07991f816af6d777de.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.326af8772646ce3e5ed5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.329a2913c983e406ed0e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.3776abac7049898a6933.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.39665758f4daeee04c5a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.3bd455fb196ad552ec63.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.3d85ab2ab07dcec2d03d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.439a5fefaf2a3a7639fa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.4d2f1ca3349dbbf681c1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.4f3698d9bd6f8a7d9e98.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.51a584335d2dd20b7cd6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.5c62a61d71a7165fd944.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.62a209ac789c5840f24f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/971648e1257541060d2781192eadbbd4b25bbd4f
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.691200da91e06fc619c0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.7171f6cbfb12b3fea0ad.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.7365068103dbecb54635.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.797cda663d5738b4ca98.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.7b46c3f13d5b5897bd00.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.7cd3400ba4e95fdaf086.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.7f7530bb7626af4cf4a8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.8550a327703f964198d1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.86ac8a4da79bc216dcff.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.8e45c94c75b0886e8f06.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.8ea041fe22fdc065e4e6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.92760673b013bc880a34.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.96a5a2402389ca9959f5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.983d4a4b7df284ab7d2e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.9c2899c279dab1557ad8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.9d705358e2abc5fa4635.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.a01e8bf94bafb864b056.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.a18e61444b68baae7fc9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.a24d01f7626d7c5f6767.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.a8022d2bfe088134189a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.ad78f6e2ea62c4b34703.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.b50dc1c69c030695be70.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.d3e2804071c8376de102.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.d4148e7801b8a2aedfbc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.d6fcc122d272c3325b41.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.db3a91576a78f426a3d5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.dc185a95caf3e2da6a54.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.e952adcdf935d45bcef1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.e99b8b7b2af4d84adb03.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.e9e17b891df6a3cccbb5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.ec5a370798cdde6a3b41.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.efc21f6c53c2a90a1244.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.f0df8a24376d58c23ad9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.f39d05a69b872326175e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.f3fdd28ff4b4d4c484db.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.f646bd9060ca636b7e03.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_es5/chunk.facec4b99de7608e9463.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.05fcccf0db2edd97455c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.0cccc905609bcb09a6b5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.10c136c33564dea1caf2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.12bb22d9e81cb6e7438e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.182bae22705172446ca4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.1bf9dd01e404e5143aea.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.1e183d0a329574ec5d34.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.203c80a7d190fc401b5c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.29ef14f6e442525451ae.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.2a242b02e4994b6a47d0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.2de20400eca2237a78d0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.2e68b483e0d34e4cfc00.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.3128fb9aa28f54d16723.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.331c722eb1e74817ac60.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.4200ae378686cf447a36.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.4279e00b7c220ad0e266.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.4a438e7938ea6b9a7e87.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.4e38a56ad4785fb45b92.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.550677aef9b1b934ce13.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.57de33de0eb272105369.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.5a89503b1cb06438ead3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.5ac5015f59aaf5c8a3ca.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.5d353fee11b51661a462.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.658affa1f14cee7ebbe8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.6842c981dcde97b52bba.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.699253e0d0bdb2c5f92d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.69d93693f07db6a324a7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.6a53137bd1055871a4ad.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.6c5e2c0b67d6b542e3f5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.6d85a38f2891f462c1d4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.6f2e9737547048c5d713.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.7389a365a02c6e14d817.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.751fa4e0b10af0fda00e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.7543210e3035220ac7e2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.75efc01c4c349d44967e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.78513cd23575843a4460.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.7d09ac099ebb4f8c5320.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.82147ad952ebab60945b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.868cf79995571d1afd5e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.95ad51205bab4d35a2d8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.9d581a5b5e8640244aa3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.a1dc2e0a6f154b401066.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.a733c6553b3e6f966ef1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.a9eb1554840b816a494f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.a9ec1fa8165bfc9a0cdd.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.abcfb4fd297cb358d4d9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.ad05945192242652ed2a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.b1ccb53a5aa790a9211d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.c009ffe83f4b5af5b1d7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.c439ffde0feb36abd69f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.c46693ce9268ed398ecc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.c9ffdbb98b0e49288279.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.cdbbfaeb41bccb79fbbc.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.d6848f42c842ed2a6bac.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.d9e1ada2b97a40d3c67d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.de9b83c7d3c3c4e7f428.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.e4e3c422474f945be77c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.e7cec089c913899c4691.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.ea56bf67abae091ba603.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.ee9091137e9ea98da65b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.f5a6f1bf3db6145486bd.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.f61a1d3057b8e52e80c4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.fdd792b1b0650a1dabff.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.feb719a4d322ba8e72a3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200220.1/hass_frontend/frontend_latest/chunk.fedc3a21ab5e446d7f42.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
/usr/share/package-licenses/home-assistant-frontend/59e2b1ab14f759f2cace1268a4a922545c4f821b
/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
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
