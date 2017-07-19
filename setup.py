from setuptools import setup

setup(
    name='rarbg',
    version='0.2-dev',
    description='RSS interface to TorrentAPI',
    url='https://github.com/enchained/rarbg',
    py_modules=['rarbg'],
    install_requires=[
        'aiohttp',
        'python-dateutil',
        'humanize',
        'jinja2',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'rarbg = rarbg:main',
        ],
    }
)
