from models.request import CgiRequest
import sys, json, io, datetime

class DiscountController :

    def __init__(self, request: CgiRequest):
        self.request = request

    def serve(self) :
        self.response = RestResponse(
                meta=RestMeta(
                    service="User API",
                    requestMethod=self.request.request_method,
                    links={
                        "get": "GET /discount",
                        "post": "POST /discount",
                    }
                )
            )

        action = "do_" + self.request.request_method.lower()
        controller_action = getattr(self, action, None)

        if controller_action:
            controller_action()
        else:
            self.response.status = RestStatus.status405
    

        print("Content-Type: application/json; charset=utf-8")
        print()

        print(json.dumps(self.response, default=lambda o: o.__dict__, ensure_ascii=False))
