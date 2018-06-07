import re
import misaka

IMAGE_REGEX = re.compile(r'<img src=\"([^\"]+)\"')


class LatexRenderer(misaka.BaseRenderer):
    def paragraph(self, content):
        return content + "\n\n"

    def list(self, content, is_ordered, is_block):
        return "\\begin{itemize}\n" + content + "\\end{itemize}\n\n"

    def listitem(self, content, is_ordered, is_block):
        return "\\item " + content + "\n"

    def link(self, content, link, title):
        link = link.replace('#', '\#')
        return "\\href{%s}{%s}" % (link, content)

    def normal_text(self, text):
        text = text.replace('$', '\\$')
        return text.replace('&', '\\&')

    def raw_html(self, text):
        match = IMAGE_REGEX.match(text)
        if match is not None:
            image = match.group(1)
            return "\\begin{center}\\includegraphics[width=\\textwidth]{..%s}\\end{center}" % image

    # def emphasis(self, content):
    #     pass
    #     # # return "\\emph{%s}" % content
    #     # return None
