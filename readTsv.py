import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
#print("Enter a file name exactly")
def user_Int():
    file_name= raw_input("Enter a file name exactly : ")
    typeOf = raw_input("Number Variants (1) or Short Variants (2) : ")
    if typeOf == 1:
        #startNumVar()
        pass
    
def specCop(chrom_data: DataFrame):
    pass
    
def copyNum_Analy(chrom_data: DataFrame):
    name = chrom_data.columns[0]
    #print(chrom_data)
    
    new_df = chrom_data
    #new_df.plot(x="Start", y="Var_Num")
    #new_df.set_index("Chrom_Name")
    #new_df.loc["Chrom_Name", "Var_Num"] = {0: 1, 1: 2, 3 : 3}
    #print(new_df)
    
    
    #new_df["Var_Num"] = new_df["Var_Num"].replace({0: 1, 1: 2, 3 : 3})
    #print(new_df)
    tot = len(new_df)
    
    larDiv = 0
    for i in range(2,tot):
        if tot % i ==0:
            larDiv = i
                   
    newNum = tot%larDiv
    num = int(len(new_df)/larDiv)
    hello =coutT= sns.countplot(x="Start", hue= "Var_Num",
                                data = new_df[:100], palette = 'winter')
    axes=plt.gca()
    axes.set_ylim([0,1])
    hello.label(name)
    """
    for i in range(num):
        track = larDiv-1
        if i ==0:
            coutT = sns.countplot(x= "Start", hue = "Var_Num",
                                  data= new_df[:larDiv-1], palette = 'winter')
        if i>0:
            coutT = sns.countplot(x= "Start", hue = "Var_Num",
                                  data= new_df[track:track*2], palette = 'winter')
        track = track*i
    coutT = sns.countplot(x= "Start", hue = "Var_Num",
                          data= new_df[:larDiv], palette = 'winter')
    """
    
    
    #new_df["Var_Num"] = new_df["Var_Num"].map({0: 'BothLost', 1: 'OneLost', 3 : 'OneGain'})
    #types = new_df["Var_Num"].value_counts()
    #types.plot.bar()
    #types.set_xlabel("Variant Copies From Bases")
def newSh_col(chrom):
    start, end = chrom
    return str(start) + "-" + str(end)

def short_varAnaly(chrom_frame):
    name = chrom_frame.columns[0]
    new_frame = chrom_frame
    print(new_frame)
    scat1= new_frame[:10].plot.bar(x="Location", y="Severity")


def copyNum_dataframe(file_name):
    pass

with open('HG002_copynumber_variants.tsv') as tsvfile:
    read1= csv.reader(tsvfile, delimiter = '\t')
    df = pd.DataFrame(read1)
    df.columns = ["Chrom_Name", "Start", "End", "Base_Num", "Var_Num", 5, 6]
    df =df.drop([5,6], axis =1)
    #print(df)
def new_col(chrom):
    base,var = chrom
    if int(base) ==0 and int(var) ==0:
        return 0
    if int(base) > int(var):
        return 1
    if int(var) > int(base):
        if int(var) -int(base) > 100:
            return 4
        elif int(var)-int(base) > 50:
            return 3
        else:
            return 2
    
with open('HG002_short_variants.tsv') as tsvfile1:
    read2 = csv.reader(tsvfile1, delimiter = '\t')
    df1 = pd.DataFrame(read2)
    df1.columns = ["Chrom_Name", "Start", "End", "Base", "Var", "Base_Num", "Var_Num"]
    df1["Severity"]= df1[["Base_Num", "Var_Num"]].apply(new_col, 1)
    df1["Location"] = df1[["Start", "End"]].apply(newSh_col, 1)
    #print(df1["Chrom_Name"].value_counts())
    
chrom = df[df["Chrom_Name"] == 'chr1']
#print(type(chrom))
#print(chrom.columns[2])
#hello = df[0].value_counts()
chrom1 = df1[df1["Chrom_Name"] == 'chr1']
#copyNum_Analy(chrom)  
short_varAnaly(chrom1)
plt.show()
