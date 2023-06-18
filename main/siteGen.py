from jinja2 import Environment, FileSystemLoader
from controller import Controller

class SiteGen():
    def __init__(self):
        bigbrain = Controller()
        self.users = bigbrain.users
        self.stations = bigbrain.stations
        self.bikes = bigbrain.bikes
        self.env = Environment(loader=FileSystemLoader('templates'))
        self.template = self.env.get_template('./site/templates/template1.html')

    def generate(self):
        template_vars = {"title" : "Bike Rental", "users" : self.users, "stations" : self.stations, "bikes" : self.bikes}
        html_out = self.template.render(template_vars)
        with open("./site/index.html", "w") as f:
            f.write(html_out)
        

        