"""Logic for posts."""
from os import path
from typing import List, TYPE_CHECKING

from markdown import markdown

import dropbox

from server.utilities.config import APP_ROOT, config

if TYPE_CHECKING:
    from dropbox import Dropbox


async def get_all_posts(dbx: "Dropbox") -> "List[Dict]":
    """Gets all posts from dropbox."""
    posts = []
    for entry in dbx.files_list_folder('/blog').entries:
        post = {
            "title": entry.name.split('.')[0],
            "filename": entry.name,
        }
        posts.append(post)
    return sorted(posts, key=lambda post: post['title'], reverse=True)


async def get_post(post: "str", dbx: "Dropbox") -> "str":
    """Renders markdown post to HTML."""
    tmp_file_path: "str" = f'/tmp/{post}'
    if not path.exists(tmp_file_path):
        dbx.files_download_to_file(tmp_file_path, f"/blog/{post}")
    with open(tmp_file_path) as post_file:
        rendered_post: "str" = markdown(post_file.read())
    return rendered_post
