from .util.register import module_register_factory

core_modules = [
    'ui'
]

register_core, unregister_core = module_register_factory(__package__, core_modules)
