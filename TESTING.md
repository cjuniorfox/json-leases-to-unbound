# Testing Guide

## Quick Start

Install test dependencies:

```sh
pip install -e ".[test]"
```

Run all tests:

```sh
pytest
```

## Test Results

✅ **33 tests passing** with **91% code coverage**

### Coverage by Module
- `cli.py`: 100% coverage
- `core.py`: 91% coverage
- Overall: 91% coverage

## Usage Examples

### Run with coverage report
```sh
pytest --cov=json_leases_to_unbound --cov-report=term-missing
```

### Run with verbose output
```sh
pytest -v
```

### Run specific test file
```sh
pytest tests/test_core.py
pytest tests/test_cli.py
```

### Run specific test class
```sh
pytest tests/test_core.py::TestLeaseExtraction
pytest tests/test_cli.py::TestCLI
```

### Run specific test
```sh
pytest tests/test_core.py::TestLeaseExtraction::test_extract_leases_valid_data
```

### Generate HTML coverage report
```sh
pytest --cov=json_leases_to_unbound --cov-report=html
# Open htmlcov/index.html in browser
```

## What's Tested

### Core Functionality (`test_core.py`)
- ✅ Lease extraction from JSON
- ✅ Lease filtering by expiration  
- ✅ DNS record generation (AAAA and PTR)
- ✅ Unbound control discovery and execution
- ✅ File system monitoring and event handling
- ✅ Lease lifecycle (add/modify/delete)
- ✅ Directory and file processing

### CLI (`test_cli.py`)
- ✅ Argument parsing
- ✅ Default values
- ✅ Custom configuration
- ✅ Input validation

## Test Fixtures

Available fixtures in `conftest.py`:
- `temp_lease_dir` - Temporary directory for test files
- `sample_lease_data` - Sample IPv6 lease data
- `sample_lease_file` - Pre-created lease file
- `mock_unbound_control` - Mocked unbound-control

See `tests/README.md` for detailed documentation.
