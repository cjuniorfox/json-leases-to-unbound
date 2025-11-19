# Tests for json-leases-to-unbound

This directory contains the pytest test suite for the json-leases-to-unbound project.

## Structure

- `conftest.py` - Shared pytest fixtures and test configuration
- `test_core.py` - Tests for core functionality (lease processing, DNS records, unbound integration)
- `test_cli.py` - Tests for CLI argument parsing and entry point

## Running Tests

### Install test dependencies

```sh
pip install -e ".[test]"
```

Or install from requirements.txt:

```sh
pip install -r requirements.txt
```

### Run all tests

```sh
pytest
```

### Run with coverage report

```sh
pytest --cov=json_leases_to_unbound --cov-report=html
```

### Run specific test file

```sh
pytest tests/test_core.py
```

### Run specific test class or function

```sh
pytest tests/test_core.py::TestLeaseExtraction
pytest tests/test_core.py::TestLeaseExtraction::test_extract_leases_valid_data
```

### Run with verbose output

```sh
pytest -v
```

### Run only fast tests (skip slow ones)

```sh
pytest -m "not slow"
```

## Test Coverage

The test suite covers:

- ✅ Lease extraction from JSON files
- ✅ Lease filtering by expiration
- ✅ DNS record generation (A/AAAA and PTR records)
- ✅ Unbound control binary discovery
- ✅ Unbound control command execution
- ✅ File system event handling
- ✅ Lease addition, modification, and removal
- ✅ Initial directory processing
- ✅ CLI argument parsing
- ✅ Main entry point execution

## Fixtures

Common fixtures available in all tests:

- `temp_lease_dir` - Temporary directory for test lease files
- `sample_lease_data` - Sample lease data structure
- `sample_lease_file` - Pre-created sample lease file
- `mock_unbound_control` - Mocked unbound-control command

## Writing New Tests

When adding new tests:

1. Use appropriate test classes to group related tests
2. Use descriptive test names starting with `test_`
3. Leverage existing fixtures from `conftest.py`
4. Mock external dependencies (subprocess, file system operations)
5. Use appropriate markers for slow or integration tests

Example:

```python
def test_my_feature(sample_lease_file, mock_unbound_control):
    """Test description."""
    # Test implementation
    assert expected == actual
```
