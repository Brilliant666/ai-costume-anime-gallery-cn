"""Rebuild the standalone gallery with source-hosted images only."""
import os
from pathlib import Path
import subprocess
import sys
root = Path(__file__).resolve().parent
env = dict(os.environ, SITE_URL="https://photoai.life/costume-anime", PYTHONUTF8="1")
subprocess.run([sys.executable, str(root / "sites/costume-anime/scripts/build_gallery.py")], env=env, check=True)
