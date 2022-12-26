from django.shortcuts import HttpResponse


# class Father_middleware:
#     def __init__(self, get_response):
#         print("it runs only one time when we load webpage it is father")

#         self.get_response = get_response

#     def __call__(self, request):
#         print("it is father and run before views")
#         # here we give this response it means it will go to the next views or next middleware(if present)
#         response = self.get_response(request)
#         print("it is father and it return after executing views")
#         return response


# class Mother_middleware:
#     def __init__(self, get_response):
#         print("it runs only one time when we load webpage it is mother")

#         self.get_response = get_response

#     def __call__(self, request):
#         print("it is mother and run before views")

#         # here we give this response and it will not go to the views becasue we return here httpresponse so our views will not run in this condition
#         # response = self.get_response(request)

#         print("it is mother and it return after executing views")
#         return HttpResponse("hey this page is under construction")


# class Son_middleware:
#     def __init__(self, get_response):
#         print("it runs only one time when we load webpage it is son")
#         self.get_response = get_response

#     def __call__(self, request):
#         print("it is Son and run before views")
#         # here we return this response means it will go to the views or next midddleware (if presnt) and   if we render on any template here then views will not run
#         response = self.get_response(request)
#         print("it is Son and it return after executing views")
#         return response


# here practice hooks in django middleware

# class hookes_processviews:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(request, *args, **kwargs):
#         # in this process views if we give none then it will go to the views or  next middleware (if present)
#         return None
#         # if we give HttpResponse in it then it will not go to the next middleware or views also
#         # return HttpResponse("hey it is process view and it return httpresponse instead of none ")


# class nextmdl:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_view(request, *args, **kwargs):
#         return HttpResponse("hey it is my second middleware's process view so in before we give none then it is come here")


# process_exception


# class nextmdl:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

#     def process_exception(self, request, exception):
#         class_name = exception.__class__.__name__
#         print(exception)
#         print(class_name)
#         return HttpResponse(exception)


class process_template:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print("process template response from middleware.......")
        response.context_data['name'] = "Gaurav"
        response.context_data["school"] = "svm"
        response.context_data["refern"] = "it is add from the middleware so we can give extra context data in our template "

        return response
