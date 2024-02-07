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

# Update operation

# Delete operation

# Run the Flask app
    