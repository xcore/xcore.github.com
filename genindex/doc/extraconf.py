import os
doc_dir = os.path.abspath(os.environ['DOC_DIR'])

def new_write_colspecs(self):
    pass

def setup(app, c, tags):
    c.set_value('html_theme','xoss')
    from sphinx.writers.html import HTMLTranslator as translator
    setattr(translator, 'write_colspecs', new_write_colspecs)
