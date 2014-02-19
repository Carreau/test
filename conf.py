extensions = ['sphinxcontrib.bibtex']

# Add any paths that contain templates here, relative to this directory.

author_first = u'Matthias'
author_last= u'Bussonnier'
author_full = u' '.join([author_first,author_last])

source_suffix = '.rst'
master_doc = 'index'
project = u'Actin gel dynamics'
copyright = u'2014, '+author_full 
version = '1.0'
release = '1.0'
today_fmt =  '%B %d, %Y at %X %Z'

exclude_patterns = ['_build','index-latex.rst']
if tags.has('latex') or tags.has('latex-web') or tags.has('latex-print'):
    exclude_patterns.remove('index-latex.rst')
    exclude_patterns.append('index.rst')
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The paper size ('letter' or 'a4').
latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

latex_documents = [
  ('index-latex', 'actingeldynamics.tex', u'Actin Gels dynamics',
   author_full, 'manual', False),
]


