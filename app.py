from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    # Mock data for portfolio display

    data = {

        "balance": "₱45,850",
        "income": "₱60,000",
        "expense": "₱14,150",
        "savings": "₱30,000"

    }

    transactions = [

        {
            "name":"Food",
            "amount":"-₱850",
            "type":"Expense"
        },

        {
            "name":"Salary",
            "amount":"+₱30,000",
            "type":"Income"
        },

        {
            "name":"Internet",
            "amount":"-₱1,500",
            "type":"Expense"
        },

        {
            "name":"Freelance",
            "amount":"+₱10,000",
            "type":"Income"
        }

    ]


    return render_template(
        "dashboard.html",
        data=data,
        transactions=transactions
    )


if __name__ == "__main__":
    app.run(debug=True)