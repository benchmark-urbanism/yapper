from setuptools import setup, find_packages

setup(
    name='yapper',
    version='0.0.1',
    packages=find_packages(),
    scripts=['yapper/__init__.py'],
    entry_points={
        'console_scripts': [
            'yapper = yapper.__init__:cli',
        ],
    },
    description='Simple python parser converting docstrings to markdown for static site generators.',
    url='https://github.com/benchmark-urbanism/yapper',
    project_urls={
        "Bug Tracker": "https://github.com/benchmark-urbanism/yapper/issues",
        "Documentation": "https://github.com/benchmark-urbanism/yapper",
        "Source Code": "https://github.com/benchmark-urbanism/yapper",
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
