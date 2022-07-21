
import sys
# get a list of the built-in module names 
modules = sys.builtin_module_names

# loop over module names
for module in modules:

    if not module.startswith("_"):
     print(module)