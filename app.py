import sys
from pathlib import Path

_root = Path(__file__).resolve().parent
_src = _root / "src"
if _src.is_dir() and str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from pc_fault_diagnosis.ui.streamlit_app import main

main()
