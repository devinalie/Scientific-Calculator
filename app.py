import streamlit as st                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🔬")
st.title("🔬 Scientific Calculator")

mode = st.radio("Mode:", ["2 Numbers", "1 Number (Scientific)"], horizontal=True)

if mode == "2 Numbers":
    c1, c2 = st.columns(2)
    a = c1.number_input("First Number (x):", value=0.0)
    b = c2.number_input("Second Number (y):", value=0.0)
    op = st.selectbox("Operation:", ["Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)"])
    if st.button("Calculate", type="primary"):
        if op == "Add (+)": st.success(f"Result: {a + b}")
        elif op == "Subtract (-)": st.success(f"Result: {a - b}")
        elif op == "Multiply (×)": st.success(f"Result: {a * b}")
        elif op == "Divide (÷)": st.error("Cannot divide by 0") if b == 0 else st.success(f"Result: {a / b}")
        elif op == "Power (^)": st.success(f"Result: {math.pow(a, b)}")
else:
    c1, c2 = st.columns(2)
    x = c1.number_input("Value (x):", value=0.0)
    unit = c2.selectbox("Angle Unit:", ["Degrees", "Radians"])
    fn = st.selectbox("Function:", ["sin(x)", "cos(x)", "tan(x)", "√x", "log10(x)", "ln(x)", "x!"])
    if st.button("Calculate", type="primary"):
        s = math.radians(x) if unit == "Degrees" else x
        if fn == "sin(x)": st.success(f"Result: {round(math.sin(s), 8)}")
        elif fn == "cos(x)": st.success(f"Result: {round(math.cos(s), 8)}")
        elif fn == "tan(x)": st.success(f"Result: {round(math.tan(s), 8)}")
        elif fn == "√x": st.error("Must be >= 0") if x < 0 else st.success(f"Result: {math.sqrt(x)}")
        elif fn == "log10(x)": st.error("Must be > 0") if x <= 0 else st.success(f"Result: {math.log10(x)}")
        elif fn == "ln(x)": st.error("Must be > 0") if x <= 0 else st.success(f"Result: {math.log(x)}")
        elif fn == "x!": st.error("Must be integer >= 0") if x < 0 or not x.is_integer() else st.success(f"Result: {math.factorial(int(x))}")
