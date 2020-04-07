from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {
        'text': 'hello world',
        'number': 1800
    }

    return render(request, 'core/index.html', context=context_dict)


def other(request):
    return render(request, 'core/other.html')


def relative(request):
    return render(request, 'core/relative_url_templates.html')
