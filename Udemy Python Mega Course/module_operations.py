# import entire module
import example

# display module's doc (help) file
example.__doc__

from example import function1

example.function2.__doc__

# import mkdir function from os module

from os import mkdir

mkdir('test')
mkdir.__doc__

# reload already imported module
import importlib
importlib.reload(example)