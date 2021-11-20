from django.shortcuts import render
from django.http import HttpResponse
from fusioncharts import FusionCharts

def chart(request):
   chartObj = FusionCharts( 'angulargauge', 'ex1', '600', '400', 'chart-1', 'json', """{
  "chart": {
    "caption": "Nordstorm's Customer Satisfaction Score for 2017",
    "lowerlimit": "0",
    "upperlimit": "100",
    "showvalue": "1",
    "numbersuffix": "%",
    "theme": "fusion",
    "showtooltip": "0"
  },
  "colorrange": {
    "color": [
      {
        "minvalue": "0",
        "maxvalue": "50",
        "code": "#F2726F"
      },
      {
        "minvalue": "50",
        "maxvalue": "75",
        "code": "#FFC533"
      },
      {
        "minvalue": "75",
        "maxvalue": "100",
        "code": "#62B58F"
      }
    ]
  },
  "dials": {
    "dial": [
      {
        "value": "81"
      }
    ]
  }
}""")
   return render(request, 'index.html', {'output': chartObj.render()})
