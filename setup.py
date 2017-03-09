from setuptools import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="beets-bbq",
    version="0.0.1",
    description="blackbird style search query plugin for beets",
    long_description=readme,
    url="https://github.com/lepisma/beets-bbq",
    install_requires=["beets>=1.4.3"],
    keywords="beets plugin search music",
    packages=["beetsplug"],
    namespace_packages=["beetsplug"],
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English", "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"))
