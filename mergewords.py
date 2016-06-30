#!/usr/bin/env python

import webapp2

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.out.write("""
        	<html>
        	<head><title>Word Machine</title></head>
        	<body>
        	 <h1>Word Machine</h1>
	          <form method="post" action="/magic">
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
				<h2>{}</h2>
				<img src="http://s.quickmeme.com/img/1e/1e316e8b30384c27aa347055973c419a658e6673e630d193304482261ef5de28.jpg" alt="Magic" style="width:304px;height:228px;">
				</body></html>""".format(c)
		self.response.headers["Content-Type"] = "text/html"
		self.response.out.write(res)

routes = [('/', MainPage),('/magic', Merge)]

my_app = webapp2.WSGIApplication(routes, debug=True)