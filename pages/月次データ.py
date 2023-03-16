import streamlit as st
import pandas as pd
import altair as alt

#ドリンクの月別売上の関数
def monthly_drink_sales():
    #エクセルデータの読み込み
    drink_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="drink", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                drink_data.columns.values,
                                key=1)
    #読み込んだエクセルデータを辞書型に変更
    drink_data_dict = drink_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": drink_data_dict[select_month].keys(),
                        "数量": drink_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のドリンク販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

#肉類の月別売上の関数
def monthly_meat_sales():
    #エクセルデータの読み込み
    meat_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="meat", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                meat_data.columns.values,
                                key=2)
    #読み込んだエクセルデータを辞書型に変更
    meat_data_dict = meat_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": meat_data_dict[select_month].keys(),
                        "数量": meat_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}の肉類販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

#サイドメニューの月別売上
def monthly_sidemenu_sales():
    #エクセルデータの読み込み
    sidemenu_data = pd.read_excel("./data/sales_data/2022sales_data.xlsx", sheet_name="sidemenu", 
                                    engine="openpyxl", index_col=0)
    #販売月のセレクトボックスを作成
    select_month = st.selectbox("月を選んでください",
                                sidemenu_data.columns.values,
                                key=3)
    #読み込んだエクセルデータを辞書型に変更
    sidemenu_data_dict = sidemenu_data.to_dict()
    #辞書に変換されたドリンクのデータから、選択された月のデータフレームを作成
    data = pd.DataFrame({
                        "メニュー": sidemenu_data_dict[select_month].keys(),
                        "数量": sidemenu_data_dict[select_month].values(),
                        })
    #選択された月のデータフレームとグラフを表示
    st.subheader(f"{select_month}のサイドメニュー販売実績")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.dataframe(data)
    with col_2:     
        st.altair_chart(alt.Chart(data).mark_bar().encode(
                    x=alt.X('メニュー', sort=None),
                    y='数量',
                    ),
                    use_container_width=True)

#タイトル
st.markdown(" ### 月次データ")

#ドリンクの月別売上のチェックボックス
if st.checkbox("ドリンク"):
    monthly_drink_sales()
    
#肉類の月別売上のチェックボックス
if st.checkbox("肉類"):
    monthly_meat_sales()

#サイドメニューの月別売上のチェックボックス
if st.checkbox("サイドメニュー"):
    monthly_sidemenu_sales()

#コメント
with st.form(key='monthly_sales_comment'):
    #textbox
    comment = st.text_input("コメントを記入してください")
    submit_btn = st.form_submit_button("登録")
    if submit_btn: #ボタンをクリックしたらコメントを登録する
        with open("./data/sales_data/monthly_sales_comment.txt", "a") as f:
            f.write(f"{comment}")
    with open("./data/sales_data/monthly_sales_comment.txt", "r") as f:
        sales_commnet = f.read()
        sales_commnet
st.markdown(":red[今回は練習用にデータベースの代わりにtxtファイルを使用してます。]")
st.markdown(":red[また今回はコメント登録後の取消し機能も実装していません。]")
st.markdown(":red[monthly_sales_comment.txtを直接編集することは可能です。]")
            

            




    

# side_menu_dict = {} #辞書の初期化
# for side_menu_list in side_menu_lists:
#     #side_menu_dict[side_menu_list] = side_sales_dict
#     side_menu_dict[side_menu_list] ={"January":67, "Februay":77, "March": 81, "April": 73,
#                                       "May":46, "June":98, "July":35, "August":79,
#                                       "September":102, "October":43, "November":51, "December":29}
#st.write(side_menu_dict)
# st.subheader(select_side)
# st.bar_chart(side_menu_dict[select_side])

# user_dict['user_id'] = user_list.user_id
#         user_dict['user_username'] = user_list.user.username
#         user_dict['user_slack_user_id'] = user_list.user.slack_user_id
#         user_dict['plan_stripe_plan_kind'] = user_list.plan.stripe_plan_kind
#         user_dict['created_at'] = user_list.created_at
#         user_dict['canceled_date'] = user_list.canceled_date
#         user_dict['ended_date'] = user_list.ended_date

#matplotlib
# x = ["march", "april"]
# y = [81, 73]
# fig, ax = plt.subplots() #オブジェクト指向型インターフェース
# ax.set_title("Side Menu")
# ax.bar(x, y)
# st.pyplot(fig)

#matplotlib
# x = ["march","aplil"]
# y = [81, 73] 
# # xとyの個数が異なるとエラーになります。
# plt.plot(x,y)
# plt.show()
#https://www.youtube.com/watch?v=8X14vY13U-M

