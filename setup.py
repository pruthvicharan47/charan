from setuptools import setup, find_packages

setup(
    name='sample-app',
    version='2.0.3',
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
    },
    package_data={
        'sample_app.package_one': ['res/*.csv', 'res/*.jpg']
    },
    data_files=[
        ('/etc/sample-app/conf/', ['conf/marvel.ini', 'conf/dc.ini'])
    ]
)
