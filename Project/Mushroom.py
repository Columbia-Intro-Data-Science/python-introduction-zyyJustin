
from flask import Flask
from flask import request
from flask import render_template
import pickle

app = Flask(__name__)

@app.route('/')
def mushroom():
    return render_template("Mushroom.html")

@app.route('/', methods=['POST'])
def mushroom_post():
    print('=====')
    cap_shape = request.form['cap-shape']
    cap_surface = request.form['cap-surface']
    cap_color = request.form['cap-color']
    bruises = request.form['bruises']
    odor = request.form['odor']
    gill_attachment = request.form['gill-attachment']
    gill_spacing = request.form['gill-spacing']
    gill_size = request.form['gill-size']
    gill_color = request.form['gill-color']
    stalk_shape = request.form['stalk-shape']
    stalk_surface_above_ring = request.form['stalk-surface-above-ring']
    stalk_surface_below_ring = request.form['stalk-surface-below-ring']
    stalk_color_above_ring = request.form['stalk-color-above-ring']
    stalk_color_below_ring = request.form['stalk-color-below-ring']
    veil_color = request.form['veil-color']
    ring_number = request.form['ring-number']
    ring_type = request.form['ring-type']
    spore_print_color = request.form['spore-print-color']
    population = request.form['population']
    habitat = request.form['habitat']
    
    input = [cap_shape, cap_color, cap_surface, bruises, odor , gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, \
             stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring ,stalk_color_below_ring, \
             veil_color, ring_number, ring_type ,spore_print_color, population, habitat]
    
    pickle_in = open('decisiontree.pickle', 'rb')
    clf = pickle.load(pickle_in)
    prediction = clf.predict(input)
    print('=====')
    if prediction == 1:
        return render_template("safe.html")
    else:
        return render_template("poison.html")

if __name__ == '__main__':
    app.debug = True
    app.run()