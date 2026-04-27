
import pytest
from cruxpy.repo import port as cruxport


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

def test_port_expose(tmp_path):
    port = tmp_path / "testport"
    port.mkdir()

    pkgfile = port / "Pkgfile"
    pkgfile.write_text(content)

    p = cruxport(str(pkgfile), git_info=False)
    p.expose_pkgfile()

    assert p.name == name
    assert p.version == f"{ version }-{ release }"
    assert p.source == source
