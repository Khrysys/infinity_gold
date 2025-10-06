# Contributing Guidelines

Thank you for your interest in contributing! This project follows the [CII Best Practices](https://bestpractices.coreinfrastructure.org/) and OpenSSF recommendations. Please read these guidelines before opening issues or submitting pull requests.

---

## How to Contribute

1. **Fork the repository** and create a feature branch from `master`.
2. **Make your changes** in code, documentation, or tests.
3. **Run the checks** locally:

   * Build and test with CMake/Conan.
   * Run Python tests with Poetry (`poetry run pytest`).
   * Ensure lint/formatting passes (`clang-format`, `clang-tidy`, `flake8`, etc.).
4. **Commit changes** with clear messages. Follow [Conventional Commits](https://www.conventionalcommits.org/) if possible.
5. **Open a Pull Request (PR)** targeting `master`.

All PRs require review from at least one maintainer and must pass CI.

---

## Code of Conduct

All contributors are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Development Setup

* **C++**: We use [Conan](https://conan.io) for dependencies and CMake for builds. See `conanfile.py` for required packages.
* **Python**: We use [Poetry](https://python-poetry.org/) for package/dependency management. The main Python package is in `bot/`.
* **Bindings**: Pybind11 code is in `bindings/python/`.

### Quick Start

```bash
# C++ build
conan install . --build=missing
conan build . --build=missing
ctest .

# Python dev setup
poetry install --with <GROUP>
poetry run pytest
```

---

## Testing

* All new code must include unit tests.
* PRs should not reduce test coverage.
* Sanitizers and fuzzing are run in CI; please run them locally before large changes.

---

## Documentation

* Public APIs must be documented with docstrings (Python) or Doxygen comments (C++).
* Run `docs` workflow locally to preview changes.

---

## Security

Do **not** file vulnerabilities as issues. Please report them privately as described in [SECURITY.md](SECURITY.md).

---

## Governance

Contribution and decision-making processes are described in [GOVERNANCE.md](GOVERNANCE.md).

---

## Licensing

By contributing, you agree that your contributions will be licensed under the [GPLv3 License](LICENSE). Each file must include the SPDX license identifier and copyright header.

---
