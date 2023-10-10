import pandas as pd
import time 
df = pd.read_csv("OP_sum_2023-10-06 1104拷貝.csv")
a = {"17000":1000}
# a = {"16400":"271.5","16450":"229.5","16500":"192.0","16600":"160.5","16550":"140.0"}
df = df.set_index("time")
df.index
print(df.index.tolist())

# print(df.head())

df.index = pd.to_datetime(df.index)
# # df.to_csv("test.csv")
# # print(df.head)
# # df.
# # print(df.columns[0])

# print(df.columns[1:])
# print(df.iloc[2,:])
# df.resample('5T')

# print(df.iloc[2,:])




# for i in range(100):


#     df = pd.concat([df, pd.DataFrame(a)], ignore_index=0)
#     df.to_csv("OP_sum_2023-10-06 1104拷貝.csv")
#     time.sleep(1)
#     print(df.tail())



