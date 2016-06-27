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
	          <form action="" method="post" action="/magic">
	        	<input type="text" name="first"><br>
	        	<input type="text" name="second"><br>
	        	<p><input type="submit" value="Magic!"></p>
	          </form>
        	</body>
        	</html>""")

class Merge(webapp2.RequestHandler):
	def post(self):
		a = self.request.get('first')
		b = self.request.get('second')
		c = ''
		i = 0
		while i < max(len(a),len(b)):
			if not a[i]:
				c = c + b[i]
			elif not b[i]:
				c = c + a[i]
			else:
				c = c + a[i] + b[i]
			i+=1
		res = """<html><body>
				{}
				</body></html>""".format(c)
		self.response.headers["Content-Type"] = "text/html"
		self.response.out.write(res)

routes = [('/', MainPage),('/magic', Merge)]

my_app = webapp2.WSGIApplication(routes, debug=True)