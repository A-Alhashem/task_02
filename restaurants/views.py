from django.shortcuts import render

# Create your views here.
def myview(request):
	context = {
	"msg": "Hello World!"
	}
	return render(request, "my_test.html", context)