import streamlit as st
from intent_parser import parse_intent
from mock_ai import get_ai_actions
from verifier import verify

# Page config
st.set_page_config(page_title="IntentChain", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        text-align: center;
        color: gray;
    }
    .box {
        padding: 15px;
        border-radius: 10px;
        background-color: #1c1f26;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🛡 IntentChain</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Execution Verification Layer</div>', unsafe_allow_html=True)
st.sidebar.header("⚙️ Policy Settings")

allowed_action = st.sidebar.selectbox("Allowed Action", ["buy", "sell"])
max_amount = st.sidebar.number_input("Max Amount", value=1000)

st.write("")

# Input
prompt = st.text_input("Enter AI Trading Instruction:", placeholder="Buy ETH worth $1000 when price drops below $3000")

run = st.button("🚀 Run Simulation")

if run:

    # Step 1: Parse intent
    intent = parse_intent(prompt)

    # Step 2: Simulate AI attack
    actions = get_ai_actions()

    # Step 3: Verify
    results = verify(intent, actions, allowed_action, max_amount)

    st.divider()

    st.markdown("### 🔍 Simulation Breakdown")

    col1, col2, col3 = st.columns(3)

    # USER INTENT
    with col1:
        st.markdown("#### 🧠 User Intent")
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.json(intent)
        st.markdown('</div>', unsafe_allow_html=True)

    # AI ACTIONS
    with col2:
        st.markdown("#### 🤖 AI Agent Output")
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.json(actions)
        st.markdown('</div>', unsafe_allow_html=True)

    # VERIFICATION
    with col3:
        st.markdown("#### 🛡 IntentChain Protection")
        st.markdown('<div class="box">', unsafe_allow_html=True)

        for act, status in results:
            if status == "BLOCKED":
                st.error(f"{act} → ❌ BLOCKED")
            else:
                st.success(f"{act} → ✅ ALLOWED")

        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    st.markdown("### ⚠️ Attack Detected")

    st.warning("""
    The AI agent attempted an unauthorized transfer not present in the original user intent.
    IntentChain successfully blocked the malicious action.
    """)
