import streamlit as st
import random


if "user_wins" not in st.session_state:
    st.session_state.user_wins = 0
if "computer_wins" not in st.session_state:
    st.session_state.computer_wins = 0
if "rounds" not in st.session_state:
    st.session_state.rounds = 0
if "current_round" not in st.session_state:
    st.session_state.current_round = 1
if "game_started" not in st.session_state:
    st.session_state.game_started = False

st.title("🎮 Rock Paper Scissors - Play vs Computer")

if not st.session_state.game_started:
    st.session_state.rounds = st.number_input("Enter how many rounds you want to play:", min_value=1, max_value=20, step=1)
    if st.button("Start Game"):
        st.session_state.game_started = True

if st.session_state.game_started:
    st.subheader(f"Round {st.session_state.current_round} of {st.session_state.rounds}")
    
    user_input = None
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🪨 Rock"):
            user_input = "rock"
    with col2:
        if st.button("📄 Paper"):
            user_input = "paper"
    with col3:
        if st.button("✂️ Scissors"):
            user_input = "scissors"

    if user_input:
        options = ["rock", "paper", "scissors"]
        computer_pick = random.choice(options)
        st.write(f"🤖 Computer picked **{computer_pick}**")

        if user_input == computer_pick:
            st.info("It's a Draw!")
        elif (
            (user_input == "rock" and computer_pick == "scissors") or
            (user_input == "paper" and computer_pick == "rock") or
            (user_input == "scissors" and computer_pick == "paper")
        ):
            st.success("You Won this round!")
            st.session_state.user_wins += 1
        else:
            st.error("You Lost this round!")
            st.session_state.computer_wins += 1

        st.session_state.current_round += 1

    st.markdown("---")
    st.write(f"✅ You Won: {st.session_state.user_wins}")
    st.write(f"🤖 Computer Won: {st.session_state.computer_wins}")

    if st.session_state.current_round > st.session_state.rounds:
        st.markdown("---")
        st.header("🎉 Game Over!")
        if st.session_state.user_wins > st.session_state.computer_wins:
            st.success("You are the overall Winner!")
        elif st.session_state.user_wins < st.session_state.computer_wins:
            st.error("Computer Wins overall!")
        else:
            st.info("It's a Tie!")

        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()


# python -m streamlit run rps_app.py