import os
import glob
import frontmatter
import markdown
import json

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

# parse internal links like this : 
# (internal-link-title)|slug-to-internal-link|
# (tutorial)|this_is_a_tutorial|

def collect_content_files(src_dir=None) :

    if src_dir is None : 
        src_dir = os.getcwd()

    files = glob.glob(os.path.join(src_dir, '*.md'))
    return files

def get_destination_dir(dest_dir=None) : 

    if dest_dir is None:
        dest_dir = os.path.join(os.getcwd(), "html")

    if not os.path.exists(dest_dir) : 
        os.mkdir(dest_dir)

    return dest_dir

def convert_to_slug(s) :

    import string

    slug = s.strip().lower()
    slug = "".join(c for c in slug if c not in string.punctuation)
    slug = slug.replace(" ", "_")

    return slug
 
def content_and_meta_from_md(md_file_path) :

    with open(md_file_path, encoding = 'utf-8', mode = 'r+') as f : 
            post = frontmatter.load(f)

    metadata = post.metadata
    content = post.content

    return content, metadata

def save_md_content_as_html(content, metadata, dest_dir) : 

    md = markdown.Markdown(extensions=[InternalLinkExtension()])
    html_content = md.convert(content)
    html_path = os.path.join(get_destination_dir(dest_dir), metadata['slug']+'.html')

    with open(html_path, encoding='utf-8', mode='w') as html_output : 
        html_output.write("{% extends 'index.html' %}\n\n")
        html_output.write("{% block blog %}\n\n")
        html_output.write(html_content)
        html_output.write("\n\n{% endblock %}")

def save_as_json(iterable, path, verbose=True):

    with open(path, encoding='utf-8', mode='w') as f : 
        json.dump(iterable, f)

    if verbose : 
        print("Saved to : ", path)



class InternalLinkProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('a')
        print()
        el.attrib['href'] = "{{% {} '{}' '{}' %}}".format('url', 'blog', m.group(2))
        # el.attrib['href'] = "{% url 'blog' %}"
        el.text = m.group(1)
        return el, m.start(0), m.end(0)

class InternalLinkExtension(Extension):
    def extendMarkdown(self, md):
        PATTERN = r'\((.*)\)\|(.*)\|'
        md.inlinePatterns.register(InternalLinkProcessor(PATTERN, md), 'internal-link', 175)
    


