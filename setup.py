from setuptools import setup, Extension

crp_yespower_1_0_module = Extension('crp_yespower_1_0',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'crp_yespower_1_0',
       version = '1.0.0',
       author_email = 'cryptomorpher@gmail.com',
       author = 'Morpher',
       url = 'https://github.com/MorphBC/crp_yespower_1_0_python3',
       description = 'Bindings for yespower-1.0 proof of work used by CranePay',
       ext_modules = [crp_yespower_1_0_module])
