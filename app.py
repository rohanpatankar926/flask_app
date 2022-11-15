from flask import Flask,redirect,render_template,request
import os

app=Flask(__name__)

@app.route("/",methods=["GET"])
def home_page():
    return render_template("index.html")

@app.route("/maths",methods=["POST"])
def math_operations():
    if request.method=="POST":
        operations=request.form["operation"]
        num1=int(request.form["num1"])
        num2=int(request.form["num2"])
        
        if (operations=="add"):
            add=num1+num2
            result= f"The sum of {num1} and {num2} is {add}"
        if (operations=="multiply"):
            mul=num1*num2
            result= f"The multiple of {num1} and {num2} is {mul}"
        if (operations=="subtract"):
            sub=num1-num2
            result= f"The substraction of {num1} and {num2} is {sub}"
        if (operations=="divide"):
            div=num1/num2
            result= f"The division of {num1} and {num2} is {div}"
        return render_template("results.html",result=result)

port=os.getenv("PORT",5000)
        
if __name__=="__main__":
    app.run(debug=False,host="0.0.0.0",port=port)
