"""Prepare the standalone NagoyAction commands (nagoyaction: pipelines, actionlint, hub; local-forge) as an isolated uv tool project."""
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = '[build-system]\nrequires = ["setuptools>=68"]\nbuild-backend = "setuptools.build_meta"\n\n[project]\nname = "nagoyaction"\nversion = "0.1.0"\ndescription = "Local pipeline execution, workflow lint and forge management"\nrequires-python = ">=3.11"\ndependencies = []\n\n[project.scripts]\nnagoyaction = "nagoyaction:main"\nlocal-forge = "local_forge:main"\n\n[tool.setuptools]\npy-modules = ["nagoyaction", "local_forge", "localci"]\n'

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=False)
    for name in ("nagoyaction.py", "local_forge.py", "localci.py"):
        shutil.copy2(ROOT / name, args.out / name)
    (args.out / "pyproject.toml").write_text(PYPROJECT, encoding="utf-8")

if __name__ == "__main__":
    main()
