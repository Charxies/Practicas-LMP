from flask import Flask, render_template
from forms import registerForm
import json
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)
datalist=[{}]

@app.route('/', methods=['POST', 'GET'])
def index():
    msg = 'todo bien'
    form=registerForm()
    if form.validate_on_submit():
        datalist=({'Nombre': form.nombre.data,
                         'Apellido Paterno': form.apellidop.data,
                         'Apellido Materno': form.apellidom.data,
                         'Telefono': form.telefono.data,
                         'Email': form.email.data,
                         'Sexo': form.sexo.data
                         })
        with open('doc.txt', 'a') as f:
            f.write("\n"+json.dumps(datalist))
            print(datalist)
        msg = 'usuario registrado'
    return render_template('index.html', form=form)
if __name__ == '__main__':
    app.run(debug=True)
