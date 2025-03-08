import streamlit as st
import secrets
import sys
import os
from streamlit import session_state as ss

# Create css directory if it doesn't exist
css_dir = "css"
if not os.path.exists(css_dir):
    os.makedirs(css_dir)

# Create style.css file with improved styling
css_path = os.path.join(css_dir, "style.css")
if not os.path.exists(css_path):
    with open(css_path, "w") as f:
        f.write("""/* Main container styling */
body {
    background-color: #1E1E2E;
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header styling */
h1, h2, h3 {
    color: #cbdced;
    font-weight: 700;
}

/* Game card styling */
.css-1r6slb0, .css-keje6w {
    border-radius: 12px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    background-color: #2D2D44;
    border: 1px solid #3D3D5C;
}

/* Button styling */
.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.7rem 1.2rem;
    transition: all 0.3s ease;
    background-color: #4F46E5;
    color: white;
    border: none;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
    background-color: #4338CA;
}

/* Success button styling */
button[kind="primary"] {
    background-color: #10B981;
}

/* Input fields styling */
.stNumberInput, .stTextInput {
    background-color: #2D2D44;
    border-radius: 8px;
    padding: 0.5rem;
    border: 1px solid #4F46E5;
}

.stNumberInput input, .stTextInput input {
    color: white !important;
}

/* Balance display styling */
[data-testid="stMetricValue"] {
    font-size: 2.5rem !important;
    font-weight: 700 !important;
    color: #10B981 !important;
    text-shadow: 0 0 10px rgba(16, 185, 129, 0.3);
}

/* Game result styling */
.element-container div[data-testid="stAlert"] {
    border-radius: 8px;
    font-weight: 600;
    padding: 1rem;
}

/* Footer styling */
footer {
    font-size: 0.8rem;
    color: #6B7280;
    text-align: center;
    margin-top: 2rem;
}

/* Hide Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Custom footer */
.custom-footer {
    position: relative;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
    padding: 1rem;
    font-size: 0.8rem;
    color: #6B7280;
    margin-top: 3rem;
}

/* Animated background for win screen */
@keyframes gradient {
    0% {background-position: 0% 50%}
    50% {background-position: 100% 50%}
    100% {background-position: 0% 50%}
}

.win-animation {
    background: linear-gradient(-45deg, #10B981, #4F46E5, #10B981);
    background-size: 400% 400%;
    animation: gradient 3s ease infinite;
    border-radius: 10px;
    padding: 2rem;
    color: white;
    text-align: center;
    margin: 1rem 0;
}

/* Custom card styling */
.custom-card {
    background-color: #2D2D44;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    margin: 1rem 0;
    border: 1px solid #3D3D5C;
}

/* Game logo styling */
.game-logo {
    text-align: center;
    margin-bottom: 1.5rem;
}

.game-logo h1 {
    font-size: 3rem;
    color: #6366F1;
    text-shadow: 0 0 10px rgba(99, 102, 241, 0.5);
}

.logo-dice {
    font-size: 2.5rem;
    display: inline-block;
    margin: 0 0.5rem;
    transform: rotate(12deg);
}

/* Media query for responsiveness */
@media screen and (max-width: 768px) {
    .main .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}""")

# Apply CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'game_state' not in ss:
    ss.game_state = "welcome"
if 'user_money' not in ss:
    ss.user_money = 0
if 'user_name' not in ss:
    ss.user_name = ""
if 'user_age' not in ss:
    ss.user_age = 0
if 'system_number' not in ss:
    ss.system_number = 0
if 'lucky_number' not in ss:
    ss.lucky_number = 0
if 'input_money' not in ss:
    ss.input_money = 0
if 'game_result' not in ss:
    ss.game_result = ""
if 'win_streak' not in ss:
    ss.win_streak = 0

# Function to generate secure random number
def get_random_number():
    secure_number = secrets.SystemRandom()
    return secure_number.randint(a=10, b=99)

# Custom components
def custom_card(title, content):
    st.markdown(f"""
    <div class="custom-card">
        <h3>{title}</h3>
        {content}
    </div>
    """, unsafe_allow_html=True)

