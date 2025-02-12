import setuptools

with open('README.txt') as file:
    long_description = file.read()

setuptools.setup(
    name="nameko-django-orm",
    version="2.0.4",
    author="Jesus Gutierrez Almazan",
    author_email="jesus.pedro.gutierrez.almazan@gmail.com",
    maintainer="Rafael Mendes Pacini Bachiega",
    description="Use django into a nameko service",
    long_description=long_description,
    url="https://github.com/Mendes11/django-nameko-standalone",
    packages=['django_nameko_standalone'],
    platforms=['Linux'],
    install_requires=[
        "Django>=3",
        "nameko>=2.12.0,<4",
        "importlib-metadata<=8.5.0,>=6.0",
        "setuptools; python_version>='3.12'"
    ],
    test_suite='pytest',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 4.0",
        "Topic :: Software Development :: Libraries",
    ],
)
