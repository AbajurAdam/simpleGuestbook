from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
# Create your views here.


def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'guestbook/index.html', context)


def sign(request):

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(
                name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment successfully added.')

            return redirect('index')
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'guestbook/sign.html', context)
