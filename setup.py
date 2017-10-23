from setuptools import setup, find_packages

setup(
    name='twitter-text',
    version='3.0',
    description='A library for auto-converting URLs, mentions, hashtags, lists, etc. in Twitter text. Also does tweet validation and search term highlighting.  Fork of twitter-text-py, that supports python 3.  Originally by David Ryan, Py3 port by Glyph.',
    author='Glyph',
    author_email='twitter-text-587601@glyph.im',
    url='http://github.com/glyph/twitter-text-py',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
    include_package_data=True,
    install_requires=['setuptools'],
    license = "BSD"
)
