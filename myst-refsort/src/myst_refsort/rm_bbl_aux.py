import os
import subprocess

def rm_bbl_aux(path, base_fname) -> None:
    # os.remove(
    #     os.path.join(path, base_fname+".bbl")
    # )
    # os.remove(
    #     os.path.join(path, base_fname+".aux")
    # )
    subprocess.run(["rm", f"{base_fname}.aux"])
    subprocess.run(["rm", f"{base_fname}.bbl"])