# Create your views here.
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
sentiment = 54.2

def graph_view(request):
    val = sentiment
    bar = '#050038'
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Meeting positivity score", 'font': {'size': 18}},
        gauge = {
            'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "#050038"},
            'bar': {'color': bar},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "white",
            'steps': [
                {'range': [0, 20], 'color': '#f94144'},
                {'range': [20, 40], 'color': '#f3722c'},
                {'range': [40, 60], 'color': '#f8961e'},
                {'range': [60, 80], 'color': '#f9c74f'},
                {'range': [80, 100], 'color': '#90be6d'}]}))
    graph = fig.update_layout(paper_bgcolor = "white", font = {'color': "#050038", 'size': 18, 'family': "Open+Sans:wght@900",})
    graph = fig.to_html(full_html=False, default_height=500, default_width=500)
    context = {'graph': graph}
    return render(request, 'main.html', context)

def test_view(request):
    test = 'this is a test'
    context = {'test': test}
    return render(request, 'main.html', context)
