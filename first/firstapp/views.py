from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Question
from django.urls import reverse
from .models import Choice, Question
from firebase import firebase
'''
def tail(request):
    
    #return HttpResponse("Hello")
    return render(request, 'firstapp/indexx.html')'''


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
   
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'firstapp/page1.html', context)





def detail(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'firstapp/indexx.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# Create your views here.
        
def thanks(request):
    #list = get_object_or_404 ( Choice, pk=choice_id)
    if request.method == 'POST' :
        x = request.POST.get('choice')
        x=int(x)
        table=Choice.objects.all().values_list()
        for e in table:
            if int(e[0])==x:
                print("match")
                print(e[0])
                t = Choice.objects.get(id=x)
                t.votes += 1
                t.save()

                # this will update only
            #print(e.vote)
            
        return render(request, 'firstapp/page3.html')
def loady(request):
    fir = firebase.FirebaseApplication('https://bult-c8c04.firebaseio.com', None)
    """if opt == 'loadyes':"""
    fir.patch('/seats/A1',{'seated':True})
    """if opt == 'loadno':
        fir.patch('/seats/A1',{'seated':False})"""
        
    return HttpResponse('I love Sk')
        
def loadn(request):
    fir = firebase.FirebaseApplication('https://bult-c8c04.firebaseio.com', None)
    """if opt == 'loadyes':"""
    fir.patch('/seats/A1',{'seated':False})
    fir.patch('/seats/A1',{'hand_raise':False})
    """if opt == 'loadno':
        fir.patch('/seats/A1',{'seated':False})"""
        
    return HttpResponse('I love mishu')
        
    
def fire(request,key):
    fir = firebase.FirebaseApplication('https://bult-c8c04.firebaseio.com', None)
    result = fir.get('/seats/A1/', None)
    print(result)
    if key=='#':# and result['seated'] == True):
        
        if result['hand_raise']== True:
            print("hvdisj")
            fir.patch('/seats/A1',{'hand_raise':False})
        elif result['hand_raise'] == False and result['seated'] == True:
            fir.patch('/seats/A1',{'hand_raise':True})
    
       #r={'emergency': False, 'hand_raise': True, 'seated': True, 'x': 1, 'y': 1}

    if key=='*':
        if result['emergency']==True:
            fir.patch('/seats/A1',{'emergency':False})
        else:
            fir.patch('/seats/A1',{'emergency':True})
        
    
    return HttpResponse("I love RB")
    