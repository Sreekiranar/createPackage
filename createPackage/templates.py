

readmeTemplate="""
# PACKAGE_NAME

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installation

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system


## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **NAME** - *Initial work* - [NAME](urlforname)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


"""
setupTemplate="""
from setuptools import setup

with open('README.md','r') as f:
    long_description = f.read()


setup(name='PACKAGE_NAME',
      version='0.1',
      description='enter the package description',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='enter the url',
      authors='author',
      author_email='emailid',
      license='MIT',
      packages=['PACKAGE_NAME'],
      install_requires=REQUIREMENTS, include_package_data=True,
      zip_safe=False)
"""

codeBlockTemplate="""
class CLASS_NAME:
    '''enter the description for the class here'''
    def __init__(self,arg1):
        '''Short summary.

        Args:
            arg1 (type): Description of parameter `arg1`.

        Returns:
            type: Description of returned object.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        '''
        arg1=self.arg1

    def func1(self):
        '''Short summary.

        Args:


        Returns:
            type: Description of returned object.

        Examples
            Examples should be written in doctest format, and
            should illustrate how to use the function/class.
            >>>

        '''
        return 0
"""
