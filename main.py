# -*- coding: utf-8 -*-
import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from sklearn import datasets, linear_model

plt.rcParams['figure.figsize'] = (10, 8) #设置绘图尺寸
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


price = pd.read_excel('data\jiage.xlsx', 'Sheet1', parse_dates=[0], index_col=0, na_values=['NA'])
statics = pd.read_excel('data\jiage.xlsx', 'Sheet2',index_col=0, na_values=['NA'])
print(statics)
#jiage_rencent = pd.Series([1,3,5,np.nan,6,8])
#jiage_rencent = pd.Series([22,23])
#print(jiage_rencent)

#print price.columns
#series = pd.Series('2017.01','2017.02')
def plotFigure(title,filename,df=price,drawdiff=False,xLocator=2,yLocator=100):
    plt.rcParams['figure.figsize'] = (10, 8)  # 设置绘图尺寸
    if drawdiff:
        pass
        diffprices = df.max(axis=1)-df.min(axis=1)
        #diffprices.plot(grid=True)
        df['max-min'] =  df.max(axis=1)-df.min(axis=1)
        #minprice = price[columnnames].min
        #minmaxprice = maxprice - minprice
        #maxprice.plot()
        #plt.plot(diffprices[0],diffprices[1])
    df.plot(grid=True)
    plt.gca().xaxis.set_major_locator(MultipleLocator(xLocator))
    plt.gca().yaxis.set_major_locator(MultipleLocator(yLocator))
    plt.title(title)
    plt.savefig(filename)
    plt.clf()

def plot42Price(x,y,title,filename):
    #filename = u'figure/2016_all_42s_price_ratio.png'
    plt.rcParams['figure.figsize'] = (8, 5)  # 设置绘图尺寸
    print x,y
    plt.plot(x[:-7], y[:-7], 'bo')
    plt.plot(x[-7:], y[-7:], 'ro')
    ratioflag = 0.0404 + (0.0526 - 0.0404)/2
    #title = u'2016年以来42s价格与中标率关系图(近7个月为红色,临界中标率%f)'% ratioflag
    plt.title(title)
    plt.savefig(filename)
    plt.clf()

def plotLastSecondPrice(x,y):
    filename = u'figure/2016_all_lastsecond_ratio.png'
    plt.rcParams['figure.figsize'] = (8, 5)  # 设置绘图尺寸
    print x, y
    plt.plot(x[:-7], y[:-7], 'bo')
    plt.plot(x[-7:], y[-7:], 'ro')
    ratioflag = 0.0404 + (0.0526 - 0.0404) / 2
    title = u'2015年5月份以来最晚出价描述与中标率关系图(近7个月为红色)'
    plt.title(title)
    plt.savefig(filename)
    plt.clf()
if __name__ == '__main__':
    columnnames = ['2016.01','2016.02','2016.03',	'2016.04',	'2016.05',	'2016.06'\
          ,'2016.07',	'2016.08',	'2016.09',	'2016.10',	'2016.11',	'2016.12'\
          ,'2017.01',	'2017.02',	'2017.03',	'2017.04',	'2017.05',	'2017.06']
    plotFigure(df=price[columnnames],title=u'2016年以来价格变化趋势'\
               ,filename='figure/201601_ALL.png')
    columnnames = ['2016.01','2016.06','2016.10',	'2017.06']
    plotFigure(df=price[columnnames],title=u'2016年以来异常月份价格变化趋势'\
               ,filename='figure/201601_Except.png',drawdiff=True)
    columnnames = ['2016.02','2016.03','2016.04',	'2016.05'\
          ,'2016.07',	'2016.08',	'2016.09',	'2016.11',	'2016.12'\
          ,'2017.01',	'2017.02',	'2017.03',	'2017.04',	'2017.05']
    plotFigure(df=price[columnnames],title=u'2016年以来正常月份价格变化趋势',\
               filename='figure/201601_Normal.png',drawdiff=True)
    columnnames = ['2016.02','2016.07','2016.11']
    plotFigure(df=price[columnnames],title=u'2016年以来异常月份下一月价格变化趋势'\
               ,filename='figure/201601_Except_Next.png',drawdiff=True)

    columnnames = ['2017.01', '2017.02', '2017.03', '2017.04', '2017.05', '2017.06']
    plotFigure(df=price[columnnames], title=u'2017年以来所有月份价格变化趋势',\
               filename='figure/201701_All.png',drawdiff=True)
    columnnames = ['2017.01', '2017.02', '2017.03', '2017.04', '2017.05']
    plotFigure(df=price[columnnames], title=u'2017年以来有效月份价格变化趋势',\
               filename='figure/201701_Normal.png',drawdiff=True)
    plotFigure(df=price[29:][columnnames], title=u'2017年以来有效月份30S后变化趋势',\
               filename='figure/201701_Normal_A30S.png',drawdiff=True,xLocator=1)
    plotFigure(df=price[39:][columnnames], title=u'2017年以来有效月份40S后变化趋势',\
               filename='figure/201701_Normal_A40S.png',drawdiff=True,xLocator=1)
    columnnames = ['2017.02', '2017.03', '2017.05']
    plotFigure(df=price[39:][columnnames], title=u'2017年以来低中标月份40S后变化趋势',\
               filename='figure/201701_Low_A40S.png',drawdiff=True,xLocator=1)

    # plot42Price(statics.T['ratio'].values[-7:], price.T['11:29:42'].values[-7:],\
    #             u'近7个月42s价格与中标率关系图',u'figure/last7m_42s_price_ratio.png')

    #plot42Price(statics.T['ratio'].values, price.T['11:29:42'].values)
    #plotLastSecondPrice(statics.T['ratio'].values, statics.T['second'].values)
    #plotLastSecondPrice(statics.T['total'].values, statics.T['second'].values)
