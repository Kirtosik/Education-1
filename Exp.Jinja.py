from jinja2 import Template

name = "Кирилл"

tm = Template("Привет {{name}}")
msg = tm.render(name=name)

print(msg)