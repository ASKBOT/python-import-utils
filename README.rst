Utility functions for loading modules,
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
