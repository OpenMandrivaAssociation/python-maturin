Name:           python-maturin
Version:        0.13.2
Release:        1
Summary:        Rust/Python Interoperability
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
Source0:        https://files.pythonhosted.org/packages/source/m/maturin/maturin-%{version}.tar.gz
# Make sure to update vendor. Cd to source then run in terminal "cargo vendor". After downloading all cargo crates, compress is as tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tomli)
BuildRequires:  python3dist(wheel)

Requires:       python-tomli

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

This project is a zero-configuration replacement for
setuptools-rust milksnake. It supports building wheels for Python
3.6+, can upload them to PyPI and has basic PyPy support.

%prep
%autosetup -a1 -n maturin-%{version}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%py_build
#mkdir wheels
#pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
%py_install
#pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

%files
%{_bindir}/maturin
%{python_sitearch}/maturin-%{version}-py*.*.egg-info
%{python_sitearch}/maturin/
