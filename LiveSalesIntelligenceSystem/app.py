from flask import Flask, request, render_template
import csv
from datetime import datetime

app = Flask(__name__)
file_path = 'F:/LiveSalesIntelligenceSystem/sales_data.csv'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        orders = int(request.form['orders'])
        returns = int(request.form['returns'])
        revenue = float(request.form['revenue'])
        ad_spend = float(request.form['ad_spend'])
        visitors = int(request.form['visitors'])

        row = [
            request.form['platform'],
            request.form['category'],
            request.form['district'],
            datetime.now().strftime('%m/%d/%Y'),
            orders,
            returns,
            revenue,
            ad_spend,
            visitors,
            round(orders / visitors, 2),
            float(request.form['conversion_rate']),
            float(request.form['net_revenue']),
            float(request.form['rating']),
            float(request.form['fulfillment_time'])
        ]

        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(row)

        return "Row added successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)