import glob
from itertools import combinations

import frontmatter


REVIEWS_GLOB = "../_reviews/*.md"
OUTPUT_PATH = "../_comparisons/"


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
    for review1, review2 in combinations(reviews, 2):
        name1 = review1['name']
        name2 = review2['name']
        description = "%1 vs %2" % (name1, name2)
        output_file_name = description.replace(' ', '-')
        with open(OUTPUT_PATH + output_file_name, 'w') as output_file:
            
