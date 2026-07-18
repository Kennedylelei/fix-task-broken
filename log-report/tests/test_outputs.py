import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """The agent must write /app/report.json."""
    assert REPORT.exists(), "no report.json found"


def test_report_schema():
    """report.json has the required keys with the correct types."""
    data = json.loads(REPORT.read_text())
    assert {"total_requests", "unique_ips", "top_path"} <= data.keys()
    assert isinstance(data["total_requests"], int)
    assert isinstance(data["unique_ips"], int)
    assert isinstance(data["top_path"], str)


def test_total_requests_correct():
    """total_requests matches the number of lines in access.log."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6


def test_unique_ips_correct():
    """unique_ips matches the number of distinct client IPs in access.log."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3


def test_top_path_correct():
    """top_path is the most frequently requested path in access.log."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html"