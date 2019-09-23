from flask import Flask, render_template, request
import pandas as pd
import csv 
app = Flask(__name__)
 
@app.route('/')
def student():
   return render_template('index.html')
 
@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      ciudad = request.form['ciudad']
      fecha = request.form['fecha']
      coste = request.form['precio']
      resumen = [ciudad, fecha, coste]

      with open('tickets.csv', "a+") as inFile:
        for line in resumen:
            inFile.write(line)
            inFile.write("\n")

        with open("tickets.csv", "r") as fRead:
            content = csv.reader(fRead)
            data=[]
            iteration = 0
            for row in content:
                data.append(row)
                iteration = iteration + 1
        
      
      return(render_template("result.html", data=data))
 
if __name__ == '__main__':
   app.run(debug = True)