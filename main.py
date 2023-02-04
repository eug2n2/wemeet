#%%"
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'NanumGothic'
import streamlit as st

from bokeh.plotting import figure,show
from bokeh.io import show


df = pd.read_csv("tong.csv")
df["ymd"] = pd.to_datetime(df["ymd"], format="%Y%m%d%H%M%S")
df["year"] = df["ymd"].dt.year
df["MonthDay"] = df["ymd"].dt.strftime('%m-%d')
daegu = df[df["주소"].str.contains('대구광역시', na=False)]
busan = df[df["주소"].str.contains('부산광역시', na=False)]
daejeon = df[df["주소"].str.contains('대전광역시', na=False)]
ulsan= df[df["주소"].str.contains('울산광역시', na=False)]
gang = df[df["주소"].str.contains('강릉광역시', na=False)]

#대구
daegu["통행시간"] = daegu["통행시간"].fillna(daegu.groupby(["year","시"])["통행시간"].transform('mean'))
daegu_ymd = daegu.groupby("ymd").mean()
years = daegu['year'].unique()
daegu_ymd = daegu_ymd.sort_values(["ymd"])
daegu_ymd = daegu_ymd.reset_index()
daegu_ymd["order"] = daegu_ymd.groupby("year")["날짜"].rank(method="dense", ascending=True)
daegu_ymd = daegu_ymd.reset_index()
daegu_ymd["order2"] = daegu_ymd.groupby("year")["ymd"].rank(method="dense", ascending=True)
daegu_ymd = daegu_ymd[daegu_ymd["order"]<=6]
years = daegu_ymd['year'].unique()
years = years.astype(int)

#부산
busan["통행시간"] = busan["통행시간"].fillna(busan.groupby(["year","시"])["통행시간"].transform('mean'))
busan_ymd = busan.groupby("ymd").mean()
years = busan['year'].unique()
busan_ymd = busan_ymd.sort_values(["ymd"])
busan_ymd = busan_ymd.reset_index()
busan_ymd["order"] = busan_ymd.groupby("year")["날짜"].rank(method="dense", ascending=True)
busan_ymd = busan_ymd.reset_index()
busan_ymd["order2"] = busan_ymd.groupby("year")["ymd"].rank(method="dense", ascending=True)
busan_ymd = busan_ymd[busan_ymd["order"]<=6]
years = busan_ymd['year'].unique()
years = years.astype(int)

#대전
daejeon["통행시간"] = daejeon["통행시간"].fillna(daejeon.groupby(["year","시"])["통행시간"].transform('mean'))
daejeon_ymd = daejeon.groupby("ymd").mean()
years = daejeon['year'].unique()
daejeon_ymd = daejeon_ymd.sort_values(["ymd"])
daejeon_ymd = daejeon_ymd.reset_index()
daejeon_ymd["order"] = daejeon_ymd.groupby("year")["날짜"].rank(method="dense", ascending=True)
daejeon_ymd = daejeon_ymd.reset_index()
daejeon_ymd["order2"] = daejeon_ymd.groupby("year")["ymd"].rank(method="dense", ascending=True)
daejeon_ymd = daejeon_ymd[daejeon_ymd["order"]<=6]
years = daejeon_ymd['year'].unique()
years = years.astype(int)

#강릉
gang["통행시간"] = gang["통행시간"].fillna(gang.groupby(["year","시"])["통행시간"].transform('mean'))
gang_ymd = gang.groupby("ymd").mean()
years = gang['year'].unique()
gang_ymd = gang_ymd.sort_values(["ymd"])
gang_ymd = gang_ymd.reset_index()
gang_ymd["order"] = gang_ymd.groupby("year")["날짜"].rank(method="dense", ascending=True)
gang_ymd = gang_ymd.reset_index()
gang_ymd["order2"] = gang_ymd.groupby("year")["ymd"].rank(method="dense", ascending=True)
gang_ymd = gang_ymd[gang_ymd["order"]<=6]
years = gang_ymd['year'].unique()
years = years.astype(int)
#울산
ulsan["통행시간"] = ulsan["통행시간"].fillna(ulsan.groupby(["year","시"])["통행시간"].transform('mean'))
ulsan_ymd = ulsan.groupby("ymd").mean()
years = gang['year'].unique()
ulsan_ymd = ulsan_ymd.sort_values(["ymd"])
ulsan_ymd = ulsan_ymd.reset_index()
ulsan_ymd["order"] = ulsan_ymd.groupby("year")["날짜"].rank(method="dense", ascending=True)
ulsan_ymd = ulsan_ymd.reset_index()
ulsan_ymd["order2"] = ulsan_ymd.groupby("year")["ymd"].rank(method="dense", ascending=True)
ulsan_ymd = ulsan_ymd[ulsan_ymd["order"]<=6]
years = ulsan_ymd['year'].unique()
years = years.astype(int)



