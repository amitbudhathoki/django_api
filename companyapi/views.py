from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends=[
        'amit',
        'suraj'
    ]
    return JsonResponse(friends,safe = False)