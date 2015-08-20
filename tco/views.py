from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import QuestionsForm

# Create your views here.
def home(request):
	form = QuestionsForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()

	return render_to_response("main.html", locals(), 
		context_instance = RequestContext(request))

def aboutus(request):

	return render_to_response("aboutus.html", locals(),
	 context_instance = RequestContext(request))
