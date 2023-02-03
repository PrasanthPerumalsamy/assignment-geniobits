from django.shortcuts import render
import csv
from django.core.files import File
import json
from django.http import HttpResponse

from MainApp.models import CsvFile
from constructor.candle_constructor import Candle, SingleCandle
# Create your views here.

def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        csv_file = File(csv_file)
        uploaded_csv = CsvFile(file=csv_file)
        uploaded_csv.save()
        timeframe = request.POST.get('timeframe')
        
        # Convert the timeframe string to a int object
        row_count = int(timeframe)
        
        #reading the file and doing operations
        reader = csv.reader(uploaded_csv.file.read().decode('utf8').splitlines())
        result = []
        id_counter = 0
        next(reader)
        for row in reader:
            if id_counter == row_count:
                break
            id_counter += 1
            nifty,date,time,open,high,low,close,volume = row
            candle = Candle(id_counter,open,high,low,close,date,volume)

            result.append(candle)

        #geting only needed data as per requirement
        open_value = result[0].open
        close_value = result[-1].close
        volume = result[-1].volume
        high_value = max(candle.high for candle in result)
        low_value = min(candle.low for candle in result)
        
        #passing data points to single object constructor
        single_candle = SingleCandle(open=open_value, close=close_value, high=high_value, low=low_value, volume=volume)
        json_data = json.dumps(single_candle, default=lambda x: x.__dict__)
        
        #convert object to json and downloading
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="data.json"'
        return response
        
    return render(request, 'upload.html')

