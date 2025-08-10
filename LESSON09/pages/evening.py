import streamlit as st
st.title("👤 ユーザー情報表示ページ")

# session_stateからデータを取得
if 'user_name' in st.session_state and st.session_state.user_name:
    st.success(f"🎉 こんにちは、{st.session_state.user_name}さん！")
    st.write("メインページで入力された名前が正しく表示されています。")

    # 追加の表示
    st.balloons()  # 祝福のアニメーション

else:
    st.error("❌ ユーザー名が設定されていません")
    st.write("メインページで名前を入力してください")

if 'user_age' in st.session_state and st.session_state.user_name:
    st.success(f"🎉 こんにちは、{st.session_state.user_age}さん！")
    st.write("メインページで入力された年齢が正しく表示されています。")

    # 追加の表示
    st.balloons()  # 祝福のアニメーション

else:
    st.error("❌ 年齢が設定されていません")
    st.write("メインページで年齢を入力してください")

if 'user_hobby' in st.session_state and st.session_state.user_name:
    st.success(f"🎉 こんにちは、{st.session_state.user_hobby}さん！")
    st.write("メインページで入力された趣味が正しく表示されています。")

    # 追加の表示
    st.balloons()  # 祝福のアニメーション

else:
    st.error("❌ 趣味が設定されていません")
    st.write("メインページで趣味を入力してください")