#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'NanumGothic'


# In[2]:


location = pd.read_csv("영업소찾기 (1).csv")


# In[3]:


location


# In[4]:


time = pd.read_csv("2019-2023통행시간.csv",encoding="cp949")


# In[5]:


time


# In[7]:


df = pd.merge(location, time, left_on="영업소코드", right_on="도착", how="right")
df


# In[8]:


df = df.drop(["본부", "지사", "영업소", "우편번호(5자리)"], axis=1)
df = df[df.통행 != -1] #결측치제거 
df


# In[9]:


df['통행시간'] = df["통행"]/3600
df['통행분'] = df["통행"]/60


# In[173]:


df


# # 부산

# In[10]:


busan = df[df["주소"].str.contains('부산광역시', na=False)]
daejeon = df[df["주소"].str.contains('대전광역시', na=False)]
gang = df[df["주소"].str.contains('강릉', na=False)]
busan


# In[11]:


daejeon


# In[12]:


busan["ymd"] = pd.to_datetime(busan["ymd"], format="%Y%m%d%H%M%S")
busan["year"] = busan["ymd"].dt.year
busan["MonthDay"] = busan["ymd"].dt.strftime('%m-%d')


# In[15]:


daejeon["ymd"] = pd.to_datetime(daejeon["ymd"], format="%Y%m%d%H%M%S")
daejeon["year"] = daejeon["ymd"].dt.year
daejeon["MonthDay"] = daejeon["ymd"].dt.strftime('%m-%d')


# In[16]:


gang["ymd"] = pd.to_datetime(gang["ymd"], format="%Y%m%d%H%M%S")
gang["year"] = gang["ymd"].dt.year
gang["MonthDay"] = gang["ymd"].dt.strftime('%m-%d')


# In[51]:


tmp = busan[busan["영업소명"]=="서부산"].sort_values(["ymd"])
tmpdae = daejeon[daejeon["영업소명"]=="대전"].sort_values(["ymd"])
tmpgang = gang[gang["영업소명"]=="강릉"].sort_values(["ymd"])
tmp


# In[53]:


tmp["ymd"] = pd.to_datetime(tmp["ymd"], format="%Y%m%d%H%M%S")
tmp["year"] = tmp["ymd"].dt.year
tmp["MonthDay"] = tmp["ymd"].dt.strftime('%m-%d')
tmpdae["ymd"] = pd.to_datetime(tmpdae["ymd"], format="%Y%m%d%H%M%S")
tmpdae["year"] = tmpdae["ymd"].dt.year
tmpdae["MonthDay"] = tmpdae["ymd"].dt.strftime('%m-%d')
tmpgang["ymd"] = pd.to_datetime(tmpgang["ymd"], format="%Y%m%d%H%M%S")
tmpgang["year"] = tmpgang["ymd"].dt.year
tmpgang["MonthDay"] = tmpgang["ymd"].dt.strftime('%m-%d')
tmp


# In[19]:


busan2019=busan[busan["year"]==2019]
daejeon2019=daejeon[daejeon["year"]==2019]
daejeon2020=daejeon[daejeon["year"]==2020]
daejeon2021=daejeon[daejeon["year"]==2021]
daejeon2022=daejeon[daejeon["year"]==2022]
gang2019=gang[gang["year"]==2019]
gang2020=gang[gang["year"]==2020]
gang2021=gang[gang["year"]==2021]
gang2022=gang[gang["year"]==2022]


# In[43]:


print(busan.mode())


# In[49]:


print(gang.mode())


# In[50]:


print(daejeon.mode())


# In[54]:


busan2019 = busan2019[busan2019.통행 != -1]
tmp2019= tmp[tmp["year"]==2019]
tmp2020= tmp[tmp["year"]==2020]
tmp2021= tmp[tmp["year"]==2021]
tmp2022= tmp[tmp["year"]==2022]
tmpdae2019= tmpdae[tmpdae["year"]==2019]
tmpdae2020= tmpdae[tmpdae["year"]==2020]
tmpdae2021= tmpdae[tmpdae["year"]==2021]
tmpdae2022= tmpdae[tmpdae["year"]==2022]
tmpgang2019= tmpgang[tmpgang["year"]==2019]
tmpgang2020= tmpgang[tmpgang["year"]==2020]
tmpgang2021= tmpgang[tmpgang["year"]==2021]
tmpgang2022= tmpgang[tmpgang["year"]==2022]


# In[47]:


tmp2019


# In[48]:


plt.figure(figsize=(20,5))
plt.plot(tmp2019["ymd"], tmp2019["통행시간"])


# In[192]:


import seaborn as sns
ax = sns.boxplot(y=busan2019['통행시간'])  #boxplot


# In[189]:


plt.figure(figsize=(20,5))
plt.plot(busan2019["ymd"], busan2019["통행시간"])


# In[20]:


plt.figure(figsize=(20,5))
plt.plot(daejeon2019["ymd"], daejeon2019["통행시간"])


# In[21]:


plt.figure(figsize=(20,5))
plt.plot(daejeon2020["ymd"], daejeon2020["통행시간"])


# In[22]:


plt.figure(figsize=(20,5))
plt.plot(daejeon2021["ymd"], daejeon2021["통행시간"])


# In[23]:


plt.figure(figsize=(20,5))
plt.plot(daejeon2022["ymd"], daejeon2022["통행시간"])


# In[24]:


plt.figure(figsize=(20,5))
plt.plot(gang2019["ymd"], gang2019["통행시간"])


# In[26]:


plt.figure(figsize=(20,5))
plt.plot(gang2020["ymd"], gang2020["통행시간"])


# In[27]:


plt.figure(figsize=(20,5))
plt.plot(gang2021["ymd"], gang2021["통행시간"])


# In[28]:


plt.figure(figsize=(20,5))
plt.plot(gang2022["ymd"], gang2022["통행시간"])


# In[33]:


busan[busan["집계시"]==8]


# In[42]:


from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.io import output_file, show
from collections import OrderedDict

output_notebook()
p=figure(title="daejeon2019",x_axis_label="ymd",y_axis_label='통행시간')

p.line(daejeon2019["ymd"], daejeon2019["통행시간"],legend="Temp",line_width=2)
p.line(gang2019["ymd"], gang2019["통행시간"],legend="Temp",line_width=2,color='limegreen')
p.line(busan2019["ymd"],busan2019["통행시간"],legend="Temp",line_width=2,color='red')
show(p)


# In[56]:


output_notebook()
p=figure(title="2019",x_axis_label="ymd",y_axis_label='통행시간')

p.line(tmpdae2019["ymd"], tmpdae2019["통행시간"],legend="Temp",line_width=2)
p.line(tmpgang2019["ymd"], tmpgang2019["통행시간"],legend="Temp",line_width=2,color='limegreen')
p.line(tmp2019["ymd"],tmp2019["통행시간"],legend="Temp",line_width=2,color='red')
show(p)


# In[ ]:




