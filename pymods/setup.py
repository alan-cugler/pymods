from setuptools import setup

setup(name='pymods',
      version='0.1',
      description='a python mod manager for Bethesda games.',
      url='https://github.com/alan-cugler/pymods',
      author='Alan Cugler',
      author_email='alan.cugler101@gmail.com',
      license='GPL',
      packages=[
        'tkinter',
        'platform',
        'patool'],
      zip_safe=False)
