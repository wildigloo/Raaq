from pathlib import Path
import markdown

LIBRARY = Path("Library")
OUTPUT = Path("Website")

OUTPUT.mkdir(exist_ok=True)


for md_file in LIBRARY.rglob("*.md"):

    # keep the same folder structure
    relative_path = md_file.relative_to(LIBRARY)

    html_file = OUTPUT / relative_path.with_suffix(".html")

    html_file.parent.mkdir(parents=True, exist_ok=True)

    # read markdown
    text = md_file.read_text(encoding="utf-8")

    # convert
    converted = markdown.markdown(
        text,
        extensions=["tables"]
    )

    # wrap in webpage
    page = f"""
<html>
<head>
<title>{md_file.stem}</title>

<style>
body {{
    font-family: Arial;
    max-width: 900px;
    margin: auto;
    padding: 30px;
}}

table {{
    border-collapse: collapse;
}}

td, th {{
    border: 1px solid black;
    padding: 8px;
}}
</style>

</head>

<body>

{converted}

</body>
</html>
"""

    html_file.write_text(page, encoding="utf-8")


print("Done converting library")