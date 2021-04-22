'''
https://docs.python.org/3.9/distutils/examples.html
https://docs.python.org/3/distutils/setupscript.html
https://scikit-build.readthedocs.io/en/latest/usage.html

# manual deployment
pip install --upgrade setuptools wheel
python setup.py sdist bdist_wheel
pip install --upgrade twine
TESTING REPO: twine upload --repository-url https://test.pypi.org/legacy/ dist/*
DOWNLOADING FROM TEST REPO: pip install --extra-index-url https://test.pypi.org/simple/ docdown==0.0.1
OTHERWISE: twine upload dist/*
'''

from setuptools import setup

setup(
    name='yapper',
    version='0.0.1b1',
    packages=['yapper'],
    description='Simple python parser from docstrings to markdown',
    url='https://github.com/benchmark-urbanism/docdown',
    project_urls={
        "Bug Tracker": "https://github.com/benchmark-urbanism/docdown/issues",
        "Documentation": "https://github.com/benchmark-urbanism/docdown",
        "Source Code": "https://github.com/benchmark-urbanism/docdown",
    },
    author='Gareth Simons',
    author_email='info@benchmarkurbanism.com',
    license='MIT',
    install_requires=[
        'docspec',
        'docspec-python',
        'pytest',
        'pyyaml'
    ]
)
