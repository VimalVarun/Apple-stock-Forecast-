# 📈 Stock Price Prediction using LSTM  

## 🔥 Project Overview  
This project predicts stock prices for the next 30 days using deep learning techniques. We use **LSTM (Long Short-Term Memory)** neural networks, which are highly effective for time series forecasting. The model is trained on historical stock price data and aims to capture patterns for future price movements.  

## 📊 Dataset  
The dataset used for this project includes:  
- **Date** (converted to datetime format)  
- **Open, High, Low, Close, and Volume** prices  
- **Technical indicators** such as Moving Averages (MA), Lag Features, and Trend Analysis  

### **🔹 Data Preprocessing Steps:**  
- Converted `Date` column to datetime and sorted values  
- Created additional time-based features (Month, Day, Day of the Week)  
- Generated **Lag Features** (Previous Days’ Closing Prices)  
- Computed **Moving Averages** (7-day, 14-day, 30-day)  
- Normalized stock prices using **MinMaxScaler**  
- Split dataset into **80% Training & 20% Testing**  

## 📌 Model Selection  
To predict stock prices, we compared different models:  

| Model      | Strengths | Weaknesses |
|------------|----------|------------|
| **ARIMA**  | Good for short-term trends | Struggles with sudden market changes |
| **Prophet** | Captures seasonality well | Not great for short-term volatility |
| **XGBoost** | Works well with feature-based data | Doesn't consider sequential dependencies |
| **LSTM (Used in this project)** | Captures time-based dependencies well | Requires a large amount of data |

Since LSTMs handle time-dependent patterns efficiently, we used a **bi-layer LSTM model with Dropout layers** for better accuracy.  

## 🔥 Model Architecture  
- **LSTM Layers** with ReLU activation  
- **Dropout Layers** to prevent overfitting  
- **Dense Output Layer** for predicting closing price  
