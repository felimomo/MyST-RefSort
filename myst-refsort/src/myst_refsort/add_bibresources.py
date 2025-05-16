def add_bibresources(tex_file_path):
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        begin_doc_idx = tex_file_cont.find(r"\begin{document}")
        tex_file_modif = (
            tex_file_cont[:begin_doc_idx]
            + r"""\addbibresource{main.bib}
""" # new line (not sure why \n gets interpreted as a special character rather than new line)
            + tex_file_cont[begin_doc_idx:]
        )

    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)