from flask import Flask, render_template

app = Flask(__name__)

# Data from Table 1
table1 = [
    {'Index': 'A1', 'Value': 41},
    {'Index': 'A2', 'Value': 18},
    {'Index': 'A3', 'Value': 21},
    {'Index': 'A4', 'Value': 63},
    {'Index': 'A5', 'Value': 2},
    {'Index': 'A6', 'Value': 53},
    {'Index': 'A7', 'Value': 5},
    {'Index': 'A8', 'Value': 57},
    {'Index': 'A9', 'Value': 60},
    {'Index': 'A10', 'Value': 93},
    {'Index': 'A11', 'Value': 28},
    {'Index': 'A12', 'Value': 3},
    {'Index': 'A13', 'Value': 90},
    {'Index': 'A14', 'Value': 39},
    {'Index': 'A15', 'Value': 80},
    {'Index': 'A16', 'Value': 88},
    {'Index': 'A17', 'Value': 49},
    {'Index': 'A18', 'Value': 60},
    {'Index': 'A19', 'Value': 26},
    {'Index': 'A20', 'Value': 28}
]

# Calculated values for Table 2
alpha = 2 + 28
beta = 80 / 5
charlie = 90 * 3

table2 = [
    {'Category': 'Alpha', 'Value': alpha},
    {'Category': 'Beta', 'Value': beta},
    {'Category': 'Charlie', 'Value': charlie}
]

@app.route('/')
def index():
    return render_template('index.html', table1=table1, table2=table2)

if __name__ == '__main__':
    app.run(debug=True)
