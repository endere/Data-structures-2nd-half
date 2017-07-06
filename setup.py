from setuptools import setup

setup(
    name="Binary Search Tree",
    description="Binary Search Tree in Python",
    version="0.1",
    author="Anna Shelby, Erik Enderlein",
    author_email="erik.end@gmail.com, bonanashelby@gmail.com",
    license="MIT",
    py_modules=['bst'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'ipython', 'tox']},
    entry_points={
        'console_scripts': [
            "bst = bst:main"
            ]
    }
    )
