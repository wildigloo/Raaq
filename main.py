import os
import json


ROOT = "Constellations/library"


def build_tree(path):

    tree = {}

    for item in sorted(os.listdir(path)):

        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):

            tree[item] = build_tree(full_path)


        elif item.endswith(".md"):

            relative_path = os.path.relpath(
                full_path,
                "."
            )

            name = item.replace(".md", "")

            tree[name] = {
                "file": relative_path.replace("\\", "/")
            }

    return tree



library = build_tree(ROOT)


with open("library.json", "w") as f:
    json.dump(
        library,
        f,
        indent=4
    )


print("library.json created")
