from jinja2 import Environment, FileSystemLoader
from controller import Controller

from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env = Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("templates/template1.html")

