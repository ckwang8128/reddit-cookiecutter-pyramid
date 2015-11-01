from setuptools import setup, find_packages

from baseplate.integration.thrift.command import ThriftBuildPyCommand


setup(
    name="{{ cookiecutter.project_name }}",
    packages=find_packages(),
    install_requires=[
        "pyramid",
        "baseplate",
    ],
    cmdclass={
        "build_py": ThriftBuildPyCommand,
    },
)
