#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : home-assistant-frontend
Version  : 20200228.0
Release  : 84
URL      : https://files.pythonhosted.org/packages/63/2e/44bb894d1c0157805e9c4dffe73d925d6090754dcca1e6fed8ead9327d30/home-assistant-frontend-20200228.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/2e/44bb894d1c0157805e9c4dffe73d925d6090754dcca1e6fed8ead9327d30/home-assistant-frontend-20200228.0.tar.gz
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
Provides: pypi(home-assistant-frontend)

%description python3
python3 components for the home-assistant-frontend package.


%prep
%setup -q -n home-assistant-frontend-20200228.0
cd %{_builddir}/home-assistant-frontend-20200228.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583159167
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
cp %{_builddir}/home-assistant-frontend-20200228.0/LICENSE.md %{buildroot}/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/app.241c9e1a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/59e2b1ab14f759f2cace1268a4a922545c4f821b
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.010b117f66c02ee6a029.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.07828ae89498a50060c9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8edad7b250a5e6c300b5f8ea98d12beece4a886e
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.16cfdf98f540323e2bc9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.1c5f636c2d35943a9e13.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.1d6dcca7ca1158ff51e9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.1d9a656f10ff34975632.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.21e0c5e3b994d495c753.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.2ab4da1927255e61b741.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.2bc07e69995e75a75d3b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.2cc1eaa75b26c46114f3.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.2d92a8cdbffa3960826e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.3289e261741ed6f4cf08.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.33faa3564fad7d768e38.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.34a8cacc4f9d408b625f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.34fc70a6095d5bd378a6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.3a2b9d5ca7affbadb686.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.3a974346b4d378509984.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.4680608d4e5ce334d62e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.4b771254b7d2f3a434e8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.4bccc9ce9e7e99dc682d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.4d49fcb2e438ff04b09f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.518ea606033835f890a4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.535700180ff3d1fb6168.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.5fe654e90bbda0366335.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.670895ee5780076783ae.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.6954e1b385738188a287.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.6cefc0446dbac4c76089.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.74bb38ddba6002dbcfa2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.7c2bb9018d6602cf673d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.80aa1032b968e528c4fe.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.836794512151c42c7e68.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.870a56f9392f46717da9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.8ad058056bc1dded8ec2.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.8e3b8c79da2458a819ed.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.96b133ea5203a62d18de.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.97870bca6c512029f8ad.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.9b1d1c35c2dd35676282.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.9b92c104be08d3211332.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.9d67313f59497ca12080.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.a375846a5bc0a368a315.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.aa42f9e2fcb4eafdd1e8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.ad268f9787b21789c441.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.afbe5fefcdd6a8ec2dc1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c02565b57e71ee492618.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c033f353818bec8de74c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c22e07cf3ba0cbe71c0f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c2b8aeaa5938110e1bab.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c699f3df9c0bbedd5576.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.c726790cd97bbb011d29.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.cc9ff84bc1372d9224b6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.d24824f9cefea3934369.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.dc9100bcb7d75d25026d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.dcba21efc3abe2f5e8eb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.de683378b4f146d9cfda.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.de79e7cfe1d1764d643a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.e3359b4b3a399f41ee4a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.e36dc86d4787d29016d8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/971648e1257541060d2781192eadbbd4b25bbd4f
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.e8ca030c79c2071dfc3e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f2db07abe8b5b70e28ee.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f309c200a930d621e66f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f55a567f6b46b8907415.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f5d26bfd43fb39d61211.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f65d1d70a6325d968cd1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.f7fa56b2a3d31d693e54.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.fbcbb6ed31cd2371355c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_es5/chunk.fc13264c471603fa1e5d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.02aa8f6013d12cfdd055.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.02b4a49a839a0772a6c8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.0d824e046741b7987ec7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.103f28904b4f1b98c32c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.13a14647cd12bc0f24f5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.145b14819ad48fb64882.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.1a792ced205378d39370.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.1b90d5d54f06f79a7824.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.1bc3cac989b68d0b6061.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.1e1344da11f756619862.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.2e71ec364817b0cce4e5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.2eae38ccea1cfff5a137.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.311a2433504d1fc16adb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.33540b3ec1e8f35f4f90.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.3ca82f2be2ec4224ecb5.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.445ff8ea8c8f6d152ab0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.474bee4efc6b3947c091.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.4fb2e6146edcf50c1bdb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.524d4f022d38c40afd8a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.52f17bdf77fb2d2ef113.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.546ab06e8644c6449045.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.5c4efff29a181f14e4d9.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.5d11c9f96b9ead5357db.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.5e96071ea8ca70b9037f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.5ee524b5a4b55cdf9a4f.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.61e9ca2973864328c82a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.62e227cea542a1349f60.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.7939b195f9f4009e5091.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/73da1be00ae0557c9de2692d87ec4c0c7641f977
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.7a69a0f547ce1e629b19.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/afe7358317fec873e1f291924462ba541c48a3ba
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.7dc5320b7914b9faa219.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.7e73efe156b30d70da5e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.82069da5e70998a91d89.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/c6f4a8a5feb0c5734c6d554ff7ab830d45ce5bed
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.82f547809d788706d1ed.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d0ba74c5f4aee0f52e27c777397602871dc5fbe6
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.8372813f31f44f965349.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.837b8d66c5c3e9fc95f0.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.867938a775d257487a97.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.8f946c9b048c360e9cec.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.9200a0e7baf15dd7b90e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.9411aa89c615bdfe6b89.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.974df82aec79a3c694c1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.9fd5ef7eff8d6164a1ac.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.a5a7a4fba14c56c8b949.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.a6028d898f3fc1f1c541.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.a66110bc594b285a400c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.a7f7dd6f36515fa60b1c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.a8035c4960434f9c5ddb.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.ab14915f44a75592538d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.ace9a9ebf550388693f6.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.b2bf4be6945569026a52.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.b4f1883530060db55939.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.b61ce547c7e328c90b05.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.bbc0ff99f1770148eaf4.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.c589f102d287918d9d5d.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.c6a31ef3a48dd4ff558e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.c896398916a5c0b79faa.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.c8ccd8e97d4dd0e23e8b.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.ca4199d2d229373ec664.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.cc2330c0f506bf922294.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.d1c83bde8d27dc780e0e.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/8073c6d2d854887d330e7de31f482689a72cc4e8
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.d655dea8cd461bcd46c8.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/f12d17e4713167bb7d7334d85cc466402bacff89
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.d772a0272dc7e08fbd06.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/dee177ec02ba127c8c3135834e0818073f2a7c81
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.dd165d49f89ab89be924.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.e2960137f8a009b032a7.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/435d3db816faac614d5584fc8df6d09ea9828b3a
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.eb97b93866cfceb87247.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.ec7f584b114016c26ee1.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.ecbefd035cbd5afff146.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.f4a623c51506ed65547a.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.f787d65df603d48aa530.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/d22c3bf160d8bfeccb275192b6e8154820b8a6c0
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.fa718baba77c74d93025.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
cp %{_builddir}/home-assistant-frontend-20200228.0/hass_frontend/frontend_latest/chunk.fdd510e5a9892ff16e5c.js.LICENSE %{buildroot}/usr/share/package-licenses/home-assistant-frontend/fb3724a403cfac8a891cbd6be583aaa458459643
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/home-assistant-frontend/0cfa3c69412acdd536367d69c99a38ba28dd01b0
/usr/share/package-licenses/home-assistant-frontend/30730e4fdc3053671b6092bda9684a55d3299eb5
/usr/share/package-licenses/home-assistant-frontend/435d3db816faac614d5584fc8df6d09ea9828b3a
/usr/share/package-licenses/home-assistant-frontend/4a606a34022a7ef2eab88e43148dd48547d3c017
/usr/share/package-licenses/home-assistant-frontend/555f11154ee482a232be08975eb01df15f68da90
/usr/share/package-licenses/home-assistant-frontend/5962264f761d86ef8f5705a25f3af3cd46ae4034
/usr/share/package-licenses/home-assistant-frontend/59e2b1ab14f759f2cace1268a4a922545c4f821b
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
