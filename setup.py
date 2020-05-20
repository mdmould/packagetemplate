import os
import setuptools

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'packagetemplate', '__version__.py'), 'r') as _:
    exec(_.read(), about)

with open ('README.md', 'r') as _:
    readme = _.read()

with open ('requirements.txt', 'r') as _:
    requires = [line.split()[0] for line in _]

setuptools.setup(
    name=about['__title__'],
    description=about['__description__'],
    long_description=readme,
    long_description_content_type='text/markdown',
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    project_urls={
        'Source Code': about['__url__'],
        'Documentation': 'https://mdmould.github.io/packagetemplate/'
    },
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3.6.*',
    install_requires=requires,
    license=about['__license__']
)
