from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Memo


def index(request):
    memo_list = Memo.objects.all()
    context = {'memo_list': memo_list}
    return render(request, 'memos/index.html', context)


def detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memos/detail.html', {'memo': memo})


def insert(request):
    memo = Memo.objects.create(text=request.POST["memo"])
    memo.save()

    index_url = reverse("index")
    return redirect(index_url)
