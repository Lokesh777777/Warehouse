from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from catboost import CatBoostRegressor
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'data/'

# Load the pre-trained CatBoost model
model = CatBoostRegressor()
model.load_model('catboost_model.cbm')

def preprocess_data(df):
    """Preprocess the uploaded data for prediction"""
    # Handle missing values
    df = df.dropna(subset=['CustomerID', 'Description'])
    
    # Filter data
    df = df[(df.UnitPrice > 0.1) & (df.UnitPrice < 20)]
    df = df[df.Quantity < 55]
    
    # Feature engineering
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Year'] = df['InvoiceDate'].dt.year
    df['Month'] = df['InvoiceDate'].dt.month
    df['Week'] = df['InvoiceDate'].dt.isocalendar().week
    df['Weekday'] = df['InvoiceDate'].dt.weekday
    df['Day'] = df['InvoiceDate'].dt.day
    
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = datetime.now().strftime("%Y%m%d%H%M%S") + ".csv"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Process data
            raw_data = pd.read_csv(filepath, encoding="ISO-8859-1")
            processed_data = preprocess_data(raw_data)
            processed_data.to_csv('data/processed_data.csv', index=False)
            
            return redirect(url_for('results'))
    
    return render_template('index.html')

@app.route('/results')
def results():
    # Load processed data
    data = pd.read_csv('data/processed_data.csv')
    
    # Generate predictions
    features = ['Year', 'Month', 'Week', 'Weekday', 'Day', 'UnitPrice']
    sample_data = data[features].iloc[:10]  # Predict for first 10 entries
    predictions = model.predict(sample_data)
    
    # Create results table
    results = []
    for i, (_, row) in enumerate(sample_data.iterrows()):
        results.append({
            'date': f"{row['Year']}-{row['Month']}-{row['Day']}",
            'unit_price': row['UnitPrice'],
            'predicted_quantity': round(predictions[i], 2)
        })
    
    return render_template('results.html', results=results)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)