from app.listener import views


def setup_routes(app):
    app.router.add_get("/", views.index)
    app.router.add_post("/", views.post)
    app.router.add_post("/ISAPI/Event/notification/httpHosts", views.post)
