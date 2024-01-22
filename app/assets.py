from flask_assets import Environment, Bundle

assets = Environment()

css = Bundle(
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
    "style.css"
)

js = Bundle(
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js",
    "site.js"
)

assets.register("css_all", css)
assets.register("js_all", js)