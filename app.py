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

# Read operation: List all transactions
@app.route('/')
def get_transactions():
    """returns the list of transactions"""
    return render_template('transactions.html', transactions=transactions)

# Create operation: Display add transaction form
@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    """returns form if http method is GET or create new transaction if 
    http method is POST"""

    if request.method == 'POST':
        # create new transaction object based on form field values
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
            }

        # append the new transaction to the list
        transactions.append(transaction)

        # Redirect to the transcation list page
        return redirect(url_for('get_transactions'))

    # Render the form template to display the add transaction form
    return render_template('form.html')

# Update operation: Display edit transaction form

@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    """ """
    try:
        if request.method == 'POST':
            # Extract the updated values from the form fields
            date = request.form['date']
            amount = float(request.form['amount'])

            # find transaction with the given id and pre-populate form
            for transaction in transactions:
                if transaction['id'] == transaction_id:
                    transaction['date'] = date
                    transaction['amount'] = amount
                    break

            # Redirect to the transaction list page after update
            return redirect(url_for('get_transactions'))

        # find transaction with the transaction_id and render it
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)

    except ValueError:
        return {'message': 'Transaction ID not found'}, 404

# Delete operation: Delete a transaction
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    """delete the transaction id"""
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    # Render the list of transaction page
    return redirect(url_for('get_transactions'))

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
