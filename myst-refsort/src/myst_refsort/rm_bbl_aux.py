import os

def rm_bbl_aux(path, base_fname) -> None:
    os.remove(
        os.path.join(path, base_fname+".bbl")
    )
    os.remove(
        os.path.join(path, base_fname+".aux")
    )