# Set page config
st.set_page_config(
    page_title="Lucky Number Game",
    page_icon="🎲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
local_css(css_path)

# Remove streamlit branding
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Main title with custom logo
st.markdown("""
<div class="game-logo">
    <h1><span class="logo-dice">🎲</span> Lucky Number Game <span class="logo-dice">🎲</span></h1>
    <p style="font-size: 1.2rem; color: #A5B4FC;">Test your luck and win big!</p>
</div>
""", unsafe_allow_html=True)

# Welcome screen
if ss.game_state == "welcome":
    col1, col2 = st.columns([2, 3])
    
    with col1:
        st.markdown("""
        <div style="background-color: #4F46E5; color: white; padding: 1.5rem; border-radius: 12px; text-align: center;">
            <h2 style="color: white;">Welcome to the Game!</h2>
            <p>Experience the thrill of the Lucky Number Game</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### How to Play")
        st.markdown("1. Register with your details")
        st.markdown("2. Make your initial deposit")
        st.markdown("3. Choose your lucky number")
        st.markdown("4. Win big if you guess correctly!")
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Ready to Start?")
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("📜 Read the Rules", use_container_width=True):
                ss.game_state = "rules"
        with col_b:
            if st.button("🎮 Play the Game", use_container_width=True):
                ss.game_state = "registration"
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Custom dice animation instead of Streamlit logo
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem;">
            <div style="font-size: 3rem; animation: bounce 1s infinite alternate;">🎲</div>
            <style>
                @keyframes bounce {
                    from { transform: translateY(0); }
                    to { transform: translateY(-10px); }
                }
            </style>
        </div>
        """, unsafe_allow_html=True)

# Rules screen
elif ss.game_state == "rules":
    st.markdown("""
    <div style="background-color: #2D2D44; padding: 2rem; border-radius: 12px; border-left: 5px solid #4F46E5;">
        <h2>Game Rules</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Player Requirements:")
        st.markdown("- 🔞 User age must be at least 18")
        st.markdown("- 💰 Deposit money more than $5000")
        st.markdown("- 🎮 You must bet more than $1000 each time you play")
        
        st.markdown("### How to Win:")
        st.markdown("- Choose your lucky number between 10-99")
        st.markdown("- If you guess the lucky number (20), you win 10x your bet!")
        st.markdown("- If you don't guess correctly, you lose your bet amount")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Ready to Play?")
        st.markdown("Click the button below to start your gaming journey!")
        
        if st.button("🎮 Start Playing Now", use_container_width=True):
            ss.game_state = "registration"
        st.markdown("</div>", unsafe_allow_html=True)

# Registration screen
elif ss.game_state == "registration":
    st.markdown("""
    <div style="background-color: #2D2D44; padding: 2rem; border-radius: 12px; border-left: 5px solid #10B981;">
        <h2>Player Registration</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Enter Your Details")
        
        ss.user_name = st.text_input("Enter your name:", value=ss.user_name, placeholder="John Doe")
        ss.user_age = st.number_input("Enter your age:", min_value=0, max_value=120, value=ss.user_age if ss.user_age > 0 else 18, step=1)
        
        if st.button("Register & Continue", use_container_width=True):
            if len(ss.user_name) > 2 and ss.user_age > 17:
                ss.game_state = "deposit"
            else:
                st.error("Please read the rules carefully. You must be at least 18 years old and provide a valid name.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Why Register?")
        st.markdown("- Track your winnings")
        st.markdown("- Personalized gaming experience")
        st.markdown("- Save your progress")
        st.markdown("</div>", unsafe_allow_html=True)

# Initial deposit screen
elif ss.game_state == "deposit":
    st.markdown(f"""
    <div style="background-color: #2D2D44; padding: 2rem; border-radius: 12px; border-left: 5px solid #F59E0B;">
        <h2>Welcome, {ss.user_name}! 🎉</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Make Your Initial Deposit")
        st.markdown("To start playing, you need to deposit at least $5,000.")
        
        deposit_values = [5000, 10000, 25000, 50000, 100000]
        deposit_cols = st.columns(len(deposit_values))
        
        for i, val in enumerate(deposit_values):
            with deposit_cols[i]:
                if st.button(f"${val:,}", key=f"quick_deposit_{val}"):
                    ss.user_money = val
        
        ss.user_money = st.number_input("Or enter custom amount ($):", min_value=0, value=ss.user_money, step=1000)
        
        if st.button("Confirm Deposit & Start Playing", use_container_width=True):
            if ss.user_money > 4999:
                ss.game_state = "game"
            else:
                st.error("Please deposit at least $5000 to play.")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Deposit Benefits")
        st.markdown("- Larger deposits mean more gameplay")
        st.markdown("- Win up to 10x your bet amount")
        st.markdown("- Withdraw your winnings anytime")
        st.markdown("</div>", unsafe_allow_html=True)

# Game screen
elif ss.game_state == "game":
    # Display current balance prominently
    st.metric("Your Balance", f"${ss.user_money:,}")
    
    st.markdown("""
    <div style="background-color: #2D2D44; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #4F46E5; margin-bottom: 1rem;">
        <h2>Time to Play!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Place Your Bet")
        
        # Quick bet buttons (25%, 50%, 75%, MAX)
        bet_cols = st.columns(4)
        with bet_cols[0]:
            if st.button("25%", key="bet_25"):
                ss.input_money = max(1000, int(ss.user_money * 0.25))
        with bet_cols[1]:
            if st.button("50%", key="bet_50"):
                ss.input_money = max(1000, int(ss.user_money * 0.5))
        with bet_cols[2]:
            if st.button("75%", key="bet_75"):
                ss.input_money = max(1000, int(ss.user_money * 0.75))
        with bet_cols[3]:
            if st.button("MAX", key="bet_max"):
                ss.input_money = ss.user_money
        
        ss.input_money = st.number_input("Bet amount ($):", 
                                        min_value=1000, 
                                        max_value=ss.user_money, 
                                        value=min(ss.input_money if ss.input_money >= 1000 else 1000, ss.user_money), 
                                        step=1000)
        
        st.markdown("### Choose Your Lucky Number")
        
        # Lucky number selector with quick picks
        lucky_cols = st.columns(5)
        for i, num in enumerate([10, 20, 42, 69, 99]):
            with lucky_cols[i]:
                if st.button(f"{num}", key=f"lucky_{num}"):
                    ss.lucky_number = num
        
        ss.lucky_number = st.number_input("Your lucky number:", 
                                          min_value=10, 
                                          max_value=99, 
                                          value=ss.lucky_number if 10 <= ss.lucky_number <= 99 else 20, 
                                          step=1)
        
        if st.button("🎲 PLAY NOW!", use_container_width=True):
            if ss.input_money < 1000:
                st.error("Minimum bet is $1000.")
            elif ss.input_money > ss.user_money:
                st.error("You cannot bet more than your balance.")
            else:
                # Generate system number
                ss.system_number = get_random_number()
                
                # Check if player won
                if ss.lucky_number == 20:  # Winning condition
                    ss.user_money = (ss.input_money * 10) + (ss.user_money - ss.input_money)
                    ss.game_result = "win"
                    ss.win_streak += 1
                else:
                    ss.user_money = ss.user_money - ss.input_money
                    ss.game_result = "lose"
                    ss.win_streak = 0
                
                ss.game_state = "result"
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Game Tips")
        st.markdown("- The winning number is 20")
        st.markdown("- Win 10x your bet amount!")
        st.markdown("- Minimum bet: $1,000")
        st.markdown("- You can play as many times as you want")
        st.markdown("</div>", unsafe_allow_html=True)
        
        if ss.win_streak > 0:
            st.markdown(f"""
            <div style="background-color: #10B981; color: white; padding: 1rem; border-radius: 10px; text-align: center; margin-top: 1rem;">
                <h3 style="color: white;">🔥 Win Streak: {ss.win_streak} 🔥</h3>
            </div>
            """, unsafe_allow_html=True)

# Result screen
elif ss.game_state == "result":
    # Display updated balance
    st.metric("Your Balance", f"${ss.user_money:,}")
    
    if ss.game_result == "win":
        st.markdown("""
        <div class="win-animation">
            <h2 style="color: white; font-size: 2.5rem;">🎉 YOU WON!!! 🎉</h2>
            <p style="font-size: 1.5rem;">Congratulations on your amazing win!</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown(f"### You guessed the lucky number: {ss.lucky_number}!")
            st.markdown(f"You bet ${ss.input_money:,} and won ${ss.input_money * 10:,}!")
            st.markdown(f"### Win streak: {ss.win_streak}")
            
            play_cols = st.columns(2)
            with play_cols[0]:
                if st.button("🎮 Play Again", use_container_width=True):
                    ss.game_state = "game"
            with play_cols[1]:
                if st.button("💰 Cash Out", use_container_width=True):
                    ss.game_state = "cash_out"
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown("### Why not try again?")
            st.markdown("- Keep your winning streak going!")
            st.markdown("- Multiple wins multiply your fortune")
            st.markdown("- Cash out anytime")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background-color: #3D2D44; padding: 1.5rem; border-radius: 12px; border-left: 5px solid #EF4444; margin-bottom: 1rem;">
            <h2>Oops! Not Lucky This Time</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown(f"### You guessed: {ss.lucky_number}")
            st.markdown(f"The lucky number was: {ss.system_number}")
            st.markdown(f"You lost ${ss.input_money:,}")
            
            # Check if player has enough money to continue
            if ss.user_money < 1000:
                st.warning(f"Not enough money (${ss.user_money:,}). Please deposit more to continue playing.")
                if st.button("💰 Deposit More", use_container_width=True):
                    ss.game_state = "deposit"
            else:
                play_cols = st.columns(2)
                with play_cols[0]:
                    if st.button("🎮 Try Again", use_container_width=True):
                        ss.game_state = "game"
                with play_cols[1]:
                    if st.button("💰 Cash Out", use_container_width=True):
                        ss.game_state = "cash_out"
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="custom-card">', unsafe_allow_html=True)
            st.markdown("### Remember")
            st.markdown("- The lucky number is 20")
            st.markdown("- Each play is a new chance to win")
            st.markdown("- Good luck on your next try!")
            st.markdown("</div>", unsafe_allow_html=True)

# Cash out screen
elif ss.game_state == "cash_out":
    st.markdown("""
    <div style="background-color: #2D2D44; padding: 2rem; border-radius: 12px; border-left: 5px solid #10B981; margin-bottom: 1rem;">
        <h2>Thank You For Playing!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown(f"### Congratulations, {ss.user_name}!")
        st.markdown(f"You're cashing out with **${ss.user_money:,}**")
        
        if ss.user_money > 5000:
            profit = ss.user_money - 5000
            st.markdown(f"Your profit: **${profit:,}**")
            st.success(f"You've made a profit of {profit/5000*100:.1f}%!")
        else:
            loss = 5000 - ss.user_money
            st.markdown(f"Your loss: **${loss:,}**")
            st.warning(f"Better luck next time!")
            
        final_cols = st.columns(2)
        with final_cols[0]:
            if st.button("🎮 Play Again", use_container_width=True):
                # Reset game but keep player info
                ss.user_money = 0
                ss.win_streak = 0
                ss.game_state = "deposit"
        with final_cols[1]:
            if st.button("🚪 Exit Game", use_container_width=True):
                # Reset everything
                for key in ss.keys():
                    del ss[key]
                ss.game_state = "welcome"
                st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown("### Game Summary")
        st.markdown(f"- Player: {ss.user_name}")
        st.markdown(f"- Final Balance: ${ss.user_money:,}")
        if ss.win_streak > 0:
            st.markdown(f"- Win Streak: {ss.win_streak}")
            
        st.markdown("### Thank you for playing!")
        st.markdown("We hope to see you again soon.")
        st.markdown("</div>", unsafe_allow_html=True)

# Custom footer (replacing Streamlit footer)
st.markdown("""
<div class="custom-footer">
    <p>Lucky Number Game &copy; 2025 | For entertainment purposes only</p>
</div>
""", unsafe_allow_html=True)