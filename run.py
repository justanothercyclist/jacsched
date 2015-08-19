#!/flask/bin/python

from jacsched import jacsched

jacsched.config['INTERNAL_DEBUG'] = True

jacsched.run( host='0.0.0.0', port=10812, debug = True )