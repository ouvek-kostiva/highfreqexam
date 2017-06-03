from django.shortcuts import render
from stockplot.forms import StockForm
from stockplot.models import Twse

# Create your views here.

def index(request):
    if request.method == 'GET':
        form = StockForm(request.GET)
        if form.is_valid():
           startdate = form.cleaned_data['startdate']
           enddate = form.cleaned_data['enddate']
           codeid = form.cleaned_data['codeid']
           prices = Twse.objects.filter(code=codeid).filter(date__range=(startdate,enddate))
           dates = Twse.objects.values_list('date', flat=True).filter(code=codeid).filter(date__range=(startdate,enddate))
           dates = [date[0:10] for date in dates]
           #return render(request, 'stockplot/plotCode.html', {'code':[codeid],'date':[startdate, enddate]})
        else:
            form = StockForm()
    return render(request, 'stockplot/plot.html', locals())
    #return render(request, 'stockplot/plot.html', {'code':['1101'],'date':['2016-05-26','2017-05-26']})
    
# def byCode(request, codeid):
#     if request.method == 'GET':
#         forms = StockForm(request.GET)
#         if form.is_valid():
#           startdate = request.GET.get('startdate', '2016-05-26')
#           enddate = request.GET.get('enddate', '2017-05-26')
#           prices = Twse.objects.get(code=codeid)
#           forms = StockForm(request.GET,initial=[codeid,startdate,enddate])
#           #return render(request, 'stockplot/plotCode.html', {'code':[codeid],'date':[startdate, enddate]})
#         else:
#             forms = StockForm()
#     return render(request, 'stockplot/plotCode.html', {'forms': forms, 'prices':prices})
    
def about(request):
    return render(request, 'stockplot/about.html')