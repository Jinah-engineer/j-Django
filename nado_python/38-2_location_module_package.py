import inspect
import random

from nado_python.package import thailand

print(inspect.getfile(random))

from package import *
print(inspect.getfile(thailand))