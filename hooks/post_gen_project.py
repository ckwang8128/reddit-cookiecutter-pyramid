#!/usr/bin/python
import os
import fnmatch

PROJECT_DIR = os.path.realpath(os.path.curdir)

def clean_up_thrift():
    """
    Remove Thrift-only files from project.
    """
    os.unlink(os.path.join( PROJECT_DIR,
                            '{{ cookiecutter.project_name }}',
                            'thrift_init.py'))

def clean_up_pyramid():
    """
    Remove Pyramid-only files from project.
    """
    os.unlink(os.path.join( PROJECT_DIR,
                            '{{ cookiecutter.project_name }}',
                            'pyramid_init.py'))
def remap_init_file():
    # Retrieve templated init files
    module_path = os.path.join(PROJECT_DIR,
                               '{{ cookiecutter.project_name }}')
    init_files = fnmatch.filter(os.listdir(module_path), "*_init.py")

    # Raise error if there's not exactly one,
    #  that means cleanup didn't work properly.
    if len(init_files) != 1:
        raise Exception("File cleanup failed. Check %s" % module_path)
    init_file = init_files[0]

    # Rename framework template to __init__.py
    os.rename(os.path.join(module_path, init_file),
              os.path.join(module_path, "__init__.py"))

CLEAN_UP_FUNCS = {
    "pyramid": clean_up_pyramid,
    "thrift": clean_up_thrift,
}

def clean_up_templates(used_server_type):
    for server_type,clean_up_func in CLEAN_UP_FUNCS.iteritems():
        if server_type != used_server_type:
            clean_up_func()

def finalize_project():
    """
    Perform secondary file cleanup after template rendering.
    """
    clean_up_templates("{{ cookiecutter.server_type }}")
    remap_init_file()

if __name__ == "__main__":

    finalize_project()

    print("""
    Congrats! Your {{ cookiecutter.server_type }} baseplate project is ready to go!

    Next steps:

    Install it

        python setup.py develop --user

    Start up the application

        baseplate-serve2 --debug example.ini

    If you interact with any thrift services, put their .thrift file in your
    application package and run "setup.py build". This will generate the
    client code for that service.

    """)