# Create Radio Buttons
region= ['대구', '부산','대전','울산' ,'강릉']
status = st.radio("서울에서 출발할 지역을 선택하세요", region)
    # Create Radio Buttons
options = ['2019년', '2020년','2021년', '2022년', '2023년',"ALL"]
syear = st.radio("연도를 선택하세요!!", options,horizontal=True)

if status == region[0]: #대구
    if syear == options[0]:
        s=plt.figure(figsize=(20,5))
        plt.title("2019년 서울->대구 통행시간", fontsize=15)
        d = daegu_ymd[(daegu_ymd["year"]==2019)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2019), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

    elif syear == options[1]:
        s=plt.figure(figsize=(20,5))
        plt.title("2020년 서울->대구 통행시간", fontsize=15)
        d = daegu_ymd[(daegu_ymd["year"]==2020)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2020), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

    elif syear == options[2]:
        s=plt.figure(figsize=(20,5))
        plt.title("2021년 서울->대구 통행시간", fontsize=15)
        d = daegu_ymd[(daegu_ymd["year"]==2021)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[3]:
        s=plt.figure(figsize=(20,5))
        plt.title("2022년 서울->대구 통행시간", fontsize=15)
        d = daegu_ymd[(daegu_ymd["year"]==2022)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[4]:
        s=plt.figure(figsize=(20,5))
        plt.title("2023년 서울->대구 통행시간", fontsize=15)
        d = daegu_ymd[(daegu_ymd["year"]==2023)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2023), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)
    else:
        s=plt.figure(figsize=(20,5))
        plt.title("연도별 서울->대구 통행시간", fontsize=15)
        for y in years:
            d = daegu_ymd[(daegu_ymd["year"]==y)]
            x = d["날짜"]
            plt.plot(d["order2"], d["통행시간"], "-", label=str(y), alpha=.6)
            plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)   

elif status == region[1]:  #busan
    if syear == options[0]:
        s=plt.figure(figsize=(20,5))
        plt.title("2019년 서울->부산 통행시간", fontsize=15)
        d = busan_ymd[(busan_ymd["year"]==2019)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2019), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

    elif syear == options[1]:
        s=plt.figure(figsize=(20,5))
        plt.title("2020년 서울->부산 통행시간", fontsize=15)
        d = busan_ymd[(busan_ymd["year"]==2020)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2020), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

    elif syear == options[2]:
        s=plt.figure(figsize=(20,5))
        plt.title("2021년 서울->부산 통행시간", fontsize=15)
        d = busan_ymd[(busan_ymd["year"]==2021)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[3]:
        s=plt.figure(figsize=(20,5))
        plt.title("2022년 서울->부산 통행시간", fontsize=15)
        d = busan_ymd[(busan_ymd["year"]==2022)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2022), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[4]:
        s=plt.figure(figsize=(20,5))
        plt.title("2023년 서울->부산 통행시간", fontsize=15)
        d = busan_ymd[(busan_ymd["year"]==2023)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2023), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)
    
    else:
        s=plt.figure(figsize=(20,5))
        plt.title("연도별 서울-> 부산 통행시간", fontsize=15)
        for y in years:
            d = busan_ymd[(busan_ymd["year"]==y)]
            x = d["날짜"]
            plt.plot(d["order2"], d["통행시간"], "-", label=str(y), alpha=.6)
            plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)     

