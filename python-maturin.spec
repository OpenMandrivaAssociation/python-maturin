# Rust sucks
%undefine _debugsource_packages

Name:           python-maturin
Version:        1.8.2
Release:        1
Summary:        Rust/Python Interoperability
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
Source0:        https://files.pythonhosted.org/packages/source/m/maturin/maturin-%{version}.tar.gz
# Make sure to update vendor. Cd to source then run in terminal "cargo vendor". After downloading all cargo crates, compress is as tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildSystem:	python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools-rust)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(tomli)
BuildRequires:  python%{pyver}dist(wheel)

Requires:       python-tomli

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

This project is a zero-configuration replacement for
setuptools-rust milksnake. It supports building wheels for Python
3.6+, can upload them to PyPI and has basic PyPy support.

%prep -a
tar xf %{S:1}
mkdir .cargo
cp %{SOURCE2} .cargo/config

%files
%{_bindir}/maturin
%{python_sitearch}/maturin-%{version}.dist-info
%{python_sitearch}/maturin/
