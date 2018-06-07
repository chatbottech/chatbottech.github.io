
import misaka


class LatexRenderer(misaka.BaseRenderer):
    def paragraph(self, content):
        return content + "\n\n"

    def list(self, content, is_ordered, is_block):
        return "\\begin{itemize}\n" + content + "\\end{itemize}\n\n"

    def listitem(self, content, is_ordered, is_block):
        return "\\item " + content + "\n"

    def link(self, content, link, title):
        return "\\hyperref[title]{link}"

    def normal_text(self, text):
        text = text.replace('$', '\\$')
        return text.replace('&', '\\&')

    # def emphasis(self, content):
    #     pass
    #     # # return "\\emph{%s}" % content
    #     # return None
