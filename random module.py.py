from setuptools import setup

setup (
    name='random2',
    version='1.0.1',
    author = "PSF",
    description = "Python 3 compatible Pytohn 2 `random` Module.",
    long_description = (
        open('CHANGES.txt').read()
        + '\n\n' +
        open('README.txt').read()
        ),
    license = "Python 2.1.1",
    keywords = "roman",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent'],
    url = 'http://pypi.python.org/pypi/random2',
    package_dir={"": "src"},
    py_modules=['random2'],
    include_package_data = True,
    test_suite = 'tests.test_suite',
    zip_safe = True,
    )
