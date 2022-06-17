import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S2FLN1',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# FLN1 : Entry to premises \r\n\r\nThe FLN1 application aids users with disabilities to report instances of refusal-for entry into restaurants. This application was created as there is a significant need for a mechanism that allows those with assistance animals to file acts of discrimination when refused entry into hospitality settings. Each user receives a generated PDF that is sent via email that allows the collation of data to raise awareness on the issue.\r\n\r\n## Authors\r\n\r\nRobert Piovesan, piov0007@flinders.edu.au<br/>\r\nChristopher Power, powe0246@flinders.edu.au<br/>\r\nKhevalin Parekh, pare0036@flinders.edu.au<br/>\r\nAnnalese Alvarez, alva0033@flinders.edu.au<br/>\r\nAccacia Verco, verc0021@flinders.edu.au<br/>\r\nMatthew Donnellan, donn0092@flinders.edu.au<br/>\r\n\r\n',
      long_description_content_type='text/markdown',
      author='Robert Piovesan',
      author_email='piov0007@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S2FLN1/', package='docassemble.LLAW33012021S2FLN1'),
     )

