"""
Finds the target dir with latex code from which to build the updated pdf.
"""

import os

DEFAULT_PATH = os.path.join("_build", "temp")

def get_latest_modified_dir(path: str = DEFAULT_PATH):
    most_recent_folder = None
    most_recent_time = 0

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            modified_time = os.path.getmtime(item_path)
            if modified_time > most_recent_time:
                most_recent_time = modified_time
                most_recent_folder = item_path

    return most_recent_folder