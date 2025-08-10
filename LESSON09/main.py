import streamlit as st
st.title("ユーザー情報入力")

# session_stateの初期化
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

if 'user_age' not in st.session_state:
    st.session_state.user_age = ""
    
if 'user_hobby' not in st.session_state:
    st.session_state.user_hobby = ""

if 'user_food' not in st.session_state:
    st.session_state.user_food = ""

if 'user_movie' not in st.session_state:
    st.session_state.user_movie = ""
# ユーザー名の入力
name = st.text_input("あなたの名前を入力してください")
if st.button("名前を保存"):
    st.session_state.user_name = name
    st.success("名前を保存しました!")

age = st.text_input("あなたの年齢を入力してください")
if st.button("年齢を保存"):
    st.session_state.user_age = age
    st.success("年齢を保存しました!")

hobby = st.text_input("あなたの趣味を教えてください")
if st.button("趣味の保存"):
    st.session_state.user_hobby = hobby
    st.success("名前を保存しました！")

food = st.text_input("あなたの好きな食べ物を教えてください")
if st.button("好きな食べ物の保存"):
    st.session_state.user_food = food
    st.success("好きな食べ物を保存しました！")

movie = st.text_input("あなたの好きな映画を教えてください")
if st.button("好きな映画の保存"):
    st.session_state.user_movie = movie
    st.success("好きな映画を保存しました")

st.write(f"現在保存されている名前: {st.session_state.user_name}")
st.write(f"現在保存されている年齢: {st.session_state.user_age}")
st.write(f"現在保存されている趣味: {st.session_state.user_hobby}")
st.write(f"現在保存されている好きな食べ物: {st.session_state.user_food}")
st.write(f"現在保存されている好きな映画:{st.session_state.user_movie}")