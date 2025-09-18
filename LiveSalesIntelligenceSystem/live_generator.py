import csv, time, random
from datetime import datetime

file_path = 'F:/LiveSalesIntelligenceSystem/sales_data.csv'

def generate_row():
    orders = random.randint(50, 200)
    returns = random.randint(0, orders // 5)
    revenue = round(orders * random.uniform(500, 1500), 2)
    ad_spend = round(random.uniform(1000, 5000), 2)
    visitors = random.randint(500, 5000)
    
    return [
        random.choice(['Amazon', 'Flipkart', 'Myntra']),
        random.choice(['Electronics', 'Fashion', 'Home Decor']),
        random.choice(['Bengaluru Urban', 'Bengaluru Rural', 'Mysuru', 'Mangaluru',
        'Hubballi-Dharwad', 'Belagavi', 'Tumakuru', 'Ballari', 'Shivamogga',
        'Davangere', 'Udupi', 'Vijayapura', 'Kalaburagi', 'Raichur', 'Bidar',
        'Bagalkot', 'Haveri', 'Gadag', 'Koppal', 'Chitradurga', 'Chikkamagaluru',
        'Hassan', 'Mandya', 'Ramanagara', 'Kolar', 'Chikkaballapur', 'Yadgir',
        'Kodagu', 'Dharwad', 'Bellary']),
        datetime.now().strftime('%m/%d/%Y'),
        orders,
        returns,
        revenue,
        ad_spend,
        visitors,
        round(orders / visitors, 2),
        round(random.uniform(0.05, 0.3), 2),
        round(revenue * (1 - random.uniform(0.05, 0.3)), 2),
        round(random.uniform(3.5, 5.0), 2),
        round(random.uniform(1.0, 5.0), 2)
    ]

def append_to_csv(path):
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(generate_row())
    print("Row added at", datetime.now().strftime('%H:%M:%S'))

while True:
    append_to_csv(file_path)
    time.sleep(10)