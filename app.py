from flask import Flask,request,render_template

app = Flask(__name__)

# # test
# @app.route('/home')
# def home():
#     return "<h1>Hello World<h1>"

@app.route('/', methods = ['POST','GET'])
def home_page():
    return render_template("index.html")

@app.route('/bill',methods=['POST'])
def shopping_bill():
    if request.method == 'POST' :
        operation = request.form['operation']
        quantity = int(request.form['quantity'])
        
        total_cost = 0

        if operation == 'protinex':
            total_cost = 1500 * quantity
        elif operation == 'chyawanprash':
            total_cost = 200 * quantity
        elif operation == 'almond':
            total_cost = 800 * quantity
        elif operation == 'oats':
            total_cost = 100 * quantity
        elif operation == 'cashew':
            total_cost = 700 * quantity
        else:
            total_cost = 500 * quantity

        if total_cost < 1000:
            discount = total_cost * (10/100)
        elif total_cost >= 1000 and total_cost < 3000:
            discount = total_cost * (20/100)
        elif total_cost >= 3000 and total_cost < 5000:
            discount = total_cost * (25/100)
        else:
            discount = total_cost * (35/100)
    final_cost = total_cost - discount
    return render_template("final_cost.html",final_cost=final_cost)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)