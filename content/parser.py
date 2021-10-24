import frontmatter
import os
import json
import markdown

from content.parser_util import collect_content_files, get_destination_dir ,InternalLinkExtension


def parse_content(src_dir=None, dest_dir=None) :

    md = markdown.Markdown(extensions=[InternalLinkExtension()])
    manifest_json = []
    # slug_keys = []
    md_files = collect_content_files(src_dir)

    for md_file in md_files : 

        with open(md_file, 'r') as f : 
            post = frontmatter.load(f)

        metadata = post.metadata
        content = post.content

        html_content = md.convert(content)
        html_path = os.path.join(get_destination_dir(dest_dir), metadata['slug']+'.html')

        with open(html_path, 'w') as html_output : 
            html_output.write("{% extends 'index.html' %}\n\n")
            html_output.write("{% block blog %}\n\n")
            html_output.write(html_content)
            html_output.write("\n\n{% endblock %}")

        manifest_json.append(metadata)
        # slug_keys.append(metadata['slug'])

    with open('manifest.json', 'w') as mj: 
        json.dump(manifest_json, mj)

    # with open('blog_list.json', 'w') as bl : 
    #     json.dump(slug_keys, bl)
        