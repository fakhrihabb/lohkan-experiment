from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_book(request):
    if request.method == "POST":
        ISBN = request.POST.get('ISBN')
        BookTitle = request.POST.get('BookTitle')
        BookAuthor = request.POST.get('BookAuthor')
        Year_Of_Publication = request.POST.get('Year_Of_Publication')
        Publisher = request.POST.get('Publisher')
        Image = request.POST.get('Image')

        new_book = Katalog(ISBN=ISBN, BookTitle=BookTitle, BookAuthor=BookAuthor,
                           Year_Of_Publication=Year_Of_Publication, Publisher=Publisher, Image=Image)
        new_book.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()