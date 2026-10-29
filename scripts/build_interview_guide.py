#!/usr/bin/env python3
"""Rebuild the full Basic → Intermediate → Advanced interview bank PDF."""

import os
import runpy
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BANK = ROOT / "interview_bank"
os.chdir(BANK)
sys.path.insert(0, str(BANK))
runpy.run_path(str(BANK / "build.py"), run_name="__main__")
src = Path("/tmp/Vijay_Baskar_AI_Interview_Guide.pdf")
dest = ROOT.parent / "public" / "Vijay_Baskar_AI_Interview_Guide.pdf"
shutil.copy2(src, dest)
print(f"Copied {src} -> {dest}")
