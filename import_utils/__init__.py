"""Utilities for loading modules,
supporting programmatic imports of types::

    >>>from import_utils import import_module_from, import_module
    >>>import x as mod_x
    >>>mod_x = import_module('x')
    >>>
    >>>import x.y as mod_xy
    >>>mod_xy = import_module('x.y')
    >>>
    >>>from x.y import z
    >>>z = import_module_from('x.y.z')
"""
import sys
__version__ = '0.0.1'

def import_module_from(mod_path):
    """``mod_path`` is python path to module.
    Examples:
    1) call with dotted path:
    >>>import_module_from('x.y.z')
    is equivalent to
    >>>from x.y import z

    2) call with path without dots:
    >>>import_module_from('x')
    is the same as 
    >>>import x
    """
    if '.' in mod_path:
        bits = mod_path.split('.')
        mod_name = bits.pop()
        mod_path = '.'.join(bits)
        return import_module(mod_path, mod_name)
    else:
        return import_module(mod_path)

def import_module(mod_path, mod_name = None):
    """first parameter must be
    a dotted python module path,
    second parameter is optional - module name.

    Examples:

    1) call with one parameter:

    >>>import_module('x.y.z')
    is equivalent to 
    >>>import x.y.z

    2) call with two parameters

    >>>import_module('x.y', 'z')
    is equivalent to
    >> from x.y import z

    Relative imports are not supported
    """
    if mod_name is None:
        try:
            return sys.modules[mod_path]
        except KeyError:
            __import__(mod_path)
            return sys.modules[mod_path]
    else:
        if mod_name.find('.') != -1:
            raise ValueError('second argument to import_module must not contain dots')
        mod_ = __import__(mod_path, globals(), locals(), [mod_name,], -1)
        return getattr(mod_, mod_name)
