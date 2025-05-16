def use_biblatex(tex_file_path):
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        tex_file_modif = (
            tex_file_cont
            .replace(
                r"\usepackage{natbib}", 
                r"\usepackage[style=authoryear,backend=biber]{biblatex}")
        )
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)

def citep_to_parencite(tex_file_path):
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        tex_file_modif = (
            tex_file_cont
            .replace(
                r"\citep",
                r"\parencite"
            )
        )
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)

def print_bibliography(tex_file_path):
    r"""
    1. comment out \bibliography and \bibliographystyle lines
    2. add a \printbibliography command right after
    """
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        tex_file_modif = (
            tex_file_cont
            .replace(r"\bibliography{main.bib}", r"% \bibliography{main.bib}")
            .replace(
                r"\bibliographystyle", 
                r"% \bibliographystyle"
            )
        )
        end_doc_idx = tex_file_modif.find(r"\end{document}")
        tex_file_modif = (
            tex_file_modif[:end_doc_idx]
            + r"\printbibliography" + "\n\n"
            +tex_file_modif[end_doc_idx:]
        )

#         bibstyle_idx = tex_file_modif.find(r"% \bibliographystyle")
#         after_bibstyle = tex_file_modif[bibstyle_idx:]
#         next_newline_idx_rel = after_bibstyle.find("\n")
#         next_newline_idx = bibstyle_idx + next_newline_idx_rel
#         tex_file_modif = (
#             tex_file_modif[:next_newline_idx+2]
#             + r"""\printbibliography
# """
#             + tex_file_modif[next_newline_idx+2:]
#         )
    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)
