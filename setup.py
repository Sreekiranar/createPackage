from setuptools import setup

with open('README.md','r') as f:
	long_description = f.read()


setup(name='createPackage',
	  version='1.0',
	  description='package to create file structure when making your own package.',
	  long_description=long_description,
	  long_description_content_type="text/markdown",
	  url='https://github.com/Sreekiranar/createPackage.git',
	  authors='Sreekiran A R',
	  author_email='sreekiranar@gmail.com',
	  license='MIT',
	  packages=['createPackage'],
	  install_requires=['MakeTreeDir'], include_package_data=True,
	  zip_safe=False)
