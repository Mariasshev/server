from models.request import CgiRequest
import sys, json, io, datetime

class RestStatus :
    def __init__(self, is_ok: bool, code:int, message: str):
        self.is_ok = is_ok
        self.code = code
        self.message = message

    def to_json(self) :
        return {
            "isOk": self.is_ok,
            "code": self.code,
            "message": self.message,
        }

RestStatus.status200 = RestStatus(True, 200, "OK")
RestStatus.status405 = RestStatus(False, 405, "Method Not Allowed")


class RestCache :
    def __init__(self, exp:str|int|None=None, lifetime:int|None=None):
        self.exp = exp
        self.lifetime = lifetime

    
    def to_json(self) :
        return {
            "exp": self.exp,
            "lifetime": self.lifetime,
            "units": "seconds",
        }

RestCache.no = RestCache()
RestCache.hrs1 = RestCache(lifetime=60*60)



class RestMeta :
    def __init__(self, service:str, requestMethod:str, dataType:str="null", 
                 cache:RestCache=RestCache.no, authUserId:str|int|None=None,
                 serverTime:int|None=None, params:dict|None=None, links:dict|None=None ):
        self.service = service
        self.requestMethod = requestMethod
        self.authUserId = authUserId
        self.dataType = dataType
        self.cache = cache
        self.serverTime = serverTime if serverTime!= None else datetime.datetime.now().timestamp()
        self.params = params
        self.links = links


    def to_json(self) :
        return {
            "service": self.service,
            "requestMethod": self.requestMethod,
            "dataType": self.dataType,
            "cache": self.cache.to_json(),
            "authUserId": self.authUserId,
            "serverTime": self.serverTime,
            "params": self.params,
            "links": self.links,
        }


class RestResponse :
    def __init__(self, meta:RestMeta, 
                 status: RestStatus=RestStatus.status200,
                 data:any=None):
        self.status = status
        self.meta = meta
        self.data = data

    def to_json(self) :
        return {
            "status": self.status,
            "meta": self.meta,
            "data": self.data,
        }



class UserController:

    def __init__(self, request: CgiRequest):
        self.request = request


    def serve(self):
        try:
            self.response = RestResponse(
                meta=RestMeta(
                    service="User API",
                    requestMethod=self.request.request_method,
                    links={
                        "get": "GET /user",
                        "post": "POST /user",
                    }
                )
            )

            action = "do_" + self.request.request_method.lower()
            controller_action = getattr(self, action, None)

            if controller_action:
                controller_action()
            else:
                self.response.status = RestStatus.status405


        # sys.stdout.buffer.write(b"Content-Type: application/json; charset=utf-8\n\n")
        # sys.stdout.buffer.write(
        #     json.dumps(self.response, 
        #                ensure_ascii=False, 
        #                default=str)
        #     .encode())

        except Exception as e:
            self.response.status = RestStatus(False, 500, str(e))
            self.response.data = None

        print("Content-Type: application/json; charset=utf-8")
        print()

        # print(json.dumps(self.response, ensure_ascii=False, default=lambda x: x.to_json if hasattr(x, 'to_json') else x.__dict__))

        print(json.dumps(self.response, default=lambda o: o.__dict__, ensure_ascii=False))




    def do_get(self):
        self.response.meta.service += ": authentication"
        self.response.meta.cache = RestCache.hrs1
        self.response.meta.dataType = "object"
        self.response.data = {
            "int": 10,
            "float": 1e-3,
            "str": "GET",
            "cyr": "Вітання",
            "headers": self.request.headers
        }


    def do_post(self):
        self.response.meta.service += ": registration"
        self.response.meta.cache = RestCache.hrs1
        self.response.meta.dataType = "object"
        self.response.data = {
            "int": 10,
            "float": 1e-3,
            "str": "POST",
            "cyr": "Вітання",
            "headers": self.request.headers
        }
    

    def index(self):
        print("Content-Type: text/html; charset=utf-8")
        print()
        print("<h1>User Controller — index()</h1>")
