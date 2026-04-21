from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class PersonAccount:
    def __init__(self):
        self.income = []
        self.expenses = []
    
    def add_income(self, amount, desc):
        self.income.append((amount, desc))

    def add_expenses(self, amount, desc):
        self.expenses.append((amount, desc))

    def total_income(self):
        return sum(a for a, _ in self.income)
    
    def total_expense(self):
        return sum(a for a, _ in self.expenses)
    
    def balance(self):
        return self.total_income() - self.total_expense()
    
    def all_amount(self):
        return self.balance()
    
account = PersonAccount()

# --- Routes ---

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    amount = int(data['amount'])
    desc = data['desc']
    type_ = data['type']

    if type_ == 'income':
        account.add_income(amount, desc)
    else:
        account.add_expenses(amount, desc)

    return jsonify({"message" : "added"})

@app.route('/summary')
def summary():
    return jsonify({
        "income": account.total_income(),
        "expense": account.total_expense(),
        "balance": account.balance()
    })

app.run(debug=True)
