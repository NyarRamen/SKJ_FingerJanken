import streamlit as st
import random

def SKJ_janken(player_hand):
    hands = ["1", "2", "3", "4", "5"]
    computer_hand = random.choice(hands)

    if player_hand == computer_hand:
        result = "両者負け"
    elif (player_hand == "1" and computer_hand == "5") or \
         (player_hand == "2" and computer_hand == "5") or \
         (player_hand == "5" and computer_hand == "3") or \
         (player_hand == "5" and computer_hand == "4") or \
         (player_hand == "4" and computer_hand == "2") or \
         (player_hand == "4" and computer_hand == "1") or \
         (player_hand == "3" and computer_hand == "2") or \
         (player_hand == "3" and computer_hand == "1"):
        result = "勝ち"

    elif (player_hand == "3" and computer_hand == "4") or \
         (player_hand == "4" and computer_hand == "3"):
        result = "両者勝ち"

    else:
        result = "負け"

    return computer_hand, result

def main():
    st.title("指じゃんけん(SKJvillage)")
    st.write("手を選んでください。")
    player_hand = st.selectbox("あなたの手", ("1", "2", "3", "4", "5"))
    if st.button("じゃんけん！"):
        computer_hand, result = SKJ_janken(player_hand)
        st.write(f"コンピューターの手: {computer_hand}")
        st.write(f"結果: {result}")

if __name__ == "__main__":
    main()
