# MyST RefSort
A lil script to sort the references cited in paper alphabetically when using MyST to compile Markdown --> Tex --> pdf.
The script essentially finds the Tex output and modifies that to produce a pdf output with sorted references.
Pretty much the (unelegant) process I did by hand in order to get that result, just implemented in python to make life easy.

## Install
Using the basic pip / python install:
```{bash}
git clone https://github.com/felimomo/MyST-RefSort.git
cd Myst-RefSort/myst-refsort
pip install .
```

## Run
Instead of running `myst build your-file.md` locally in your file's directory, switch to this directory and run:
```{bash}
python myst-refsort/run/main.py -f path/to/your/markdown/file.md
```
