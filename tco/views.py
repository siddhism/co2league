from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from .forms import *
from .coolClimate import *
from .models import Result
# from instagram.client import InstagramAPI

# import sample_app as Insta


def first_screen(request):
	# user_data = Insta.home()
	url = 'https://api.instagram.com/oauth/authorize/?client_id=6aeb81a251d948e181cd794232c65f8a&redirect_uri=http://localhost:8000/oauth_callback&response_type=token'
	return render_to_response("first_screen.html", locals(),
	 context_instance = RequestContext(request))

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
		data["input_footprint_transportation_publictrans"] = save_it.input_footprint_transportation_publictrans
		data["input_footprint_transportation_airtotal"] = save_it.input_footprint_transportation_airtotal
		data["input_footprint_housing_squarefeet"] = save_it.input_footprint_housing_squarefeet
		data["input_footprint_shopping_goods_total"] = save_it.input_footprint_shopping_goods_total
		data["input_footprint_shopping_services_total"] = save_it.input_footprint_shopping_services_total
		
		# global result_grand_total
		result_grand_total = coolclimate(data)
		return render_to_response("aboutus.html",
			locals(),
		 context_instance=RequestContext(request))

	return render_to_response("main.html", locals(),
			context_instance = RequestContext(request))

def travel(request):
	form = Travel_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		# data["input_footprint_transportation_miles1"] = save_it.input_footprint_transportation_miles1
		# data["input_footprint_transportation_mpg1"] = save_it.input_footprint_transportation_mpg1
		# data["input_footprint_transportation_fuel1"] = save_it.input_footprint_transportation_fuel1
		# data["input_footprint_transportation_miles2"] = save_it.input_footprint_transportation_miles2
		# data["input_footprint_transportation_mpg2"] = save_it.input_footprint_transportation_mpg2
		# data["input_footprint_transportation_fuel2"] = save_it.input_footprint_transportation_fuel2
		# data["input_footprint_transportation_publictrans"] = save_it.input_footprint_transportation_miles1
		# data["input_footprint_transportation_airtotal"] = save_it.input_footprint_transportation_airtotal
		# HttpResponseRedirect('/food')
		return render_to_response('food.html',
			locals(),
		 context_instance=RequestContext(request))
	
	return render_to_response("travel.html", locals(),
		context_instance = RequestContext(request))

def food(request):
	form = Food_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		# data["input_footprint_housing_electricity_type"] = save_it.input_footprint_housing_electricity_type
		# data["input_footprint_housing_cleanpercent"] = save_it.input_footprint_housing_cleanpercent
		# data["input_footprint_housing_naturalgas_type"] = save_it.input_footprint_housing_naturalgas_type
		# data["input_footprint_housing_naturalgas_dollars"] = save_it.input_footprint_housing_naturalgas_dollars
		# data["input_footprint_housing_heatingoil_type"] = save_it.input_footprint_housing_heatingoil_type
		# data["input_footprint_housing_heatingoil_dollars"] = save_it.input_footprint_housing_heatingoil_dollars
		# data["input_footprint_housing_heatingoil_gallons"] = save_it.input_footprint_housing_heatingoil_gallons
		# data["input_footprint_housing_heatingoil_dollars_per_gallon"] = save_it.input_footprint_housing_heatingoil_dollars_per_gallon
		# data["input_footprint_housing_squarefeet"] = save_it.input_footprint_housing_squarefeet
		# data["input_footprint_housing_watersewage"] = save_it.input_footprint_housing_watersewage
		# HttpResponseRedirect('/housing/')
		return render_to_response('travel.html',
			locals(),
		 context_instance=RequestContext(request))
	
	return render_to_response("food.html", locals(),
		context_instance = RequestContext(request))

def housing(request):
	form = Housing_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		# data["input_footprint_shopping_food_meatfisheggs_default"] = save_it.input_footprint_shopping_food_meatfisheggs_default
		# data["input_footprint_shopping_food_dairy_default"] = save_it.input_footprint_shopping_food_dairy_default
		# data["input_footprint_shopping_food_fruitvegetables_default"] = save_it.input_footprint_shopping_food_fruitvegetables_default
		# data["input_footprint_shopping_food_cereals"] = save_it.input_footprint_shopping_food_cereals
		# data["input_footprint_shopping_food_otherfood"] = save_it.input_footprint_shopping_food_otherfood
		# HttpResponseRedirect('/shopping/')
		return render_to_response('travel.html',
			locals(),
		 context_instance=RequestContext(request))
	
	return render_to_response("housing.html", locals(),
		context_instance = RequestContext(request))

def shopping(request):
	form = Shopping_questionsForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit = False)
		save_it.save()
		# data["input_footprint_shopping_goods_type"] = save_it.input_footprint_shopping_goods_type
		# data["input_footprint_shopping_goods_total"] = save_it.input_footprint_shopping_goods_total
		# data["input_footprint_shopping_services_type"] = save_it.input_footprint_shopping_services_type
		# data["input_footprint_shopping_services_total"] = save_it.input_footprint_shopping_services_total
		# global result_grand_total
		# result_grand_total = result_grand_total
		# HttpResponseRedirect('/aboutus/')
		# print result_grand_total
		return render_to_response("aboutus.html",
			locals(),
		 context_instance=RequestContext(request))

	return render_to_response("shopping.html", locals(),
		context_instance = RequestContext(request))

def aboutus(request):
	return render_to_response("aboutus.html", locals(),
	 context_instance = RequestContext(request))

# def first_screen(request):
# 	data = sample_app.home()
# 	access_token = "YOUR_ACCESS_TOKEN"
# 	client_secret = "YOUR_CLIENT_SECRET"
# 	api = InstagramAPI(access_token=access_token, client_secret=client_secret)
# 	recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
# 	for media in recent_media:
#    		print media.caption.text
# 	return render_to_response("first_screen.html", locals(),
# 	 context_instance = RequestContext(request))

def user_start(request):
	return render_to_response("user_start.html", locals(),
	 context_instance = RequestContext(request))

