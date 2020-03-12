from setuptools import find_packages, setup
from sockets.sockets import settings

setup(
    name='sockets',
    version=settings.__VERSION__,
    url='https://github.com/YUND4/Django-WebSocket',
    author='SwankyGG',
    author_email='syundarivera@gmail.com',
    description="Implementation of websockets django project",
    license='',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.5',
    install_requires=[
        'Django>=2.2',
        'asgiref~=3.2',
        'daphne~=2.3',
        'channels_redis==2.4.2'
    ],
    extras_require={
        'tests': [
            'pytest~=4.4',
            "pytest-django~=3.4",
            "pytest-asyncio~=0.10",
            "async_generator~=1.10",
            "async-timeout~=3.0",
            'coverage~=4.5',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ],
)