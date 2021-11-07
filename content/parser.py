import frontmatter
import os
import json
import markdown
import string

from content.parser_util import collect_content_files, convert_to_slug, get_destination_dir ,InternalLinkExtension


def parse_content(src_dir=None, dest_dir=None) :

    md = markdown.Markdown(extensions=[InternalLinkExtension()])
    manifest_json = []
    md_files = collect_content_files(src_dir)
    tag_post_maps = {}
    slug_post_maps = {}

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

        with open("tags.json", "r") as f :
            tag_slug_maps = json.load(f)
        
        metadata['tag_slugs'] = []

        for tag in metadata['tags'] : 
            metadata['tag_slugs'].append({"tag_name" : tag,
                                "tag_slug" : tag_slug_maps[tag]})
            try : 
                tag_post_maps[tag_slug_maps[tag]].append(post.metadata)
            except : 
                tag_post_maps[tag_slug_maps[tag]] = [post.metadata]

        manifest_json.append(metadata)
        slug_post_maps[metadata['slug']] = metadata

        print("****Generating manifest json****")
        print(manifest_json)
        print("********")

    with open('manifest.json', 'w') as mj: 
        json.dump(manifest_json, mj)

    with open('tag_post.json', 'w') as f : 
        json.dump(tag_post_maps, f)

    with open('slug_post.json', 'w') as f : 
            json.dump(slug_post_maps, f)


def parse_tags(src_dir) :

    md_files = collect_content_files(src_dir)
    raw_tags = {}
    tag_set = []
    # tag_post_maps = {}


    for md_file in md_files : 

        with open(md_file, 'r') as f : 
            post = frontmatter.load(f)

        for tag in post.metadata['tags'] : 
            if tag not in tag_set :
                tag_set.append(tag)

                tag_slug = convert_to_slug(tag)
                raw_tags[tag] = tag_slug
                

    with open('tags.json', 'w') as f : 
        json.dump(raw_tags, f)


    print("**** Generating Tags json *****")
    print(raw_tags)
    print("*********")


