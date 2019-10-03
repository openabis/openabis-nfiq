from distutils.core import setup

setup(
    name='openabis-nfiq',
    version='0.0.1',
    packages=['openabis_nfiq'],
    url='https://github.com/newlogic42/openabis-nfiq',
    license='Apache License 2.0',
    author='newlogic42',
    author_email='',
    description='OpenAbis\' integration plugin for NFIQ',
    install_requires=[
        'pillow==6.2.1'
    ]
)
