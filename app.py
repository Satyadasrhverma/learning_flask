from flask import Flask , render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('student.html', title = "Student Information")

@app.route('/result' , methods = ['POST'])
def result():
    if request.method == 'POST':
    
        form_daa = request.form
        return render_template("result.html", result = form_daa)
    


if __name__=="__main__":
    app.run(debug= True)



