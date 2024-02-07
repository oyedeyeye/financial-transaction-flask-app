# Import libraries
from flask import Flask, url_for, render_template, request, redirect

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    """returns the list of transactions"""
    return render_template('transactions.html', transactions=transactions)

# Create operation
@app.route('/add', methods=['GET', 'POST'])
def add_transactions():
    """returns form if http method is GET or create new transaction if 
    http method is POST"""

    if request.method == 'POST':
        # create new transaction object based on form field values
        new_transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
            }

        # append the new transaction to the list
        transactions.append(new_transaction)

        # Redirect to the transcation list page
        return redirect(url_for('get_transactions'))

    # Render the form template to display the add transaction form
    return render_template('form.html')

# Update operation

# Delete operation

# Run the Flask app
