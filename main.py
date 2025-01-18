from flask import Flask, render_template, request
import shapes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        
        if operation == "add":
            result = shapes.add(num1, num2)
        elif operation == "subtract":
            result = shapes.subtract(num1, num2)
        elif operation == "multiply":
            result = shapes.multiply(num1, num2)
        elif operation == "divide":
            result = shapes.divide(num1, num2)
        else:
            result = "Operação inválida."

        return render_template('index.html', result=result)

    except ValueError:
        return render_template('index.html', result="Erro: Entrada inválida.")
    except Exception as e:
        return render_template('index.html', result=f"Erro: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
