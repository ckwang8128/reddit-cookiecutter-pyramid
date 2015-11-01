#!/usr/bin/python

print("""Congrats! Your baseplate pyramid project is ready to go!

Next steps:

Install it

    python setup.py develop --user

Start up the application

    baseplate-serve2 --debug example.ini

If you interact with any thrift services, put their .thrift file in your
application package and run "setup.py build". This will generate the
client code for that service.

""")
