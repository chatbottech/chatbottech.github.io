"""
Collect all review files and spit out their content as a tex document.
"""
import glob

import frontmatter
import misaka

from latexrenderer import LatexRenderer

REVIEWS_GLOB = "../_reviews/*.md"


def get_reviews():
    paths = glob.glob(REVIEWS_GLOB)
    reviews = []
    for path in paths:
        review = frontmatter.load(path)
        # print(review['title'])
        # print(content)
        reviews.append(review)
    return sorted(reviews, key=lambda x: x['name'])


def clean(content):
    return content.replace('_', '')


def render_content(reviews):
    renderer = LatexRenderer()
    markdown = misaka.Markdown(renderer)
    for review in reviews:
        name = review['name']
        title = markdown(clean(review['title'])).strip()
        # print("TITLE", title)
        # title = markdown(title.replace(name, "\\textbf{%s}" % name)).strip()
        print("\section*{%s}\n" % title)
        print("\markboth{%s}{%s}\n\n" % (name, name))

        print("\\begin{block}\\begin{tabular}{lp{5.5cm}}")
        for info in review['info']:
            key = info['name']
            value = markdown(info['value']).strip()
            print("%s: & %s\\\\" % (key, value))

        for info in review['ratings']:
            key = info['name']
            value = info['value']
            print("%s: & %s\\\\" % (key, '$' + '\\bigstar ' * value + '$'))
        print("%s: & %s\\\\" % ("Overall score:", "%d\\%%" % review['score']))
        print("\\end{tabular}\\end{block}\n\n")

        content = markdown(clean(review.content))
        print(content)
        print("\\raggedbottom\n\\pagebreak\n")


if __name__ == "__main__":
    reviews = get_reviews()
    render_content(reviews)
