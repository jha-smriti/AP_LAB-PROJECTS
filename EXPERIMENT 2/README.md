# Experiment 2: Dog vs Cat Image Classification

A comprehensive machine learning project for binary image classification using various algorithms to distinguish between dogs and cats.

## 📁 Files Structure
```
EXPERIMENT 2/
└── proj_Dog_vs_cat_classification.ipynb    # Complete implementation notebook
```

## 🎯 Project Overview

This experiment implements and compares multiple machine learning approaches for classifying images of dogs and cats. The project demonstrates the entire machine learning pipeline from data preprocessing to model evaluation.

## ✨ Features

- **Multiple ML Algorithms**: Implementation of various classification models
- **Image Preprocessing**: Data augmentation and normalization techniques
- **Model Comparison**: Performance evaluation across different algorithms
- **Visualization**: Results plotting and data exploration
- **Comprehensive Analysis**: Detailed accuracy metrics and confusion matrices

## 🤖 Machine Learning Models Implemented

1. **Convolutional Neural Networks (CNN)**
   - Deep learning approach optimized for image classification
   - Multiple convolutional and pooling layers
   - Dropout for regularization

2. **Support Vector Machine (SVM)**
   - Traditional ML approach with feature extraction
   - Kernel-based classification

3. **Random Forest**
   - Ensemble method with multiple decision trees
   - Feature importance analysis

4. **Logistic Regression**
   - Linear classification baseline model
   - Probability-based predictions

## 🛠 Prerequisites

Install required dependencies:
```bash
pip install tensorflow keras scikit-learn matplotlib pandas numpy opencv-python pillow seaborn
```

## 🚀 How to Run

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: If requirements.txt is not present, install the packages listed in Prerequisites*

2. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook proj_Dog_vs_cat_classification.ipynb
   ```

3. **Execute the Notebook**:
   - Run all cells sequentially
   - Follow the step-by-step implementation
   - View results and visualizations

## 📊 Dataset Information

- **Type**: Binary classification dataset
- **Classes**: Dogs and Cats
- **Format**: Image files (JPG/PNG)
- **Preprocessing**: Resizing, normalization, and augmentation applied

## 🔍 Implementation Steps

1. **Data Loading and Exploration**
   - Dataset visualization
   - Class distribution analysis

2. **Data Preprocessing**
   - Image resizing and normalization
   - Data augmentation techniques
   - Train/validation/test split

3. **Model Implementation**
   - CNN architecture design
   - Traditional ML feature extraction
   - Model compilation and training

4. **Model Evaluation**
   - Accuracy metrics calculation
   - Confusion matrix analysis
   - ROC curves and AUC scores

5. **Results Comparison**
   - Performance comparison across models
   - Visualization of results

## 📈 Expected Results

- **CNN**: Highest accuracy (typically 80-90%)
- **SVM**: Good performance with proper feature extraction
- **Random Forest**: Moderate accuracy with interpretability
- **Logistic Regression**: Baseline performance

## 🛠 Technologies Used

- **Python**: Primary programming language
- **TensorFlow/Keras**: Deep learning framework
- **Scikit-learn**: Traditional ML algorithms
- **OpenCV**: Image processing
- **Matplotlib/Seaborn**: Data visualization
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations

## 📝 Key Learnings

- Image preprocessing techniques
- CNN architecture design
- Comparison of deep learning vs traditional ML
- Model evaluation metrics
- Data augmentation strategies

## 🔧 Troubleshooting

**Common Issues:**
1. **Memory Error**: Reduce batch size or image resolution
2. **CUDA Error**: Ensure proper GPU setup or use CPU
3. **Import Error**: Verify all dependencies are installed

## 📊 Performance Metrics

The notebook evaluates models using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC

---
**Course**: Advanced Programming Laboratory  
**Experiment**: 2  
**Topic**: Image Classification using Machine Learning