from models.request import CgiRequest
import sys, json, io

class UserController:

    def __init__(self, request: CgiRequest):
        self.request = request

    def serve(self):
        # нормальная кодировка stdout
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

        print("Content-Type: application/json; charset=utf-8")


        # получаем HTTP метод (GET/POST)
        method = getattr(self.request, "REQUEST_METHOD", "GET").upper()

        # роутинг по HTTP методу
        if method == "GET":
            self.do_get()
            return

        if method == "POST":
            self.do_post()
            return

        # если метод не поддерживается
        print("Status: 405 Method Not Allowed")
        print("Content-Type: text/plain; charset=utf-8")
        print()
        print("Method not allowed")

    # =====================
    # ACTIONS
    # =====================

    def do_get(self):
        data = {
            "int": 10,
            "float": 1e-3,
            "str": "Hello",
            "cyr": "Вітання"
        }

        print("Content-Type: application/json; charset=utf-8")
        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_post(self):
        data = {
            "int": 10,
            "float": 1e-3,
            "str": "POST",
            "cyr": "Вітання"
        }

        print("Content-Type: application/json; charset=utf-8")
        print()
        print(json.dumps(data, ensure_ascii=False))

    def index(self):
        print("Content-Type: text/html; charset=utf-8")
        print()
        print("<h1>User Controller — index()</h1>")
