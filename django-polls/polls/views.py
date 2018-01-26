# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Choice, Question
# Create your views here.
# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template("polls/index.html")
# 	context = {
# 		'latest_question': latest_question_list,
# 	}
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#  #    try:
#  #    	question = Question.objects.get(pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist")
# 	# context = {
# 	# 	'question': question
# 	# }
# 	# return render(request, 'polls/detail.html', context)
# 	question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#     	selected_choice = question.choice_set.get(pk=request.POST['choice'])
# 	except (keyError, Choice.DoesNotExist):
# 		return render(request, 'polls/detail.html', {
# 			'question': question,
# 			'error_message': "you didn't selected a choice.",
# 			})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		# return Question.objects.order_by('-pub_date')[:5]
		return Question.objects.filter(
				pub_date__lte = timezone.now()
			).order_by('-pub_date')[:5]

# Question.objects.filter(pub_date__lte=timezone.now()) returns a queryset containing Questions whose pub_date is less than or equal to - that is, earlier than or equal to - timezone.now.

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

	def get_queryset(self):

		return Question.objects.filter(pub_date__lte= timezone.now())


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (keyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "you didn't selected a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
