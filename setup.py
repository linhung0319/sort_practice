import setuptools

setuptools.setup(
    name="sort_practice",
    version="1.0",
    packages=['sort_practice'],
    entry_points={
        'console_scripts': ['app=sort_practice.app:main']
    }
)