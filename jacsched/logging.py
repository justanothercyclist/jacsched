from jacsched import jacsched

def debugOutput( s ):
	# TODO: Do more than print
	if 'INTERNAL_DEBUG' in jacsched.config.keys():
		if not jacsched.config['INTERNAL_DEBUG']:
			return

	print s
	return
