from flask import Flask ,render_template,request
app=Flask(__name__,template_folder="templates")
@app.route('/',methods =[ "POST"])
def index():
    a=request.form.get("email")
    print(a)
    return render_template("yu.html")
    
if __name__=="__main__":
    app.run(debug=True)