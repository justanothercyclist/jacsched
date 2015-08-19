from flask import render_template, request, Response, jsonify, redirect
from jacsched import jacsched

@jacsched.route('/')
def mainEntry():
	print "Exec main entry\n"