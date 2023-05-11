from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("templates/template2.html")

with open("pages/page1.md") as markdown_file:
    article1 = markdown(
        markdown_file.read(), extras=["fenced-code-blocks", "code-friendly"]
    )

with open("pages/page2.md") as markdown_file:
    article2 = markdown(
        markdown_file.read(), extras=["fenced-code-blocks", "code-friendly"]
    )

with open("pages/page3.md") as markdown_file:
    article3 = markdown(
        markdown_file.read(), extras=["fenced-code-blocks", "code-friendly"]
    )

with open("pages/aboutme.md") as markdown_file:
    aboutme = markdown(
        markdown_file.read(), extras=["fenced-code-blocks", "code-friendly"]
    )

with open("config.json") as config_file:
    config = load(config_file)

with open("index.html", "w") as output_file:
    output_file.write(
        template.render(
            title=config["title"],
            aboutme=aboutme,
            article1=article1,
            article2=article2,
            article3=article3,
        )
    )
