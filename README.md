
# Customer Sales Analysis Project

This project involves customer segmentation and sales prediction using data from customer shopping transactions. The goal of the project is to help businesses understand customer behavior, segment customers based on purchasing patterns, and predict future sales. The project is built using Python for data analysis, machine learning, and visualization.

## Project Overview

The project performs the following tasks:

1. **Data Loading and Cleaning**: Loads and cleans customer transaction data.
2. **Feature Engineering**: Creates customer-level features like total spend, number of transactions, and average order value.
3. **Customer Segmentation**: Uses K-Means clustering to group customers based on their purchasing behavior.
4. **Sales Prediction**: Builds a Random Forest model to predict total customer spend based on historical data.
5. **Visualizations**: Generates visualizations for clustering results and sales predictions.
6. **Report Generation**: Automatically saves customer segmentation and prediction results to an Excel file.

## Project Structure

- **Customer_sales_analysis/**
  - **data_loader.py**: Script for loading and cleaning data.
  - **feature_engineering.py**: Script for creating customer-level features.
  - **clustering.py**: Script for applying K-Means clustering for customer segmentation.
  - **prediction.py**: Script for building and evaluating the sales prediction model.
  - **visualization.py**: Script for generating visualizations.
  - **report_generator.py**: Script for saving the analysis results to Excel.
  - **main.py**: Main script to orchestrate the entire project.
  - **README.md**: Project overview and instructions.
  - **customer_shopping_data.csv**: The dataset used for analysis.

## Installation

### Requirements

Make sure you have the following libraries installed:

- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `openpyxl`

You can install the required libraries using pip:

```bash
pip install pandas matplotlib seaborn scikit-learn openpyxl
```

## How to Run the Project

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/Customer_sales_analysis.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Customer_sales_analysis
   ```

3. **Install the required libraries**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main script**:

   ```bash
   python main.py
   ```

5. The results will be saved as `customer_report.xlsx` and visualized in the output window.

## Features and Workflow

### Data Loading and Cleaning

- The dataset is loaded using `data_loader.py`, which handles missing values and formats date columns. It also creates a `total_spend` column by multiplying product price and quantity.

### Feature Engineering

- `feature_engineering.py` creates customer-level features such as:
  - Total spend
  - Total quantity of items purchased
  - Number of unique transactions
  - Average spend per transaction

### Customer Segmentation

- Using **K-Means clustering** in `clustering.py`, customers are segmented into different groups based on their purchasing patterns. Visualizations of the clustering results are generated using **PCA** for dimensionality reduction.

### Sales Prediction

- In `prediction.py`, a **Random Forest** model is trained to predict the total spend per customer using features like:
  - Total transactions
  - Average spend per order
  - Total quantity purchased
- The model is evaluated using **Mean Squared Error (MSE)** and **R-squared**.

### Visualization

- Visualizations of the clustering results and prediction accuracy are generated using **matplotlib** and **seaborn** in `visualization.py`.

### Report Generation

- The final results, including customer segmentation and sales predictions, are saved to an Excel file (`customer_report.xlsx`) using **openpyxl** in `report_generator.py`.

## Technologies Used

- **Python**: Programming language
- **pandas**: Data manipulation
- **matplotlib** and **seaborn**: Data visualization
- **scikit-learn**: Machine learning (K-Means clustering, Random Forest)
- **openpyxl**: Excel report generation


