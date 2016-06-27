#!/usr/bin/env python

import webapp2


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
        	<html>
        	<head><title>Word Machine</title></head>
        	<body>
        	 <h1>Word Machine</h1>
	          <form action="" method="post">
	        	<input type="text" name="first"><br>
	        	<input type="text" name="second"><br>
	        	<p><input type="submit" value="Magic!"></p>
	          </form>
        	</body>
        	</html>""")

class Merge(webapp2.RequestHandler):
	def post(self):
		a = self.request.get("first")
		b = self.request.get("second")
		res = """<html><body>
				{}
				</body></html>""".format(a+b)
		self.response.headers["Content-Type"] = "text/html"
		self.response.write(res)

routes = [('/', MainPage),('/magic', Merge)]

my_app = webapp2.WSGIApplication(routes, debug=True)