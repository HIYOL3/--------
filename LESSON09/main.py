import streamlit as st
st.title("ユーザー情報入力")

# session_stateの初期化
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if 'user_age' not in st.session_state:
    st.session_state.user_age = ""
    
if 'user_hobby' not in st.session_state:
    st.session_state.user_hobby = ""
# ユーザー名の入力
name = st.text_input("あなたの名前を入力してください")
if st.button("名前を保存"):
    st.session_state.user_name = name
    st.success("名前を保存しました!")

age = st.text_input("あなたの年齢を入力してください")
if st.button("年齢を保存"):
    st.session_state.user_name = age
    st.success("年齢を保存しました!")

hobby = st.text_input("あなたの趣味を教えてください")
if st.button("趣味の保存"):
    st.session_state.user_hobby = hobby
    st.success("名前を保存しました！")

st.write(f"現在保存されている名前: {st.session_state.user_name}")
st.write(f"現在保存されている年齢: {st.session_state.user_age}")
st.write(f"現在保存されている趣味: {st.session_state.user_hobby}")