from models.request import CgiRequest
import sys, json, io

class OrderController:

    def __init__(self, request: CgiRequest):
        self.request = request

    def serve(self):
        print("Content-Type: application/json; charset=utf-8")

        method = getattr(self.request, "REQUEST_METHOD", "GET").upper()

        if method == "GET":
            return self.do_get()
        if method == "POST":
            return self.do_post()
        if method == "PUT":
            return self.do_put()
        if method == "PATCH":
            return self.do_patch()
        if method == "DELETE":
            return self.do_delete()

        print("Status: 405 Method Not Allowed")
        print("Content-Type: text/plain; charset=utf-8")
        print()
        print("Method not allowed")

    # =====================
    # HTTP METHODS
    # =====================

    def do_get(self):
        data = {
            "method": "GET",
            "message": "Отримано дані",
            "sample": [1, 2, 3],
        }

        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_post(self):
        data = {
            "method": "POST",
            "message": "Створено новий ресурс",
        }

        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_put(self):
        data = {
            "method": "PUT",
            "message": "Ресурс повністю оновлено",
        }

        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_patch(self):
        data = {
            "method": "PATCH",
            "message": "Ресурс частково оновлено",
        }

        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_delete(self):
        data = {
            "method": "DELETE",
            "message": "Ресурс видалено",
        }

        print()
        print(json.dumps(data, ensure_ascii=False))

    # опційно
    def index(self):
        print("Content-Type: text/html; charset=utf-8")
        print()
        print("<h1>Order API Controller</h1>")
