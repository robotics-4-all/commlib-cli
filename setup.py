"""
CLI for broker-based communication using commlib-py
"""
from setuptools import find_packages, setup

required = []

setup(
    name='commlib-cli',
    version='0.2.0',
    url='https://github.com/klpanagi/commlib-cli',
    license='MIT',
    author='Konstantinos Panayiotou',
    author_email='klpanagi@gmail.com',
    description='CLI for broker-based communication using commlib-py',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=required,
    entry_points={
        'console_scripts': [
            'commlib-cli = commlib_cli.cli:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
