# main cli script

import argparse
import os
import subprocess

import myst_refsort as mrs

parser = argparse.ArgumentParser(
                    prog='MyST-RefSort-CLI',
                    description='Helps you sort your MyST references alphabetically in a quick-n-dirty way!',
                    epilog='Hope this saves you some time! Felipe / Momo')

parser.add_argument(
    "-f", "--filename", 
    help="the markdown file you want myst to build and whose refs you want to sort alphabetically",
)

args = parser.parse_args()


# 1. run myst
subprocess.run(["myst", "build", f"{args.file_name}"])

# 2. get target dir
myst_md_main = os.path.dirname(args.filename)
target_parent = os.path.join(
    myst_md_main,
    "_build",
    "temp"
)
target_dir = mrs.get_latest_modified_dir(path=target_parent)

# 3. cd to target dir
# subprocess.run(["cd", f"{target_dir}"]) # nope i think?
os.chdir(target_dir)

# 4. rm bbl and aux
fname_no_path = os.path.basename(args.filename)
base_fname = "".join(
    fname_no_path.split(".")[:-1] # ie, just omit the extension, like .tex
)
mrs.rm_bbl_aux(path=".", base_fname=base_fname)

# 5. biblatex commands

# 6. bibfile edits

# 7. recompile tex

subprocess.run(["pdflatex", f"{base_fname}"])
subprocess.run(["biber", f"{base_fname}"])
subprocess.run(["pdflatex", f"{base_fname}"])
subprocess.run(["pdflatex", f"{base_fname}"])

