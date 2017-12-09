import os
from jinja2 import Environment, PackageLoader


def generate_file(framework=None):
    config = {
              }

    env = Environment(
        loader=PackageLoader('codegen', 'templates')
    )

    kv = {}
    for root, dirs, files in os.walk('codegen/templates/{}'.format(framework),
                                     topdown=False):
        for name in files:
            full_path = os.path.join(root, name)
            kv[full_path] = None

    print kv
    for e in kv:
        path_components = e.split('/')
        template_path = '/'.join(path_components[2:])
        template_file = path_components[-1]
        print template_path
        print template_file

        template = env.get_template(template_path)

        kv[e] = template.render(config=config)
        print kv[e]

    for e in kv:
        path_components = e.split('/')
        template_path = '/'.join(path_components[3:-1])
        template_file = path_components[-1]

        output_path = 'output/{}'.format(template_path)
        output_file = '{0}/{1}'.format(output_path, template_file)
        try:
            os.makedirs('output/{}'.format(template_path))
        except:
            pass
        # os.makedirs(path)
        with open(output_file, 'w') as f:
            f.write(kv.get(e))
