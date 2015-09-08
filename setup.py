from setuptools import setup

import os


# Installed name used for various commands (both script and setuptools).
command_name = "make_ipython_toc"

with open("dev_requirements.txt") as file:
    tests_require = [dep.strip() for dep in file.readlines()]

setup(name="make_ipython_toc",
      version="0.0.1",
      description="Build a table of contents from a IPython notebook.",
      author="Alex LordThorsen",
      author_email="AlexLordThorsen@gmail.com",
      url="https://github.com/rawrgulmuffins/ipython_table_of_contents",
      packages=["make_ipython_toc", "make_ipython_toc.test"],
      include_package_data=True,
      install_requires=[],
      test_suite="make_ipython_toc.test",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
      ],
      zip_safe=True,
)
