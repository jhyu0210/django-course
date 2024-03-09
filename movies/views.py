from django.http import HttpResponse
from django.shortcuts import render

# data = {"movies": ["movie1", "movie2"]}
data = {
    "movies": [
        {"id": 5, "title": "Jaws", "year": 1669},
        {"id": 6, "title": "Meg", "year": 1700},
        {"id": 7, "title": "Sharknado", "year": 1800},
    ]
}


def movies(request):
    # return HttpResponse("Hello there")
    return render(
        # request, "movies/movies.html", {"movies": ["movie1", "movie2", "movie3"]}
        request,
        "movies/movies.html",
        data,
    )


def home(request):
    return HttpResponse("Home Page")
