from setuptools import setup, find_packages

setup(
    name="django_blogposts",
    version='0.2',
    description='Django module for simple blog',
    author='Spi4ka',
    packages=[
        "django_blogposts",
        "django_blogposts.templatetags",
        "django_blogposts.migrations",
    ],
    include_package_data=True,
    package_data={'django_blogposts': ['django_blogposts/templates', ]},
)
