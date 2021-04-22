from setuptools import setup, find_packages

setup(
    name='yapper',
    version='0.0.1b3',
    packages=find_packages(),
    scripts=['yapper/__init__.py'],
    entry_points={
        'console_scripts': [
            'yapper = yapper.__init__:cli',
        ],
    },
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
        'pyyaml'
    ]
)
