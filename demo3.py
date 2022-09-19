import pandas as pd
import streamlit as st
from load_css import local_css

from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import streamlit.components.v1 as components

st.title("Data inference")

count=0
meanings=pd.read_csv(r"C:\Users\Admin\Downloads\Data_inference-main (1)\label_meanings.csv", engine="pyarrow")

#train = pd.read_csv(r"C:\Users\Admin\Downloads\final_file.tsv",sep='\t', encoding='utf-8')

df1=pd.read_csv("C:/Users/Admin/Documents/0 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df2=pd.read_csv("C:/Users/Admin/Documents/1 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df3=pd.read_csv("C:/Users/Admin/Documents/2 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df4=pd.read_csv("C:/Users/Admin/Documents/3 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df5=pd.read_csv("C:/Users/Admin/Documents/4 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df6=pd.read_csv("C:/Users/Admin/Documents/5 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df7=pd.read_csv("C:/Users/Admin/Documents/6 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
df8=pd.read_csv("C:/Users/Admin/Documents/7 editeddd_final_file.tsv" ,  sep='\t', engine="pyarrow")
train = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8])   

okk1 = pd.read_csv(
    "C:/Users/Admin/Documents/sent_final_file.tsv", sep='\t',engine="pyarrow")

print(train)
print(train.shape)
print(okk1)
print(okk1.shape)
train = train.reset_index(drop=True)
print(train)
conf_mat=pd.read_csv(r"C:\Users\Admin\Downloads\Data_inference-main (1)\conf_mat.csv", engine="pyarrow")


df = pd.read_csv(
    r"C:\Users\Admin\Downloads\Data_inference-main (1)\final_file1.csv", engine="pyarrow")


df_pred=pd.read_csv(r"C:\Users\Admin\Downloads\Data_inference-main (1)\result_file.csv", engine="pyarrow")

#check if test file and result file are consistent and add the prediction columns to the final_file 
df['HEAD_PRED']=" "
df['DEPREL_PRED']=" "
for i in range(len(df)):
  if df['SENT_NO'][i]== df_pred['SENT_NO'][i] and df['ID'][i]==df_pred['ID'][i] and (df['FORM'][i]== df_pred['FORM'][i] or pd.isnull(df['FORM'][i])) :
    df['HEAD_PRED'][i]=df_pred['HEAD'][i]
    df['DEPREL_PRED'][i]=df_pred['DEPREL'][i]
  else:
    print("There is a mismatch in the IDs of test and predicted data at index :")
    print(i)
    break


sent_df=pd.read_csv(r"C:\Users\Admin\Downloads\Data_inference-main (1)\test_sent.csv", engine="pyarrow")
sent_df['SENT_NO'] = pd.to_numeric(sent_df['SENT_NO'])

df['sentence']= " "
for i in range(len(df)):
  df['sentence'][i]=sent_df.loc[sent_df['SENT_NO']==df['SENT_NO'][i], 'FORM'].item()


print(df.columns)
print(df.head(5))
df1=df.head(5)
df1.to_csv('file1.csv')







def support(label1,label2):
  idx_l1=int(conf_mat[conf_mat['Labels']==label1].index.values)
  idx_l2=int(conf_mat[conf_mat['Labels']==label2].index.values)
  columns=['label','Train_support','Test_support']
  support=pd.DataFrame(columns=columns)
  support.loc[len(support.index)] = [label1, conf_mat['Training_support'][idx_l1], conf_mat['Test Support'][idx_l1]]
  support.loc[len(support.index)] = [label2, conf_mat['Training_support'][idx_l2], conf_mat['Test Support'][idx_l2]]
  st.dataframe(support)
  print(support)

def info(count,idx,label1,label2):
  columns=['label_type','labels','Meaning_Sanskrit','Meaning_English']
  conf=pd.DataFrame(columns=columns)
  conf['label_type']=['annotated label', 'predicted label']
  conf['labels']=[label1,label2]
  def meaningS(i):
    return meanings.loc[meanings['Label'] == conf['labels'][i], 'Meaning(Sanskrit)'].iloc[0]
  def meaningE(i):
    return meanings.loc[meanings['Label'] == conf['labels'][i], 'Meaning(English)'].iloc[0]
  if label1 in meanings['Label'].values:
    if label2 in meanings['Label'].values:
      conf['Meaning_Sanskrit']= [meaningS(0),meaningS(1)]
      conf['Meaning_English']=[meaningE(0),meaningE(1)]
    else:
      conf['Meaning_English'][0]=meaningE(0)
      conf['Meaning_Sanskrit'][0]=meaningS(0)
  elif label2 in meanings['Label'].values:
    conf['Meaning_English'][1]=meaningE(1)
    conf['Meaning_Sanskrit'][1]=meaningS(1)
  print("Wrongly predicted sentence\n")
  st.write("Wrongly predicted sentence\n")
  print(df['sentence'][idx] + "\nword: "+ df['FORM'][idx] +"\thead: " + str(df['HEAD'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
  st.write(df['sentence'][idx]+"\n"+"\nword: "+ df['FORM'][idx] +"\thead: " + str(df['HEAD'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
  if(count==0):
    st.dataframe(conf)
    print(conf)
    print("\n")
    print(support(label1,label2))
    count+=1

    print("Examples of "+label1+"\n")
    st.write("Examples of "+label1+"\n")
    c=1
    for idx in range(len(train)):
        if train['karka Relation'][idx]==label1:
            print("inside")
            st.write(okk1['sentence'][idx],"\nword: "+ train['Inflection/Surface form'][idx] +"\thead: " + str(train['head_inflection'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
            print(okk1['sentence'][idx] + "\nword: "+ train['Inflection/Surface form'][idx] +"\thead: " + str(train['head_inflection'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
            c+=1
        if c>3:
            break       
    print("Examples of "+str(label2)+"\n")
    st.write("Examples of "+str(label2)+"\n")
    c=1
    for idx in range(len(train)):
        if train['karka Relation'][idx]==label2:
            st.write(okk1['sentence'][idx],"\nword: "+ train['Inflection/Surface form'][idx] +"\thead: " + str(train['head_inflection'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
            print(okk1['sentence'][idx] + "\nword: "+ train['Inflection/Surface form'][idx] +"\thead: " + str(train['head_inflection'][idx]) + "\tsent_id: " + str(df['ID'][idx]) + "\n")
            c+=1
        if c>3:
            break  






label1 = st.selectbox(
     'Annotated label',df.DEPREL.unique()
     )

st.write('You selected:', label1)

label2 = st.selectbox(
     'Predicted label',
  
     df['DEPREL'].unique())


st.write('You selected:', label2)
        
for idx in range(len(df)):
  if df['DEPREL'][idx]==label1 and df['DEPREL_PRED'][idx]==label2:
    if(count==0):
        info(count,idx,label1,label2)
        count+=1
        isclick = st.button('Click For more example')
    else:
        if isclick:
            info(count,idx,label1,label2)
            count+=1
            if(count>3):
                break
            
        


    # if count > 3:
    #     break


if idx>=(len(df)-1):
  print("No more confustion pairs..")

