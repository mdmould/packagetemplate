import setuptools
import sys

sys.path.append("packagetemplate")

from _version import __version__

setuptools.setup(
    name="packagetemplate",
    version=__version__,
    author="Matthew Mould",
    author_email="mattdmould@gmail.com",
    packages=setuptools.find_packages(),
)
