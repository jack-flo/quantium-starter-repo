# app.py
import dash
import dash.html as html

app = dash.Dash(__name__)
app.layout = html.H1("Hello, Quantium!")

if __name__ == "__main__":
    app.run(debug=True)
