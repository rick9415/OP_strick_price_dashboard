import streamlit as st
import pandas as pd 
import os 
import plotly.express as px
import plotly.figure_factory as ff
import time 


# 指定要扫描的目录路径
directory_path = './'

# 创建一个空列表来存储CSV文件的完整路径
csv_file_paths = []

# 遍历目录中的所有文件和子目录
for root, dirs, files in os.walk(directory_path):
    for file in files:
        # 检查文件扩展名是否为.csv
        if file.endswith(".csv"):
            # 构建完整的文件路径
            file_path = os.path.join(root, file)
            # 将完整路径添加到列表中
            csv_file_paths.append(file_path)

# print(csv_file_paths)
csv_file_paths = sorted(csv_file_paths)

##### plot 
@st.cache_data
def plot_oldf(df):
    df['Mean'] = df.iloc[:,1:].mean(axis=1)
    fig = px.line(df, x=df.columns[0], y=df.columns[1:], labels={'x': 'X轴标签', 'value': 'Price'},height = 650, width = 1300)
    return fig

##### plot 
@st.cache_data
def plot(df):
    df['Mean'] = df.iloc[:,:].mean(axis=1)
    fig = px.line(df, x=df.index, y=df.columns[:], labels={'x': 'X轴标签', 'value': 'Price'},height = 650, width = 1300)
    return fig



##### Streamlit
st.set_page_config(layout="wide")

placeholder = st.empty()
with placeholder.container():

    option = st.selectbox("Pick Data", csv_file_paths)
    df = pd.read_csv(option,index_col=0)
    st.write(df.columns)

    df = df.set_index('time')
    df.index = pd.to_datetime(df.index, format = "%Y-%m-%d %H:%M")
    st.dataframe(df)
    start_time = pd.to_datetime('13:46:00').time()
    end_time = pd.to_datetime('14:59:00').time()
    # df = df[(df.index < start_time) | (df.index > end_time)]

    # 
    #### Plot 
    fig = plot(df)
    st.plotly_chart(fig, use_container_width=False)
    resample = '5T'
    st.write(f'Resample with {resample}')
    df_resample = df.resample('5T').asfreq()
    st.dataframe(df_resample.head())
    fig2 = plot(df_resample)
    st.plotly_chart(fig2, use_container_width=False)
