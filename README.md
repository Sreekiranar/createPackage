# CreatePackage

Python package which creates the **filestructure**, basic **readme**, **setup.py** with dependencies
provided on your requirements file, **code** **blocks** with class and function templates with **doc strings**.

### Prerequisites

- **MakeTreeDir**

    Python package to easily create complex directory structures.

    https://github.com/Sreekiranar/MakeTreeDir.git

    ```python

    from MakeTreeDir import MAKETREEDIR
    md=MAKETREEDIR()
    md.makedir('this/is/a/testing/package/creation')

    ### Corner cases
    md.makedir('/media/username/New Volume/folderName')
    md.makedir('../../../folderName')
    md.makedir('C:\\Users\\userName\\folderName')
    ```

### Installation

You can easily install the package by

`pip install createPackage`

## Running the tests

If you have to create a package with the following setup:
- Package Name: `demoPackage`
- code Blocks:
    - `demoBlock1`
    - `demoBlock2`
- dependencies: contained inside a `requirements.txt` in this structure : `library1==0.1.0` or `library2`


After installing **createPackage** ,

```python
from createPackage import createPackage
packageName='demoPackage'
codeBlocks=['demoBlock1','demoBlock2']
requirements='path/to/requirements.txt'
##init class
cp=createPackage(packageName,codeBlocks,requirements)

##call main function
cp.pythonPackage()
```

This will create the following folder structure.


```
demoPackage
│   README.md
│   setup.py
│
└───demoPackage
│   │   __init__.py
│   │   demoBlock1.py
│   │   demoBlock2.py
```

- `demoBlock1.py` and `demoBlock2.py` will have basic class structure and doc strings to be filled and modifed by the user. It will also be included in the **__init__.py**

- `setup.py` will have all the dependencies from the `requirements.txt` mentioned like shown below:

    ```python
    from setuptools import setup

    with open('README.md','r') as f:
        long_description = f.read()


    setup(name='demoPackage',
          version='0.1',
          description='enter the package description',
          long_description=long_description,
          long_description_content_type="text/markdown",
          url='enter the url',
          authors='author',
          author_email='emailid',
          license='MIT',
          packages=['demoPackage'],
          install_requires=['library1==0.1.0','library2'], include_package_data=True,
          zip_safe=False)
    ```
- There will a standard `README.md` template which can be filled accordingly.




## Authors

* **Sreekiran A R** - *Analytics Consultant, AI Labs, Bridgei2i Analytics Solutions* -
 [Github](https://github.com/Sreekiranar) ,
[Stackoverflow](https://stackoverflow.com/users/9605907/sreekiran)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
