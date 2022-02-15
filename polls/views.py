from django.shortcuts import render, redirect
from .models import Sondage

from .forms import PollForm


def home(request):
    questions = Sondage.objects.all().order_by('-add_le')
    ctx = {
        'questions': questions
    }
    return render(request, 'home.html', ctx)

def ajouter(request):
    form = PollForm
    if request.method == 'POST':
        form = PollForm(request.POST)
        form.save()
        return redirect('home')
    ctx = {
        'form': form
    }
    return render(request, 'create.html', ctx)


class Httpesponse:
    pass


def vote(request, id=None):
    poll = Sondage.objects.get(pk=id)
    if request.method == 'POST':
       selected_option = request.POST['poll']
       if selected_option == 'option1':
           poll.count_res_1 += 1
       elif selected_option == 'option2':
           poll.count_res_2 += 1
       elif selected_option == 'option3':
           poll.count_res_3 += 1
       else:
           return Httpesponse(400, 'Erreur formulaire')

       poll.save()

       return redirect('results', poll.id)

    ctx = {
        'poll': poll
    }
    return render(request, 'vote.html', ctx)

def results(request, id=None):
    poll = Sondage.objects.get(pk=id)
    ctx = {
        'poll': poll
    }
    return render(request, 'results.html', ctx)
# Create your views here.