elif status == region[2]: # 대전
    if syear == options[0]:
        s=plt.figure(figsize=(20,5))
        plt.title("2019년 서울-> 대전 통행시간", fontsize=15)
        d = daejeon_ymd[(daejeon_ymd["year"]==2019)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2019), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

    elif syear == options[1]:
        s=plt.figure(figsize=(20,5))
        plt.title("2020년 서울-> 대전 통행시간", fontsize=15)
        d = daejeon_ymd[(daejeon_ymd["year"]==2020)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2020), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

    elif syear == options[2]:
        s=plt.figure(figsize=(20,5))
        plt.title("2021년 서울-> 대전 통행시간", fontsize=15)
        d = daejeon_ymd[(daejeon_ymd["year"]==2021)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[3]:
        s=plt.figure(figsize=(20,5))
        plt.title("2022년 서울-> 대전 통행시간", fontsize=15)
        d = daejeon_ymd[(daejeon_ymd["year"]==2022)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2022), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[4]:
        s=plt.figure(figsize=(20,5))
        plt.title("2023년 서울->대전 통행시간", fontsize=15)
        d = daejeon_ymd[(daejeon_ymd["year"]==2023)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2023), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)
    else:
        s=plt.figure(figsize=(20,5))
        plt.title("연도별 서울->대전 통행시간", fontsize=15)
        for y in years:
            d = daejeon_ymd[(daejeon_ymd["year"]==y)]
            x = d["날짜"]
            plt.plot(d["order2"], d["통행시간"], "-", label=str(y), alpha=.6)
            plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

elif status == region[3]: #울산
    if syear == options[0]:
        s=plt.figure(figsize=(20,5))
        plt.title("2019년 서울->울산 통행시간", fontsize=15)
        d = ulsan_ymd[(ulsan_ymd["year"]==2019)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2019), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

    elif syear == options[1]:
        s=plt.figure(figsize=(20,5))
        plt.title("2020년 서울->울산 통행시간", fontsize=15)
        d = ulsan_ymd[(ulsan_ymd["year"]==2020)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2020), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

    elif syear == options[2]:
        s=plt.figure(figsize=(20,5))
        plt.title("2021년 서울->울산 통행시간", fontsize=15)
        d = ulsan_ymd[(ulsan_ymd["year"]==2021)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[3]:
        s=plt.figure(figsize=(20,5))
        plt.title("2022년 서울-> 울산 통행시간", fontsize=15)
        d = ulsan_ymd[(ulsan_ymd["year"]==2022)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2022), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[4]:
        s=plt.figure(figsize=(20,5))
        plt.title("2023년 서울-> 울산 통행시간", fontsize=15)
        d = ulsan_ymd[(ulsan_ymd["year"]==2023)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2023), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)
    else:
        s=plt.figure(figsize=(20,5))
        plt.title("연도별 서울->울산 통행시간", fontsize=15)
        for y in years:
            d = ulsan_ymd[(ulsan_ymd["year"]==y)]
            x = d["날짜"]
            plt.plot(d["order2"], d["통행시간"], "-", label=str(y), alpha=.6)
            plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

else:  #강릉
    if syear == options[0]:
        s=plt.figure(figsize=(20,5))
        plt.title("2019년 서울->강릉 통행시간", fontsize=15)
        d = gang_ymd[(gang_ymd["year"]==2019)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2019), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)    

    elif syear == options[1]:
        s=plt.figure(figsize=(20,5))
        plt.title("2020년 서울-> 강릉 통행시간", fontsize=15)
        d = gang_ymd[(gang_ymd["year"]==2020)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2020), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

    elif syear == options[2]:
        s=plt.figure(figsize=(20,5))
        plt.title("2021년 서울->강릉 통행시간", fontsize=15)
        d = gang_ymd[(gang_ymd["year"]==2021)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2021), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[3]:
        s=plt.figure(figsize=(20,5))
        plt.title("2022년 서울-> 강릉 통행시간", fontsize=15)
        d = gang_ymd[(gang_ymd["year"]==2022)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2022), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)

    elif syear == options[4]:
        s=plt.figure(figsize=(20,5))
        plt.title("2023년 서울-> 강릉 통행시간", fontsize=15)
        d = gang_ymd[(gang_ymd["year"]==2023)]
        x = d["날짜"]
        plt.plot(d["order2"], d["통행시간"], "-", label=str(2023), alpha=.6)
        plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s)
    else:    
        s=plt.figure(figsize=(20,5))
        plt.title("연도별 서울-> 강릉 통행시간", fontsize=15)
        for y in years:
            d = gang_ymd[(gang_ymd["year"]==y)]
            x = d["날짜"]
            plt.plot(d["order2"], d["통행시간"], "-", label=str(y), alpha=.6)
            plt.grid()
        plt.legend(fontsize=13)
        plt.xticks(ticks = np.arange(1,132, 22), labels = ["설연휴 이틀전", "설연휴 하루전", "설 연휴", "설 연휴", "설 당일", "설 연휴"], rotation=90)
        plt.xlabel("날짜")
        plt.ylabel("통행시간")
        st.pyplot(s) 

# %%
