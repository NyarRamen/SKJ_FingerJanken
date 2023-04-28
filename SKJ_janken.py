import streamlit as st
import random
from PIL import Image

def explain_game():
    st.title("指じゃんけんの遊び方")
    st.write("ここでは、SKJvillageの動画内で現れた謎ゲーム、指じゃんけんのルールを説明します。")
    st.header("ルール")
    st.write("・出す手は1から５")
    st.write("・基本的には数字が大きい方が勝ち")
    st.write("・同じ数字は両者負け")
    st.write("・1は5に勝てる")
    st.write("・2は5に勝てる(ここだけ2がチョキ✌, 5がパー✋になり普通のじゃんけんになる)")
    st.write("・3と4の場合は両者勝ち")
    st.header("操作")
    st.write("左のサイドバーを開き、selectで「指じゃんけんプレイ！」を選択")
    st.write("対戦相手を「sa2,サイカツ,シンカ」から選択")
    st.write("出す手を「1,2,3,4,5」から選択")
    st.write("「じゃんけん！」ボタンを押すとじゃんけん開始！")
    st.write("相手の手と勝敗，対戦相手と勝敗に応じて画像出現！")
    st.header("参考")
    st.write("https://www.youtube.com/watch?v=i__b6owlvhk")
    st.write("【大爆笑】ゴールは目の前なのに…マリメ面白すぎるだろ!!!!")

def SKJ_janken(youkai_enemy,player_hand):
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
        result = "あなたの勝ち"

    elif (player_hand == "3" and computer_hand == "4") or \
         (player_hand == "4" and computer_hand == "3"):
        result = "両者勝ち"

    else:
        result = "あなたの負け"

    if youkai_enemy == "sa2":
        if result == "あなたの勝ち":
            img = Image.open('SKJ_janken_image/sa2負け.jpg')
        elif result == "あなたの負け":
            img = Image.open('SKJ_janken_image/sa2勝ち.jpg')
        elif result == "両者勝ち":
            img = Image.open('SKJ_janken_image/sa2両者勝ち.jpg')
        else:
            img = Image.open('SKJ_janken_image/sa2両者負け.jpg')

    if youkai_enemy == "サイカツ":
        if result == "あなたの勝ち":
            img = Image.open('SKJ_janken_image/サイカツ負け.jpg')
        elif result == "あなたの負け":
            img = Image.open('SKJ_janken_image/サイカツ勝ち.jpg')
        elif result == "両者勝ち":
            img = Image.open('SKJ_janken_image/サイカツ両者勝ち.jpg')
        else:
            img = Image.open('SKJ_janken_image/サイカツ両者負け.jpg')

    if youkai_enemy == "シンカ":
        if result == "あなたの勝ち":
            img = Image.open('SKJ_janken_image/シンカ負け.jpg')
        elif result == "あなたの負け":
            img = Image.open('SKJ_janken_image/シンカ勝ち.jpg')
        elif result == "両者勝ち":
            img = Image.open('SKJ_janken_image/シンカ両者勝ち.jpg')
        else:
            img = Image.open('SKJ_janken_image/シンカ両者負け.jpg')

    return computer_hand, result, img

def play_game():
    st.title("指じゃんけん(SKJvillage)")
    st.header("対戦相手を選んでください。")
    youkai_enemy = st.selectbox("対戦相手", ("sa2", "サイカツ", "シンカ"))
    st.header("手を選んでください。")
    player_hand = st.selectbox("あなたの手", ("1", "2", "3", "4", "5"))
    if st.button("じゃんけん！"):
        computer_hand, result, img = SKJ_janken(youkai_enemy,player_hand)
        st.write(f"{youkai_enemy}の手: {computer_hand}")
        st.write(f"結果: {result}")
        st.image(img)

def main():
    apps = {"-": None,
            "指じゃんけんプレイ！":play_game,
            "遊び方":explain_game}

    selected_app_name = st.sidebar.selectbox(label='select',options=list(apps.keys()))

    if selected_app_name == "-":
        st.title("指じゃんけん(SKJvillage)")
        st.info("サイドバーのselectから選択してね")
        st.subheader("SKJvillageとは")
        image = Image.open('SKJ_janken_image/skjvillage.png')
        st.image(image)
        st.write("３人組YouTuberのSKJvillageです！")
        st.write("高校時代の親友で「早稲田・慶應・上智」大学にそれぞれ進学")
        st.write("大手企業を退職後、３人でYoutube活動開始。")
        st.write("https://www.youtube.com/@SKJVillage/about")
        st.write("SKJvillageのチャンネル概要より抜粋")
        st.stop()

    render_func = apps[selected_app_name]
    render_func()

if __name__ == "__main__":
    main()
