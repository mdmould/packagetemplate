import setuptools
import sys

from _version import __version__

sys.path.append("packagetemplate")

setuptools.setup(
    name="packagetemplate",
    version=__version__,
    author="Matthew Mould",
    author_email="mattdmould@gmail.com",
    packages=setuptools.find_packages(),
)
