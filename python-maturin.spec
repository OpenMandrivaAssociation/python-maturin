# Rust sucks
%undefine _debugsource_template

Name:           python-maturin
Version:        1.13.1
Release:        1
Summary:        Rust/Python Interoperability
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
Source0:        https://files.pythonhosted.org/packages/source/m/maturin/maturin-%{version}.tar.gz
# Make sure to update vendor. Cd to source then run in terminal "cargo vendor". After downloading all cargo crates, compress is as tar.xz
Source1:        %{name}-%{version}-vendor.tar.xz

BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(tomli)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(puccinialin)
BuildRequires:	rust-packaging
BuildRequires:	cargo

Requires:	python%{pyver}dist(tomli)
Requires:	cargo

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings
as well as rust binaries as python packages.

This project is a zero-configuration replacement for
setuptools-rust milksnake. It supports building wheels for Python
3.6+, can upload them to PyPI and has basic PyPy support.

%prep -a
tar xf %{S:1}

%cargo_prep -v vendor
cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build -a
export CARGO_HOME=$PWD/.cargo
# sort out crate licenses
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%install -a
# install LICENSES.dependencies into dist-info/licenses
install -Dpm 0644 LICENSES.dependencies -t %{buildroot}%{python_sitearch}/maturin-%{version}.dist-info/licenses

%files
%{_bindir}/maturin
%{python_sitearch}/maturin
%{python_sitearch}/maturin-%{version}.dist-info
