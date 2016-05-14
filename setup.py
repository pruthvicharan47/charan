from setuptools import setup, find_packages

setup(
    name='sample-app',
    version='2.0.0',
    description='Step 1 tutorial',
    url='http://bitbucket.org/avilay/sample-app',
    author='Avilay Parekh',
    author_email='avilay@avilaylabs.net',
    license='MIT',
    packages=find_packages(exclude=['sample_app.test']),
    install_requires=['colored'],
    entry_points={
        'console_scripts': [
            'sapp=sample_app.sample_app:main'
        ]
    }
)
