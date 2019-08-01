import jinja2
import yaml
import os


# print(os.path.abspath('.'))
# print(os.path.realpath(__file__))

basepath = os.path.join(os.path.abspath('.'),'pageelement')
# print(basepath)
def parseyaml():
    item = {}
    for fpath, dirname, fnames in os.walk(basepath):
        print(fpath,dirname,fnames)
        for fname in fnames:
            filepath = os.path.join(fpath,fname)
            print(filepath)
            if '.yaml' in str(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    page = f.read()
                    Loader = yaml.load(page)
                    item.update(Loader)
    return item


def get_page_list(yamlpage):
    page_object = {}
    for page, names in yamlpage.items():
        a = []
        locs = names['locators']
        for loc in locs:
            a.append(loc['name'])
        page_object[page] = a
    print(page_object)
    return page_object

def create_page_py(page_object):
    print(os.path.join(os.path.abspath('.'), 'templetpate'))
    template_loader = jinja2.FileSystemLoader(searchpath=os.path.abspath('.'))
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template('templetpate')

    with open(os.path.join(os.path.abspath('.'), 'page.py'), 'w', encoding='utf-8') as f:
        f.write(template.render({'page_object': page_object}))


create_page_py(get_page_list(parseyaml()))