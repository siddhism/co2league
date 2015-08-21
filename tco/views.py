from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import *
from .coolClimate import *
from .models import Result

# Create your views here.
def home(request):
	form = QuestionsForm(request.POST or None)
	result_grand_total = ""
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		data = {}
		data["input_location"] = save_it.input_location
		data["input_income"] = save_it.input_income
		data["input_location_mode"] = save_it.input_location_mode
		data["input_size"] = save_it.input_size
		# result_grand_total = coolclimate(data)
		HttpResponseRedirect('/travel')
		# return render_to_response('travel.html', 
		# 	locals(),
		#  context_instance=RequestContext(request))
	return render_to_response("main.html", locals(), 
			context_instance = RequestContext(request))

def travel(request):
	form = Travel_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		HttpResponseRedirect('/food')
	return render_to_response("travel.html", locals(), 
		context_instance = RequestContext(request))

def food(request):
	form = Food_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		HttpResponseRedirect('/housing/')
	return render_to_response("food.html", locals(), 
		context_instance = RequestContext(request))

def housing(request):
	form = Housing_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		HttpResponseRedirect('/shopping/')
	return render_to_response("housing.html", locals(), 
		context_instance = RequestContext(request))

def shopping(request):
	form = Shopping_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		# HttpResponseRedirect('../about-us/')
		result_grand_total = coolclimate(data)
	return render_to_response("aboutus.html", locals(), 
		context_instance = RequestContext(request))



def aboutus(request):
	return render_to_response("aboutus.html", locals(),
	 context_instance = RequestContext(request))
