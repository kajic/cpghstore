import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, Extension

cpghstore = Extension(
    'cpghstore', sources=['src/cpghstore.c'], extra_compile_args=['-O3']
)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: C',
    'Programming Language :: Python',
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='cpghstore',
    version='0.1',
    description='Fast postgres hstore parser.',
    author='Robert Kajic',
    author_email='robert@{nospam}kajic.com',
    url='https://github.com/kajic/cpghstore',
    license='MIT',
    plaforms=['any'],
    ext_modules=[cpghstore],
    classifiers=CLASSIFIERS,
    test_suite='tests',
)
