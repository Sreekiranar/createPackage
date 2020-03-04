import os
from MakeTreeDir import MAKETREEDIR
from .templates import *
class createPackage:

	'''main class to create python package file structure'''

	def __init__(self,packageName,codeBlockList,requirements):
		"""initialising variables

		Args:
			packageName (str): Name of the package to be created
			codeBlockList (list): List of code blocks required.
									[seperate python files will be created
									for each element in the list]
			requirements (str): Path to requirements.txt which contains the list of dependencies
		"""
		self.packageName=packageName
		self.codeBlockList=codeBlockList
		self.requirements=requirements


	def pythonPackage(self):
		""" Main function to call to create package file structure
		"""

		### creating folder structure
		MAKETREEDIR().makedir(self.packageName)
		MAKETREEDIR().makedir(os.path.join(self.packageName,self.packageName))

		### creating setup.py
		self.createSetup()

		### create init.py and code blocks
		with open(os.path.join(self.packageName,self.packageName,'__init__.py'),'w') as f:
			for block in self.codeBlockList:
				f.write('from .{} import *\n'.format(block))

		### copying code block from  template
		cb=codeBlockTemplate
		with open('code_block_template.txt','w') as cbt:
			cbt.write(cb)
		with open('code_block_template.txt','r') as ff:
			lines=ff.read()
			lines=lines.replace('CLASS_NAME',block.upper())

		for block in self.codeBlockList:
			with open(os.path.join(self.packageName,self.packageName,(block+'.py')),'w') as fff:
				for line in lines:
					fff.write(line)

		### creating README.md
		rm=readmeTemplate
		with open('README_temp.txt','w') as rmt:
			rmt.write(rm)
		with open('README_temp.md','r') as readme:
			read_text=readme.read()
			read_text=read_text.replace('PACKAGE_NAME',self.packageName.upper())
		with open(os.path.join(self.packageName,'README.md'),'w') as write_readme:
			write_readme.write(read_text)
		try:
			os.remove("README_temp.txt")
			os.remove("code_block_template.txt")
		except:
			pass


	### creating setup.py from requirements.txt
	def createSetup(self):
		sp=setupTemplate
		with open('setup_template.txt','w') as spt:
			spt.write(sp)

		with open('setup_template.txt','r') as template:
			setup=template.read().replace('PACKAGE_NAME',self.packageName)

		with open(self.requirements,'r') as req:
			dependencies=req.readlines()
			dependencies=list(filter(lambda x:x!='',[dep.strip() for dep in dependencies]))
			setup=setup.replace('REQUIREMENTS',str(dependencies))
		with open(os.path.join(self.packageName,'setup.py'),'w') as writeSetup:
			writeSetup.write(setup)
		try:
			os.remove("setup_template.txt")
		except:
			pass
