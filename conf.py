extensions = ['sphinxcontrib.bibtex']


author_first = u'Matthias'
author_last= u'Bussonnier'
author_full = u' '.join([author_first,author_last])

source_suffix = '.rst'
master_doc = 'index-latex'

exclude_patterns = ['_build']
# The name of the Pygments (syntax highlighting) style to use.

latex_documents = [
  ('index-latex', 'actingeldynamics.tex', u'Actin Gels dynamics',
   author_full, 'manual', False),
]


