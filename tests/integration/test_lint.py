"""Check scaffolded content integration with ansible-lint."""

import re
import sys
from collections.abc import Callable
from pathlib import Path
from subprocess import CalledProcessError, CompletedProcess
from typing import Any

cli_type = Callable[[Any], CompletedProcess[str] | CalledProcessError]

CREATOR_BIN = Path(sys.executable).parent / "ansible-creator"
LINT_BIN = Path(sys.executable).parent / "ansible-lint"


def test_create_collection(cli: cli_type, tmp_path: Path) -> None:
    """Test running ansible-creator --help.

    Args:
        cli: cli_run function.
        tmp_path: Temporary path.
    """
    final_dest = f"{tmp_path}/collections/ansible_collections"
    cli(f"mkdir -p {final_dest}")

    result = cli(
        f"{CREATOR_BIN} init testorg.testcol --init-path {final_dest}",
    )
    assert result.returncode == 0

    # check stdout
    assert re.search("Note: collection testorg.testcol created at", result.stdout) is not None

    result = cli(
        f"{LINT_BIN} {final_dest}",
    )
    assert result.returncode == 3

    # check stdout
    assert (
        re.search(
            "WARNING  The following filters were mocked during the run: testorg.testcol.hello_world",
            result.stdout,
        )
        is not None
    )
