from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='ddp2neo4j',
    version='1',
    description='Loading Patient, genetic and Ontology data related to Developmental Disorders',
    url='http://github.com//statbio',
    author='Colin Mclean',
    author_email='Colin.D.Mclean@ed.ac.uk',
    license='MIT',
    packages=['ddp2neo4j'],
    install_requires=[
        'neo4j-driver',
        'obonet',
        'networkx',
        'numpy',
        'neomodel'
    ],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
