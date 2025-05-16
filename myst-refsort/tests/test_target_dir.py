from myst_refsort import get_latest_modified_dir

import os
import time

def test():
    os.makedirs("_build/temp/1", exist_ok=True)
    time.sleep(2)
    os.makedirs("_build/temp/2", exist_ok=True)
    latest_dir = get_latest_modified_dir()
    assert latest_dir=="_build/temp/2", f"test_target_dir.py: expected latest_dir = _build/temp/2, got {latest_dir}."
    #
    os.removedirs("_build/temp/1")
    os.removedirs("_build/temp/2")


if __name__ == "__main__":
    test()