import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
TEST_DIR_PARENT = THIS_DIR.parent

sys.path.insert(0, str(TEST_DIR_PARENT))
