from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'webtest',
    'pyramid_debugtoolbar',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points={
        'paste.app_factory': [
            'main = tutorial:main',
        ],
    },
)