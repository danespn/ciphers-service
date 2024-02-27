from django.http import JsonResponse

def greetings(request):
    result = {"message": "Welcome to the ciphers service"}
    return JsonResponse(result)