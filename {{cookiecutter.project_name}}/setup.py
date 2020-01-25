# TODO: double check this, set up requirements to pull from requirements file

from setuptools import setup, find_packages

setup(name="{{cookiecutter.project_name}}",
      version="",
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "{{cookiecutter.project_name}} = {{cookiecutter.project_name}}.cli:cli"
            ]
      },
      install_requires=["boto3==1.10.14", "click=7.0"],
      setup_requires=["pytest-runner"],
      test_suite="tests",
      tests_require=["pytest", "mock", "prospector", "pytest-cov", "bandit"])
