from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def read_csv_and_vis():
    circle_data_lst = []
    for i in range(0, 50):
        circle_data_lst.append(
            {
                "cx":np.random.random()*750,
                "cy": np.random.random()*750,
                "r": (np.random.random()+1)*20,
                "fill": f"rgb({np.random.randint(0, 256)}, {np.random.randint(0, 256)}, {np.random.randint(0, 256)})",
            }
        )
    return render_template('chart.html', circle_data_lst=circle_data_lst)

if __name__=='__main__':
    app.run()