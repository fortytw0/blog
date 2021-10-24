import os
import glob

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

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
        # PATTERN = r'\[(.*)\]\|([a-zA-Z0-9_%\-\?=&]*)\|' 
        PATTERN = r'\((.*)\)\|(.*)\|'
        md.inlinePatterns.register(InternalLinkProcessor(PATTERN, md), 'internal-link', 175)
    


