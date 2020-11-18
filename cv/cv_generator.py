from jinja2 import Template
import yaml

template = env.get_template('mytemplate.html')

with open("cv.yml", 'r') as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)
