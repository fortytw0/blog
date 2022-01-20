import frontmatter
import os
import json
import markdown
import string

from content.parser_util import *


def parse_content(src_dir=None, dest_dir=None) :

    
    md_files = collect_content_files(src_dir)
    num_md_files = len(md_files)

    manifest_json = []
    tag_post_maps = {}
    slug_post_maps = {}

    for i, md_file in enumerate(md_files) : 

        print("Working on : {}/{}".format(i+1, num_md_files))

        content, metadata = content_and_meta_from_md(md_file)
        save_md_content_as_html(content, metadata, dest_dir)

        #--------#
        
        print("Generating the tag-slug json...")

        with open("tags.json", "r") as f :
            tag_slug_maps = json.load(f)
        
        metadata['tag_slugs'] = []

        for tag in metadata['tags'] : 
            metadata['tag_slugs'].append({"tag_name" : tag,
                                "tag_slug" : tag_slug_maps[tag]})
            try : 
                tag_post_maps[tag_slug_maps[tag]].append(metadata)
            except : 
                tag_post_maps[tag_slug_maps[tag]] = [metadata]

        save_as_json(tag_post_maps, 'tag_post.json')
        save_as_json(slug_post_maps, 'slug_post.json')

        #--------#

        print("Generating manifest metadata json...")
        manifest_json.append(metadata)
        save_as_json(manifest_json, 'manifest.json')

        #--------#
        
        print("Generating slug-metadata json")
        slug_post_maps[metadata['slug']] = metadata
        save_as_json(slug_post_maps, 'slug_post.json')

        #--------#

        print("Finished working on {}.\n\n".format(md_file))




def parse_tags(src_dir) :

    md_files = collect_content_files(src_dir)
    raw_tags = {}
    tag_set = []


    for md_file in md_files : 

        with open(md_file,encoding = 'utf-8', mode = "r+") as f : 
            post = frontmatter.load(f)

        for tag in post.metadata['tags'] : 
            if tag not in tag_set :
                tag_set.append(tag)

                tag_slug = convert_to_slug(tag)
                raw_tags[tag] = tag_slug
                
    save_as_json(raw_tags, 'tags.json')



