import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def euler_method(k, x0, y0, x_final, h):
    """
    Implement Euler's method for dy/dx = ky
    
    Args:
        k: constant in the differential equation
        x0: initial x value
        y0: initial y value
        x_final: final x value to compute to
        h: step size
    
    Returns:
        lists of x values, y values (Euler), and y values (analytical)
    """
    # Calculate number of steps
    n_steps = int((x_final - x0) / h)
    
    # Initialize arrays
    x_values = [x0]
    y_euler = [y0]
    y_analytical = [y0]
    
    # Current values
    x_current = x0
    y_current = y0
    
    # Perform Euler's method
    for i in range(n_steps):
        # Euler's method: y_{n+1} = y_n + h * f(x_n, y_n)
        # For dy/dx = ky, f(x,y) = ky
        y_next = y_current + h * k * y_current
        x_next = x_current + h
        
        # Store values
        x_values.append(x_next)
        y_euler.append(y_next)
        
        # Analytical solution: y = y0 * e^(k*(x-x0))
        y_analytical.append(y0 * math.exp(k * (x_next - x0)))
        
        # Update current values
        x_current = x_next
        y_current = y_next
    
    return x_values, y_euler, y_analytical

def create_step_table(x_values, y_euler, y_analytical, k, h):
    """
    Create a step-by-step calculation table
    """
    steps_data = []
    
    for i in range(len(x_values)):
        if i == 0:
            derivative = k * y_euler[i]
            steps_data.append({
                'Step': i,
                'x': f"{x_values[i]:.4f}",
                'y (Euler)': f"{y_euler[i]:.6f}",
                'y (Analytical)': f"{y_analytical[i]:.6f}",
                'dy/dx = ky': f"{derivative:.6f}",
                'Error': f"{abs(y_euler[i] - y_analytical[i]):.6f}",
                'Next y': "Initial value"
            })
        else:
            derivative = k * y_euler[i-1]
            next_y_calc = f"{y_euler[i-1]:.6f} + {h} × {derivative:.6f}"
            steps_data.append({
                'Step': i,
                'x': f"{x_values[i]:.4f}",
                'y (Euler)': f"{y_euler[i]:.6f}",
                'y (Analytical)': f"{y_analytical[i]:.6f}",
                'dy/dx = ky': f"{derivative:.6f}",
                'Error': f"{abs(y_euler[i] - y_analytical[i]):.6f}",
                'Next y': next_y_calc
            })
    
    return pd.DataFrame(steps_data)

def main():
    st.title("Euler's Method for Differential Equations")
    st.markdown("### Solving dy/dx = ky using Euler's Method")
    
    st.markdown("""
    This application solves differential equations of the form **dy/dx = ky** where the rate of change 
    is directly proportional to the amount present. This type of equation models exponential growth or decay.
    """)
    
    # Input section
    st.header("Input Parameters")
    
    col1, col2 = st.columns(2)
    
    with col1:
        k = st.number_input(
            "Constant k (proportionality constant)",
            value=0.1,
            step=0.01,
            format="%.3f",
            help="Positive values indicate growth, negative values indicate decay"
        )
        
        x0 = st.number_input(
            "Initial x value (x₀)",
            value=0.0,
            step=0.1,
            format="%.2f"
        )
    
    with col2:
        y0 = st.number_input(
            "Initial y value (y₀)",
            value=1.0,
            step=0.1,
            format="%.2f"
        )
        
        x_final = st.number_input(
            "Final x value",
            value=5.0,
            step=0.1,
            format="%.2f"
        )
    
    h = st.number_input(
        "Step size (h)",
        value=0.1,
        min_value=0.001,
        max_value=1.0,
        step=0.01,
        format="%.3f",
        help="Smaller step sizes generally provide more accurate results"
    )
    
    # Validation
    if x_final <= x0:
        st.error("Final x value must be greater than initial x value")
        return
    
    if h <= 0:
        st.error("Step size must be positive")
        return
    
    # Calculate using Euler's method
    x_values, y_euler, y_analytical = euler_method(k, x0, y0, x_final, h)
    
    # Display results
    st.header("Results")
    
    # Summary statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Final Euler Value", f"{y_euler[-1]:.6f}")
    
    with col2:
        st.metric("Final Analytical Value", f"{y_analytical[-1]:.6f}")
    
    with col3:
        final_error = abs(y_euler[-1] - y_analytical[-1])
        relative_error = (final_error / abs(y_analytical[-1])) * 100 if y_analytical[-1] != 0 else 0
        st.metric("Final Absolute Error", f"{final_error:.6f}")
    
    st.metric("Final Relative Error", f"{relative_error:.4f}%")
    
    # Mathematical explanation
    st.subheader("Mathematical Background")
    st.markdown(f"""
    **Differential Equation:** dy/dx = {k}y
    
    **Analytical Solution:** y = {y0} × e^({k} × (x - {x0}))
    
    **Euler's Method Formula:** y_{{n+1}} = y_n + h × f(x_n, y_n) = y_n + {h} × {k} × y_n
    """)
    
    # Step-by-step calculation table
    st.subheader("Step-by-Step Calculations")
    
    steps_df = create_step_table(x_values, y_euler, y_analytical, k, h)
    
    # Display table with pagination for large datasets
    if len(steps_df) > 20:
        st.markdown("*Showing first 20 steps. Use the full table below for complete data.*")
        st.dataframe(steps_df.head(20), use_container_width=True)
        
        with st.expander("Show All Steps"):
            st.dataframe(steps_df, use_container_width=True)
    else:
        st.dataframe(steps_df, use_container_width=True)
    
    # Visualization
    st.subheader("Visualization")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Comparison of methods
    ax1.plot(x_values, y_euler, 'bo-', label='Euler Method', markersize=4, linewidth=2)
    ax1.plot(x_values, y_analytical, 'r-', label='Analytical Solution', linewidth=2)
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_title('Euler Method vs Analytical Solution')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Error analysis
    errors = [abs(y_euler[i] - y_analytical[i]) for i in range(len(x_values))]
    ax2.plot(x_values, errors, 'g-', linewidth=2, marker='o', markersize=3)
    ax2.set_xlabel('x')
    ax2.set_ylabel('Absolute Error')
    ax2.set_title('Error Analysis')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig)
    
    # Error statistics
    st.subheader("Error Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        max_error = max(errors)
        st.metric("Maximum Error", f"{max_error:.6f}")
    
    with col2:
        mean_error = np.mean(errors)
        st.metric("Mean Error", f"{mean_error:.6f}")
    
    with col3:
        rms_error = np.sqrt(np.mean([e**2 for e in errors]))
        st.metric("RMS Error", f"{rms_error:.6f}")
    
    # Educational notes
    st.subheader("Educational Notes")
    st.markdown("""
    **Key Observations:**
    - Smaller step sizes (h) generally provide more accurate results but require more computation
    - The error typically accumulates as we move further from the initial condition
    - For exponential growth (k > 0), Euler's method tends to underestimate the true solution
    - For exponential decay (k < 0), Euler's method tends to overestimate the true solution
    
    **Improving Accuracy:**
    - Use smaller step sizes
    - Consider higher-order methods like Runge-Kutta
    - Monitor error accumulation over longer intervals
    """)

if __name__ == "__main__":
    main()
