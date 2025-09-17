# Experiment 3: Pneumonia Detection from Chest X-rays

A deep learning web application that detects pneumonia in chest X-ray images using Convolutional Neural Networks (CNN) with an interactive Flask web interface.

## 📁 Files Structure
```
EXPERIMENT 3/
├── AP_Lab_Pneu_3.ipynb              # Model training and development notebook
├── app.py                           # Flask web application
├── requirements.txt                 # Python dependencies
├── .ipynb_checkpoints/              # Jupyter checkpoint files
├── templates/
│   └── index.html                   # Web interface template
├── static/
│   └── uploads/                     # Directory for uploaded images
└── test/                           # Sample test images
    ├── NORMAL/                     # Normal chest X-ray samples
    │   ├── IM-0001-0001.jpeg
    │   ├── IM-0003-0001.jpeg
    │   └── ... (multiple samples)
    └── PNEUMONIA/                  # Pneumonia case samples
        └── ... (multiple samples)
```

## 🎯 Project Overview

This project implements a binary classification system to detect pneumonia in chest X-ray images. It combines deep learning model training with a user-friendly web interface for real-time predictions.

## ✨ Features

- **CNN-based Detection**: Deep learning model for accurate pneumonia detection
- **Web Interface**: User-friendly Flask application for image upload
- **Real-time Predictions**: Instant classification with confidence scores
- **Sample Images**: Pre-loaded test cases for demonstration
- **High Accuracy**: Trained on medical imaging dataset
- **Confidence Scoring**: Probability-based predictions

## 🏥 Medical Classification

**Classes:**
- **Normal**: Healthy chest X-rays
- **Pneumonia**: X-rays showing pneumonia indicators

**Dataset Structure:**
- Training images organized by diagnosis
- Balanced dataset with normal and pneumonia cases
- High-resolution medical imaging data

## 🛠 Prerequisites

### System Requirements
- Python 3.7+
- 4GB+ RAM recommended
- Web browser for interface

### Python Dependencies
```bash
pip install -r requirements.txt
```

**Key Libraries:**
- TensorFlow/Keras
- Flask
- OpenCV
- NumPy
- Pillow
- Matplotlib

## 🚀 Installation and Setup

1. **Clone and Navigate**:
   ```bash
   cd "EXPERIMENT 3"
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train Model** (Optional):
   ```bash
   jupyter notebook AP_Lab_Pneu_3.ipynb
   ```
   - Run all cells to train the model
   - Model will be saved automatically

4. **Run Web Application**:
   ```bash
   python app.py
   ```

5. **Access Application**:
   - Open browser and navigate to `http://localhost:5000`
   - Upload chest X-ray images for prediction

## 🌐 Web Application Usage

### Upload and Predict
1. **Upload Image**: Click "Choose File" and select a chest X-ray
2. **Supported Formats**: JPEG, JPG, PNG
3. **Click Predict**: Get instant pneumonia detection results
4. **View Results**: See prediction confidence and diagnosis

### Sample Testing
- Use images from `test/NORMAL/` for healthy cases
- Use images from `test/PNEUMONIA/` for pneumonia cases
- Compare predictions with actual diagnoses

## 🧠 Model Architecture

### CNN Structure
- **Input Layer**: 224x224x3 (RGB images)
- **Convolutional Layers**: Feature extraction
- **Pooling Layers**: Dimensionality reduction
- **Dense Layers**: Classification
- **Output**: Binary classification (Normal/Pneumonia)

### Training Process
- Data augmentation for better generalization
- Binary cross-entropy loss
- Adam optimizer
- Early stopping to prevent overfitting

## 📊 Model Performance

### Metrics
- **Accuracy**: High classification accuracy
- **Precision**: Low false positive rate
- **Recall**: High true positive detection
- **F1-Score**: Balanced performance metric

### Validation
- Trained on medical imaging dataset
- Validated on separate test set
- Cross-validation for robust performance

## 🛠 Technologies Used

### Backend
- **Python**: Core programming language
- **TensorFlow/Keras**: Deep learning framework
- **Flask**: Web application framework
- **OpenCV**: Image processing

### Frontend
- **HTML5**: Web structure
- **CSS3**: Styling and layout
- **JavaScript**: Interactive functionality

### Data Processing
- **NumPy**: Numerical operations
- **Pillow**: Image manipulation
- **Matplotlib**: Visualization

## 🔍 File Descriptions

- **`AP_Lab_Pneu_3.ipynb`**: Complete model development workflow
- **`app.py`**: Flask web server and prediction logic
- **`requirements.txt`**: All required Python packages
- **`templates/index.html`**: Web interface template
- **`test/`**: Sample images for testing the system

## ⚠️ Important Notes

### Medical Disclaimer
- This is an educational project for learning purposes
- Not intended for actual medical diagnosis
- Always consult healthcare professionals for medical decisions

### Performance Considerations
- Model loading may take time on first run
- Large images are automatically resized
- GPU acceleration recommended for training

## 🔧 Troubleshooting

**Common Issues:**

1. **Module Import Error**:
   ```bash
   pip install --upgrade tensorflow flask opencv-python
   ```

2. **Memory Issues**:
   - Reduce image batch size
   - Close other applications

3. **Model Loading Error**:
   - Ensure model file is present
   - Re-run training notebook if needed

## 📈 Future Enhancements

- Multi-class classification (different pneumonia types)
- Integration with DICOM format
- Batch processing capability
- Advanced visualization features
- API endpoint for external integration

---
**Course**: Advanced Programming Laboratory  
**Experiment**: 3  
**Topic**: Medical Image Classification using Deep Learning