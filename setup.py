from distutils.core import setup, Extension

module1 = Extension('goWsgi',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '0'),
                                     ('DEBUG_VERSION', '1')],
                    sources = ['goWsgimodule.c'])

setup (name = "goWsgi",
       version = '0.0.1',
       description = 'desc',
       author = 'James Calo',
       author_email = 'jamesafcalo@gmail.com',
       #url
       long_description = ''' long desc ''',
       ext_modules = [module1])
