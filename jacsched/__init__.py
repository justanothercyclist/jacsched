from flask import Flask
import pprint

jacsched = Flask(__name__, instance_relative_config=True)

import logging
logging.debugOutput( 'Initializing ' + __name__ )


### DEBUG / DEV Only
pp = pprint.PrettyPrint( indent=2 )
pp.pprint( jacsched.config )


from jacsched import routes