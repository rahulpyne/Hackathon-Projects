from django.shortcuts import render
from django.http import HttpResponse
from foodbud.models import Meals
# Create your views here.
price_item= {}
calories_item = {}
def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def initialInfo(request):
    if request.method=='GET': #This is to load the page first time with all the fields.
        return render(request,'initial-info.html')
    elif request.method == 'POST': #this is to load the same page with all the results
        list_of_objs = Meals.objects.all()
        if request.POST.get('preference','').encode('utf8') == 'Yes':
            list_of_objs = filter(lambda x: x.category == 'veg', list_of_objs) # filters the list_of_objs with only those objects which contain veg category.
        for meal in list_of_objs:
            price_item.update({meal.item_name.encode('utf8'):meal.price})
            calories_item.update({meal.item_name.encode('utf8'):meal.calories})
        set_of_food_combos = []
        per_day = float(request.POST.get('budget',''))/float(request.POST.get('days',''))
        for value in make_food_combos(price_item,price_item.keys(),per_day-5,per_day,0): # returns all the possible combos
            if len(set_of_food_combos) <=1000: #to make it feasable keeping the list of combos less than 1000
                if value not in set_of_food_combos and len(value)>=3: #allowing non-reapative combos and should have atleast 3 meals in it.
                    set_of_food_combos.append(value)
            else:
                break
        calories_fit_combos=[] # will maintain only those combos which are within the calorie range.
        print request.POST.get('Age','').encode('utf8')
        print request.POST.get('gender','').encode('utf8')
        for value in set_of_food_combos:
            if(valid_calories(request.POST.get('gender','').encode('utf8'),int(request.POST.get('Age','')),value,calories_item)):
                calories_fit_combos.append(value)
        return render(request,"meal_plan.html",{'list_of_content':calories_fit_combos})



# returns boolean about whether the given calorie count of a combo
# is within the range of required calories per day based on the gender, age.
def calorie_fitness(gender,age,calorie):
    if gender=='male':
        if (age in range(14,19) and calorie>=3200) or (age in range(18,24) and calorie>=3400) or \
                (age in range(23,31) and calorie>=3300) or (age in range(30,36) and calorie>=3000):
                return True
        else:
            return False
    if gender=='female':
        if (age in range(14,19) and calorie>=2400) or (age in range(18,24) and calorie>=2600) or \
                (age in range(23,31) and calorie>=2700) or (age in range(30,36) and calorie>=2200):
                return True
        else:
            return False


def valid_calories(gender,age,list_of_items,calories_item):
    calori = 0
    for item in list_of_items:
        calori+=calories_item[item]
    return calorie_fitness(gender,age,calori)

# makes all the possible combos using the generator method
# implements sum subset algorithm.
# upper bound and lower_bound defines the range of amount in which the sum should be.
# food_dict contains all the food items and its prices.
# key_list contains the list of all keys of food_dict
def make_food_combos(food_dict,key_list,lower_bound,upper_bound,sum):
    if upper_bound == 0: # returns control directly because the upper bound is too less to consider.
        return
    if lower_bound <= sum <= upper_bound: # giving a relaxation of range for the sum to be in. Out here its 5$
        yield[]
    if sum > upper_bound or not key_list:
        return
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum + food_dict[key_list[0]]):
        yield [key_list[0]] + solution
    for solution in make_food_combos(food_dict,key_list[1:], lower_bound, upper_bound,sum):
        yield solution

def login(request):
	return render(request,"login.html")
