from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'waitress',
    'webtest',
    'pyramid_debugtoolbar',
    'pytest',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points={
        'paste.app_factory': [
            'main = tutorial:main',
        ],
    },
)