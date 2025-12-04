from models.request import CgiRequest
import sys, json, io

class UserController:

    def __init__(self, request: CgiRequest):
        self.request = request

    def serve2(self):
        
        print("Content-Type: application/json; charset=utf-8")

        method = self.request.server.get("REQUEST_METHOD", "GET").upper()

        if method == "GET":
            self.do_get()
            return

        if method == "POST":
            self.do_post()
            return

        print("Status: 405 Method Not Allowed")
        print("Content-Type: text/plain; charset=utf-8")
        print()
        print("Method not allowed")


    def serve(self) :
        # шукаємо в об'єкті метод action та виконуємо його
        action = "do_" + self.request.request_method.lower() 
        controller_action = getattr(self, action, None)
        if controller_action :
            controller_action()
        else :
            print("Status: 405 Method Not Allowed\n")

    def do_get(self):
        data = {
            "int": 10,
            "float": 1e-3,
            "str": "GET",
            "cyr": "Вітання",
            "headers": self.request.headers
        }

        print("Content-Type: application/json; charset=utf-8")
        print()
        print(json.dumps(data, ensure_ascii=False))

    def do_post(self):
        data = {
            "int": 10,
            "float": 1e-3,
            "str": "POST",
            "cyr": "Вітання",
            "headers": self.request.headers
        }
        
        print("Content-Type: application/json; charset=utf-8")
        print()
        print(json.dumps(data, ensure_ascii=False))

        # sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n\n")
        # sys.stdout.buffer.write(json.dumps(data, ensure_ascii=False))

    def index(self):
        print("Content-Type: text/html; charset=utf-8")
        print()
        print("<h1>User Controller — index()</h1>")
