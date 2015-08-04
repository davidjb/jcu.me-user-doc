# -*- coding: utf-8 -*-
#
# Plone User Documentation documentation build configuration file, created by
# sphinx-quickstart on Tue Feb 16 15:30:03 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------


def setup(app):
    app.add_config_value('metadata', {}, 'env')
    app.add_config_value('tags', [], 'env')


on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
metadata = {
    'project': {
        'name': u'Research Portfolio',
        'shortname': 'ResearchPortfolioUserDocumentation',
        'team': u'eResearch Centre, James Cook University',
        'url': 'https://jcu.me'
    }
}
current_year = datetime.datetime.now().year


# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.intersphinx', 'sphinx.ext.ifconfig']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'%s Documentation' % metadata['project']['name']
copyright = u'CC-BY-NC %i %s' % (current_year, metadata['project']['team'])

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

#A list of global patterns that should be excluded when looking for files. 
#The following have been included to prevent a warning as they are not used in the toctree. 
exclude_patterns = []

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# A string of reStructuredText that will be included at the end of every source
# file that is read. This is the right place to add substitutions that should
# be available in every file.
rst_epilog = '\n'
for key, value in metadata['project'].items():
    replacement = '.. |project-%s| replace:: %s\n' % (key, value)
    rst_epilog += replacement

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'bootstrap'
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
                      
# Bootswatch (http://bootswatch.com/) theme.
#
# Options are nothing with "" (default) or the name of a valid theme
# such as "amelia" or "cosmo".
#
# Note that this is served off CDN, so won't be available offline.
    #'bootswatch_theme': "spacelab",
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

if not on_rtd:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = metadata['project']['shortname']

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index',
   '%s.tex' % metadata['project']['shortname'],
   u'%s Documentation' % metadata['project']['name'],
   metadata['project']['team'],
   'manual'),
]

# Configuration for LaTeX snippets for generated .tex files
latex_elements = {'papersize': 'a4paper',
                  'pointsize': '10pt',
                  'classoptions': ',openany,oneside',
                  'babel': '\\usepackage[english]{babel}'}

# Control whether to display URL addresses.
latex_show_urls = 'inline'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'images/logo.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

#If true, add page references after internal references.
latex_show_pagerefs = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
