import os

def bib_file_changes(tex_file_path):
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        tex_file_modif = (
            tex_file_cont
            .replace("\i", "i") # some google scholar bibtex references had this character??
            .replace(" &", " \&") # avoid biblatex/biber/etc confusing it with align character
        )

    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)
