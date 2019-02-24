from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
import json

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route("/")
def get():
    return "<h1>Hi</h1>"


# @api.route("/data")
# class Scraper(Resource):
#     def get(self):
#         orgs = scrape()
#         return {"pages": orgs["pages"], "urls": orgs["urls"]}


# @api.route("/page", methods=["POST"])
# class Scraper(Resource):
#     def post(self):
#         org = scrape_page((json.loads(request.json))["url"])
#         print(org)
#         return {"data": org}


# @api.route("/test")
# class ScraperVietnam(Resource):
#     def get(self):
#         org = scrape(one=True)
#         return {"test": org[0]}


if __name__ == "__main__":
    app.run(debug=True)
