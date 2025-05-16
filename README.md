# MyST RefSort
A lil script to sort the references cited in paper alphabetically when using MyST to compile Markdown --> Tex --> pdf.
The script essentially finds the Tex output and modifies that to produce a pdf output with sorted references.
Pretty much the (unelegant) process I did by hand in order to get that result, just implemented in python to make life easy.

## Install
Using the basic pip / python install:
```{bash}
pip install git+https://github.com/felimomo/MyST-RefSort.git
```

## Run
Instead of running `myst build your-file.md` locally in your file's directory, switch to this directory and run:
```{bash}
cd Myst-RefSort/myst-refsort
python run/main.py -f path/to/your/markdown/file.md
```

The output pdf along with the generating `.tex` and `.bib` files will be placed in `myst-refsort/refsort-out`.

## Important note
At the moment, the base filename of the markdown file must match the base filename of the pdf export for the script to work, i.e. if the target markdown file is `paper.md`, the export file must be specified to be `paper.pdf`. 

## Work in progress / reach out / contribute!
This is a very raw piece of code and still needs lots of work to make it functional over a wider range of scenarios (even though the scope is narrow—--sorting references alphabetically for tex-based publications)!
Please don't hesitate to reach out, make pull requests, open issues, etc.
I made this out of my own need for it, and I would love for it to be useful for others too!
