from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import JsonStockData
from django.shortcuts import render
from django.core.paginator import Paginator
import json
from datetime import datetime
from .models import SqlStockData



@csrf_exempt
def update_stock_data(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)

            # Parse and reformat the date
            date_str = data['date']
            date_obj = datetime.strptime(date_str, '%b. %d, %Y')  
            formatted_date = date_obj.strftime('%Y-%m-%d')

            # Update the database entry
            #stock_entry = JsonStockData.objects.get(id=data['id'])
            stock_entry = SqlStockData.objects.get(id=data['id'])
            stock_entry.date = formatted_date
            stock_entry.trade_code = data['trade_code']
            stock_entry.high = data['high']
            stock_entry.low = data['low']
            stock_entry.open = data['open']
            stock_entry.close = data['close']  # Assuming 'close' is a field
            stock_entry.volume = data['volume']
            stock_entry.save()

            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'fail'}, status=400)
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)




# def stock_data_view(request):
#     data = JsonStockData.objects.all()  # Or however you're getting your data
#     return render(request, 'stockData/stock_table.html', {'data': data})


def stock_data_view(request):
    #data_list = JsonStockData.objects.all()
    data_list = SqlStockData.objects.all()
    paginator = Paginator(data_list, 200)  # Show 25 entries per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    
    return render(request, 'stockData/stock_table.html', {'data': data})

# In your views.py


@csrf_exempt
def delete_stock_data(request, id):
    try:
        stock_entry = SqlStockData.objects.get(id=id)
        stock_entry.delete()
        return JsonResponse({'status': 'success'})
    except SqlStockData.DoesNotExist:
        return JsonResponse({'status': 'not found'}, status=404)
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def chart_data(request, trade_code):
    data = SqlStockData.objects.filter(trade_code=trade_code).order_by('date').values('date', 'close', 'volume')
    return JsonResponse(list(data), safe=False)


def trade_codes(request):
    codes = SqlStockData.objects.values_list('trade_code', flat=True).distinct()
    return JsonResponse(list(codes), safe=False)
