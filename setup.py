from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "rt", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh.readlines()]

setup(
    name="sc-dandelion",
    use_scm_version={
        "write_to": "dandelion/logging/version.py",
        "write_to_template": "# coding: utf-8\n# file generated by setuptools_scm\n# don't change, don't track in version control\n__version__ = '{version}'.split('+')[0]",
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    },
    author="zktuong",
    author_email="z.tuong@uq.edu.au",
    description="sc-TCR/BCR-seq analysis tool",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zktuong/dandelion/",
    packages=find_packages(),
    setup_requires=["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.0"],
    install_requires=requirements,
    extras_require={
        "docs": [
            "airr",
            "biopython",
            "changeo",
            "presto",
            "pyyaml",
            "yamlordereddictloader",
            "sphinx<7",  # see issue at https://github.com/readthedocs/readthedocs.org/issues/10279
            "nbsphinx<=0.9.2",
            "sphinx-autodoc-typehints<=2.2.2",
            "sphinx_rtd_theme<=2.0.0",
            "readthedocs-sphinx-ext<=2.2.5",
            "recommonmark<=0.7.1",
        ],
        "scirpy": ["scirpy<=0.17.0", "awkward", "mudata"],
    },
    package_data={
        "dandelion": ["bin/tigger-genotype.R", "bin/MakeDb_gentle.py"]
    },
    data_files=[("bin", ["bin/tigger-genotype.R", "bin/MakeDb_gentle.py"])],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    zip_safe=False,
)
