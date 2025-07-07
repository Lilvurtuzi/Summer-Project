# Euler's Method Differential Equation Solver

A Streamlit web application that implements and visualizes Euler's method for solving first-order differential equations of the form dy/dx = ky.

## Features

- Interactive parameter input for differential equation constants
- Real-time numerical solution using Euler's method
- Comparison with analytical solution
- Step-by-step calculation table
- Visual plots showing method comparison and error analysis
- Educational notes about the mathematics

## Installation & Setup

### Prerequisites
- Python 3.7 or higher installed on your computer

### Step 1: Download the Files
Download these files to a folder on your computer:
- `app.py` (the main application file)
- `README.md` (this file)

### Step 2: Install Required Packages
Open your terminal/command prompt and navigate to the folder containing the files, then run:

```bash
pip install streamlit numpy pandas matplotlib
```

### Step 3: Run the Application
In the same terminal/command prompt, run:

```bash
streamlit run app.py
```

### Step 4: Access the Application
- The application will automatically open in your web browser
- If it doesn't open automatically, go to: http://localhost:8501

## How to Use

1. **Input Parameters:**
   - **k**: The proportionality constant (positive for growth, negative for decay)
   - **Initial x value (x₀)**: Starting x coordinate
   - **Initial y value (y₀)**: Starting y coordinate  
   - **Final x value**: Where to stop the calculation
   - **Step size (h)**: Size of each step (smaller = more accurate)

2. **View Results:**
   - See the final calculated values
   - Review the step-by-step calculation table
   - Analyze the visual comparison plots
   - Check error statistics

3. **Experiment:**
   - Try different values of k to see growth vs decay
   - Adjust step size to see how it affects accuracy
   - Change initial conditions to explore different scenarios

## Mathematical Background

This application solves differential equations of the form:
```
dy/dx = ky
```

Where:
- **Analytical Solution**: y = y₀ × e^(k×(x-x₀))
- **Euler's Method**: y_{n+1} = y_n + h × k × y_n

## Troubleshooting

### Common Issues:

1. **"streamlit: command not found"**
   - Make sure Python is installed
   - Try: `python -m pip install streamlit`

2. **Import errors**
   - Install missing packages: `pip install [package-name]`

3. **Application won't start**
   - Check that you're in the correct folder
   - Verify `app.py` is in the same directory

4. **Browser doesn't open automatically**
   - Manually go to: http://localhost:8501

### Getting Help:
- Make sure all files are in the same folder
- Check that Python 3.7+ is installed: `python --version`
- Ensure all packages are installed correctly

## Educational Use

This application is perfect for:
- Learning numerical methods
- Understanding differential equations
- Comparing numerical vs analytical solutions
- Exploring the effects of step size on accuracy
- Teaching exponential growth and decay models

## System Requirements

- Python 3.7+
- Web browser (Chrome, Firefox, Safari, Edge)
- ~50MB of free disk space for packages
- Internet connection for initial package installation