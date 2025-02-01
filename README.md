# **Warehouse Optimization System**

## **Project Title**
**Warehouse Optimization System: Predictive Analytics for Inventory Management**

---

## **Description**
The **Warehouse Optimization System** is a data-driven solution designed to help businesses optimize their warehouse operations by predicting future sales quantities. Using machine learning (CatBoost Regressor) and data analytics, the system provides actionable insights to improve inventory management, reduce costs, and enhance overall efficiency.

This project is built using **Python**, **Flask**, and **CatBoost**, with a user-friendly web interface for uploading sales data and viewing predictions.

---

## **Key Features**
1. **Data Upload**: Users can upload sales data in CSV format.
2. **Data Preprocessing**: The system automatically cleans and preprocesses the data (e.g., handling missing values, filtering outliers, and feature engineering).
3. **Sales Prediction**: Predicts future sales quantities using a pre-trained CatBoost model.
4. **Interactive Dashboard**: Displays predictions in a clean, professional table format.
5. **Responsive Design**: The web interface is fully responsive and works on all devices (desktop, tablet, mobile).
6. **Scalable**: Built with Flask, the system can be easily extended to handle larger datasets and additional features.

---

## **Why This Project Was Created**
The **Warehouse Optimization System** was created to address common challenges in inventory management, such as:
- **Overstocking**: Excess inventory leads to increased storage costs.
- **Understocking**: Insufficient inventory results in lost sales and unhappy customers.
- **Inefficient Operations**: Lack of data-driven insights can lead to poor decision-making.

By leveraging machine learning and predictive analytics, this system helps businesses:
- **Forecast Demand**: Accurately predict future sales quantities to optimize inventory levels.
- **Reduce Costs**: Minimize storage and operational costs by maintaining optimal stock levels.
- **Improve Efficiency**: Streamline warehouse operations with data-driven insights.

---

## **Technologies Used**
- **Backend**: Python, Flask, CatBoost, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap
- **Machine Learning**: CatBoost Regressor
- **Data Preprocessing**: Pandas, NumPy
- **Deployment**: Flask (local or cloud-based)

---

## **How It Works**
1. **Upload Data**: Users upload a CSV file containing sales data (e.g., `InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, `Country`).
2. **Preprocess Data**: The system cleans and preprocesses the data (e.g., handling missing values, filtering outliers, and feature engineering).
3. **Generate Predictions**: The pre-trained CatBoost model predicts sales quantities for the next 10 days.
4. **View Results**: Predictions are displayed in a clean, professional table format.

---

## **Installation**
To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/warehouse-optimization-system.git
   cd warehouse-optimization-system
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   ```bash
   python app.py
   ```

4. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:5000`.

---

## **File Structure**
```
warehouse-optimization-system/
├── app.py                  # Flask application
├── train_model.py          # Script to train and save the CatBoost model
├── models/
│   └── catboost_model.cbm  # Pre-trained CatBoost model
├── data/                   # Folder for uploaded CSV files
├── templates/              # HTML templates
│   ├── index.html          # Home page (upload form)
│   └── results.html        # Results page (predictions table)
├── static/                 # Static files (CSS, images)
│   └── style.css           # Custom CSS
└── README.md               # Project documentation
```

---

## **Usage**
1. **Upload Data**:
   - Go to the home page (`http://127.0.0.1:5000`).
   - Upload a CSV file containing sales data.

2. **View Predictions**:
   - After uploading the file, the system will display sales predictions for the next 10 days.

3. **Download Report** (Optional):
   - Click the "Download Report" button to save the predictions as a CSV file.

---

## **Example Dataset**
The system expects a CSV file with the following columns:
- `InvoiceNo`: Invoice number (string)
- `StockCode`: Product code (string)
- `Description`: Product description (string)
- `Quantity`: Quantity sold (integer)
- `InvoiceDate`: Date and time of the transaction (string in `MM/DD/YYYY HH:MM` format)
- `UnitPrice`: Price per unit (float)
- `CustomerID`: Customer identifier (string)
- `Country`: Country of the customer (string)

Example CSV Data:
```csv
InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,CustomerID,Country
536365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,12/1/2010 8:26,2.55,17850,United Kingdom
536366,71053,WHITE METAL LANTERN,6,12/1/2010 8:26,3.39,17850,United Kingdom
536367,84406B,CREAM CUPID HEARTS COAT HANGER,8,12/1/2010 8:34,2.75,17850,United Kingdom
```

---

## **Future Enhancements**
- **Advanced Analytics**: Add more visualizations (e.g., charts, graphs) to provide deeper insights.
- **User Authentication**: Add login/signup functionality for multiple users.
- **Cloud Deployment**: Deploy the system on a cloud platform (e.g., AWS, Heroku) for scalability.
- **Real-Time Updates**: Integrate real-time data processing for live predictions.

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch
3. Commit your changes
4. Push to the branch 
5. Open a pull request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
For questions or feedback, feel free to reach out:
- **Your Name**: Lokesh
- **GitHub**: [Your GitHub Profile](https://github.com/Lokesh777777)

---

This `README.md` provides a comprehensive overview of your project, making it easy for others to understand and contribute. Let me know if you'd like to add or modify anything! 🚀
