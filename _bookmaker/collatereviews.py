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
        content = markdown(clean(review.content))

        name = review['name']
        title = clean(review['title'])
        # print("TITLE", title)
        title = markdown(title.replace(name, "\\textbf{%s}" % name)).strip()
        print("\section{%s}\n" % title)
        print(content)



if __name__ == "__main__":
    reviews = get_reviews()
    render_content(reviews)
