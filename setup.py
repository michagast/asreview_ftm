from setuptools import setup
from setuptools import find_namespace_packages

setup(
    name='ftm_feature_extractor',
    version='1.0',
    description='Example feature_extraction extension',
    url='https://github.com/michagast/asreview_ftm',
    author='ASReview team',
    author_email='asreview@uu.nl',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='systematic review',
    packages=find_namespace_packages(include=['asreviewcontrib.*']),
    python_requires='~=3.9',
    install_requires=[
        'sklearn',
        'torch',
        'transformers',
        'pyenchant',
        'nltk',
        'spacy',
        'num2words',
        'tensorflow',
        'spacy'
        #'spacy-legacy',
        #'termcolor',


    ],
    entry_points={
        'asreview.models.classifiers': [
            #
        ],
        'asreview.models.feature_extraction': [
            'enron = asreviewcontrib.models.ftm_fe:FTM',
        ],
        'asreview.models.balance': [
            # define balance strategy algorithms
        ],
        'asreview.models.query': [
            # define query strategy algorithms
        ]
    },
    project_urls={
        'Bug Reports': 'https://github.com/asreview/asreview/issues',
        'Source': 'https://github.com/asreview/asreview/',
    },
)
