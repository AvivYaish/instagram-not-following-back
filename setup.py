from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='instagram-not-following-back',
    version='1',
    description='A python script that prints users that are not following you back.',
    long_description=readme(),
    install_requires=[
        'instaloader'
    ],
)
