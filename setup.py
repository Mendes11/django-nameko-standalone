import setuptools

with open('README.txt') as file:
    long_description = file.read()

setuptools.setup(
    name="nameko-django-orm",
    version="1.3.4",
    author="Jesus Gutierrez Almazan",
    author_email="jesus.pedro.gutierrez.almazan@gmail.com",
    description="Use django into a nameko service",
    long_description=long_description,
    url="https://github.com/jesusenlanet/django-nameko-standalone",
    packages=['nameko_django_orm'],
    platforms=['Linux'],
    install_requires=[
        "Django>=1.11.27,<3.0",
        "nameko<3"
    ],
    test_suite='pytest',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 2",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Topic :: Software Development :: Libraries",
    ],
)
