import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# CSS agar layar dan tombol terlihat seperti kalkulator fisik
st.markdown("""
    <style>
    .calc-screen {
        background-color: #1e293b;
        color: #38bdf8;
        font-family: 'Courier New', monospace;
        font-size: 32px;
        font-weight: bold;
        text-align: right;
        padding: 18px 20px;
        border-radius: 12px;
        border: 2px solid #334155;
        margin-bottom: 14px;
        overflow-x: auto;
    }
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧮 Scientific Calculator")

if "expr" not in st.session_state:
    st.session_state.expr = ""

def press(val):
    if st.session_state.expr == "Error":
        st.session_state.expr = ""
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""

def backspace():
    if st.session_state.expr == "Error":
        st.session_state.expr = ""
    else:
        st.session_state.expr = st.session_state.expr[:-1]

def calculate():
    try:
        raw = st.session_state.expr
        raw = raw.replace("×", "*").replace("÷", "/").replace("^", "**")
        raw = raw.replace("π", "math.pi").replace("√(", "math.sqrt(")
        raw = raw.replace("sin(", "math.sin(math.radians(")
        raw = raw.replace("cos(", "math.cos(math.radians(")
        raw = raw.replace("tan(", "math.tan(math.radians(")
        raw = raw.replace("log(", "math.log10(").replace("ln(", "math.log(")
        raw = raw.replace("fact(", "math.factorial(")

        # Otomatis tutup kurung yang belum tertutup
        open_p = raw.count("(")
        close_p = raw.count(")")
        if open_p > close_p:
            raw += ")" * (open_p - close_p)

        res = eval(raw, {"__builtins__": None, "math": math})
        if isinstance(res, float):
            res = round(res, 10)
            if res.is_integer():
                res = int(res)
        st.session_state.expr = str(res)
    except Exception:
        st.session_state.expr = "Error"

# Layar Kalkulator
display_text = st.session_state.expr if st.session_state.expr else "0"
st.markdown(f'<div class="calc-screen">{display_text}</div>', unsafe_allow_html=True)

# Susunan Tombol (Grid 5 Kolom)
buttons = [
    [("sin", "sin("), ("cos", "cos("), ("tan", "tan("), ("DEL", "DEL"), ("AC", "AC")],
    [("√", "√("), ("log", "log("), ("ln", "ln("), ("(", "("), (")", ")")],
    [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "÷"), ("^", "^")],
    [("4", "4"), ("5", "5"), ("6", "6"), ("×", "×"), ("n!", "fact(")],
    [("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"), ("π", "π")],
    [("0", "0"), (".", "."), ("=", "="), ("+", "+"), ("e", str(round(math.e, 6)))]
]

for r_idx, row in enumerate(buttons):
    cols = st.columns(5)
    for c_idx, (label, val) in enumerate(row):
        btn_type = "primary" if label in ["=", "AC"] else "secondary"
        if cols[c_idx].button(label, key=f"btn_{r_idx}_{c_idx}", type=btn_type):
            if val == "AC":
                clear()
            elif val == "DEL":
                backspace()
            elif val == "=":
                calculate()
            else:
                press(val)
            st.rerun()
