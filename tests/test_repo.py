import pytest
from pathlib import Path
from cruxpy.portspage import page


name    = "test-port"
version = "1.2.3"
release = "1"
source  = "http://example.com/src.tar.gz"

content = f"""# Description: A test port
# URL: https://wawrzek.name
# Maintainer: John Doe
# Depends on: other_port

name={ name }
version={ version }
release={ release }
source=({ source })

build() {{
    ./configure
    make
}}
"""


def test_repo_page(tmp_path):
    ports = tmp_path / "ports"
    ports.mkdir()
    port1 = ports / "testport"
    port1.mkdir()
    pkgfile1 = port1 / "Pkgfile"
    pkgfile1.write_text(content)

    p = page(str(ports), git_info=False)
    p.read_repo()

    assert p.style == "original"
    assert len(p.ports) == 1

#    assert repo_page

