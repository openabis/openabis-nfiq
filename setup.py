from distutils.core import setup

setup(
    name='openabis-nfiq',
    version='0.0.2',
    packages=['openabis_nfiq'],
    url='https://github.com/newlogic42/openabis-nfiq',
    license='Apache License 2.0',
    author='newlogic42',
    author_email='',
    description='OpenAbis\' integration plugin for NFIQ',
    include_package_data=True,
    install_requires=[
        'pillow==6.2.1'
    ]
)
