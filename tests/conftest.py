import pytest
import os
import tempfile
import json
from pathlib import Path


@pytest.fixture
def temp_lease_dir():
    """Create a temporary directory for lease files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def sample_lease_data():
    """Sample lease data for testing."""
    return [
        {
            "Address": [0x2001, 0xdb8, 0, 0, 0, 0, 0, 1],
            "AddressType": "IPv6",
            "Hostname": "test-host",
            "Expire": "2025-12-31T23:59:59Z"
        },
        {
            "Address": [0x2001, 0xdb8, 0, 0, 0, 0, 0, 2],
            "AddressType": "IPv6",
            "Hostname": "another-host",
            "Expire": "2025-12-31T23:59:59Z"
        }
    ]


@pytest.fixture
def sample_lease_file(temp_lease_dir, sample_lease_data):
    """Create a sample lease file."""
    lease_file = os.path.join(temp_lease_dir, "test-lease.json")
    with open(lease_file, 'w') as f:
        json.dump(sample_lease_data, f)
    return lease_file


@pytest.fixture
def mock_unbound_control(mocker):
    """Mock unbound-control command execution."""
    mock_result = mocker.Mock()
    mock_result.stdout = "ok"
    mock_result.stderr = ""
    mock_result.returncode = 0
    
    mock_run = mocker.patch('subprocess.run', return_value=mock_result)
    mock_which = mocker.patch('shutil.which', return_value='/usr/sbin/unbound-control')
    
    return mock_run, mock_which
