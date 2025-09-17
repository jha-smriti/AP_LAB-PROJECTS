# Experiment 4: Stock Price Prediction using LSTM

An advanced time series forecasting system that predicts stock prices using Long Short-Term Memory (LSTM) neural networks with an interactive web interface.

## 📁 Files Structure
```
EXPERIMENT4/
├── model.ipynb          # Jupyter notebook for LSTM model development
├── app.py              # Flask web application server
├── index.html          # Web interface for stock prediction
└── script.js           # Frontend JavaScript functionality
```

## 🎯 Project Overview

This project implements a sophisticated stock price prediction system using LSTM deep learning networks. It combines financial data analysis, time series modeling, and web development to create an interactive forecasting platform.

## ✨ Features

- **LSTM Neural Networks**: Advanced time series prediction using deep learning
- **Interactive Web Interface**: User-friendly platform for stock analysis
- **Real-time Predictions**: Generate forecasts for multiple stock symbols
- **Historical Data Visualization**: Charts and graphs for trend analysis
- **Multiple Timeframes**: Support for various prediction windows
- **Financial Indicators**: Technical analysis integration
- **Responsive Design**: Works across desktop and mobile devices

## 📈 Stock Market Analysis

### Supported Features
- **Stock Symbol Input**: Enter any valid stock ticker
- **Historical Data**: Fetch and analyze past price movements
- **Technical Indicators**: Moving averages, RSI, MACD
- **Trend Analysis**: Identify bullish/bearish patterns
- **Volume Analysis**: Trading volume considerations

### Prediction Capabilities
- **Price Forecasting**: Future stock price predictions
- **Trend Direction**: Bullish or bearish trend identification
- **Confidence Intervals**: Prediction reliability metrics
- **Risk Assessment**: Volatility and risk indicators

## 🧠 LSTM Model Architecture

### Network Design
- **Input Layer**: Sequential stock price data
- **LSTM Layers**: Multiple memory cells for pattern recognition
- **Dropout Layers**: Prevent overfitting
- **Dense Layers**: Final prediction output
- **Time Steps**: Configurable lookback window

### Training Features
- **Data Preprocessing**: Normalization and scaling
- **Feature Engineering**: Technical indicators as inputs
- **Sequence Generation**: Time series data preparation
- **Validation Split**: Train/test data separation

## 🛠 Prerequisites

### System Requirements
- Python 3.8+
- 8GB+ RAM recommended
- Internet connection for data fetching
- Modern web browser

### Python Dependencies
```bash
pip install tensorflow pandas numpy matplotlib flask yfinance scikit-learn plotly dash
```

## 🚀 Installation and Setup

1. **Navigate to Directory**:
   ```bash
   cd EXPERIMENT4
   ```

2. **Install Dependencies**:
   ```bash
   pip install tensorflow pandas numpy matplotlib flask yfinance scikit-learn
   ```

3. **Train Model** (Optional):
   ```bash
   jupyter notebook model.ipynb
   ```
   - Execute all cells to train the LSTM model
   - Model will be saved for web application

4. **Run Web Application**:
   ```bash
   python app.py
   ```

5. **Access Application**:
   - Open browser and navigate to `http://localhost:5000`
   - Start making stock predictions!

## 🌐 Web Application Usage

### Getting Started
1. **Enter Stock Symbol**: Type a valid ticker (e.g., AAPL, GOOGL, TSLA)
2. **Select Timeframe**: Choose prediction period
3. **Configure Parameters**: Set additional options if available
4. **Generate Prediction**: Click "Predict" to get forecasts

### Understanding Results
- **Predicted Prices**: Future price forecasts
- **Confidence Scores**: Reliability of predictions
- **Trend Analysis**: Direction and strength
- **Historical Context**: Past performance comparison

## 📊 Data Sources

### Primary Data
- **Yahoo Finance API**: Real-time and historical stock data
- **Price Data**: Open, High, Low, Close, Volume
- **Frequency**: Daily stock prices
- **Coverage**: Major global stock exchanges

### Technical Indicators
- **Moving Averages**: SMA, EMA
- **Momentum**: RSI, MACD
- **Volume**: Trading volume analysis
- **Volatility**: Standard deviation, Bollinger Bands

## 🛠 Technologies Used

### Backend Technologies
- **Python**: Core programming language
- **TensorFlow/Keras**: LSTM implementation
- **Flask**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **yfinance**: Stock data API

### Frontend Technologies
- **HTML5**: Web structure and semantics
- **CSS3**: Styling and responsive design
- **JavaScript**: Interactive functionality
- **Chart.js/Plotly**: Data visualization

### Machine Learning
- **LSTM Networks**: Time series prediction
- **Feature Engineering**: Technical indicator creation
- **Data Preprocessing**: Normalization and scaling
- **Model Evaluation**: Performance metrics

## 📈 Model Performance

### Evaluation Metrics
- **Mean Absolute Error (MAE)**: Average prediction error
- **Root Mean Square Error (RMSE)**: Prediction accuracy
- **Mean Absolute Percentage Error (MAPE)**: Relative error
- **Directional Accuracy**: Trend prediction success

### Validation Methods
- **Time Series Split**: Chronological validation
- **Walk-Forward Analysis**: Real-world simulation
- **Backtesting**: Historical performance testing

## 🔍 File Descriptions

- **`model.ipynb`**: Complete LSTM model development and training
- **`app.py`**: Flask server with prediction endpoints
- **`index.html`**: User interface for stock prediction
- **`script.js`**: Frontend logic and API interactions

## ⚠️ Important Disclaimers

### Financial Advisory
- **Educational Purpose**: This project is for learning only
- **Not Financial Advice**: Do not use for actual trading decisions
- **Market Risks**: Stock markets are inherently unpredictable
- **Consult Professionals**: Always seek financial advisor guidance

### Technical Limitations
- **Prediction Accuracy**: Models cannot guarantee future performance
- **Market Volatility**: Extreme events may not be predicted
- **Data Dependency**: Quality predictions require quality data

## 🔧 Troubleshooting

**Common Issues:**

1. **Data Fetching Error**:
   ```bash
   pip install --upgrade yfinance
   ```

2. **Memory Issues**:
   - Reduce sequence length
   - Use smaller batch sizes

3. **Model Loading Error**:
   - Re-run training notebook
   - Check model file paths

4. **Prediction Errors**:
   - Verify stock symbol validity
   - Check internet connection

## 📚 Key Learning Outcomes

- **Time Series Analysis**: Understanding sequential data patterns
- **LSTM Architecture**: Deep learning for temporal data
- **Financial Markets**: Stock market dynamics and indicators
- **Web Development**: Full-stack application development
- **Data Visualization**: Interactive charts and graphs

## 🚀 Future Enhancements

- **Multiple Asset Classes**: Forex, cryptocurrency, commodities
- **Advanced Models**: Transformer networks, ensemble methods
- **Real-time Streaming**: Live data integration
- **Portfolio Optimization**: Multi-asset portfolio suggestions
- **News Sentiment**: Incorporate news sentiment analysis
- **Mobile Application**: Native mobile app development

## 📖 Additional Resources

- **Financial Data APIs**: Alpha Vantage, Quandl, IEX Cloud
- **Technical Analysis**: Investopedia, TradingView
- **LSTM Tutorials**: TensorFlow documentation
- **Flask Development**: Flask official documentation

---
**Course**: Advanced Programming Laboratory  
**Experiment**: 4  
**Topic**: Time Series Forecasting using Deep Learning