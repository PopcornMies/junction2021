import plotly.graph_objects as go
import plotly.express as px

val = 82
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
            {'range': [0, 50], 'color': '#e15454'},
            {'range': [50, 100], 'color': '#77cc66'}]}))
picker_style = {'float': 'left', 'margin': 'auto'}

fig.update_layout(paper_bgcolor = "white", font = {'color': "#050038", 'size': 18, 'family': "Open+Sans:wght@900",})
fig.show()
fig.write_html("C:/Users/Mikko Pajula/junction/junction-332712/templates/file.html")
