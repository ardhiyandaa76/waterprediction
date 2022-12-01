from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        aluminium = request.form['aluminium']
        flouride = request.form['flouride']
        bacteria = request.form['bacteria']
        viruses = request.form['viruses']
        uranium = request.form['uranium']
        df = pd.read_csv('csv/waterQuality2.csv')
        x = df[['aluminium', 'flouride', 'bacteria',
               'viruses', 'uranium']].values
        y = df["is_safe"]

        # splitting the data into training and testing
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2, random_state=0)

        # DECISION treeçc
        isSafe = DecisionTreeClassifier(criterion="gini", max_depth=10)
        isSafe.fit(x_train, y_train)

        # prediction
        x_new = np.array((aluminium, flouride, bacteria, viruses, uranium))
        x_new = np.reshape(x_new, (1, -1))

        predTree = isSafe.predict(x_new)
        output = predTree[0]

        return render_template('main.html', output=output)
    else:
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
