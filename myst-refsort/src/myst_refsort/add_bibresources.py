def add_bibresources(tex_file_path):
    with open(tex_file_path, "r") as tex_file:
        tex_file_cont = tex_file.read()
        begin_doc_idx = tex_file_cont.find("\begin{document}")
        tex_file_modif = (
            tex_file_cont[:begin_doc_idx]
            + "\bibresource{main.bib}\n"
            + tex_file_cont[begin_doc_idx:]
        )

    with open(tex_file_path, "w") as tex_file:
        tex_file.write(tex_file_modif)