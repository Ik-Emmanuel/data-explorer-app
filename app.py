import os 
import streamlit as st

# import EDA libraries 
import numpy as np 
import pandas as pd 

# import visualization tools 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 


def main(): 
    # Our Dataset Explorer App with streamlit 
    st.title ("THE DATASET EXPLORER APP")
    st.subheader('Powered by StreamLit.  ')
   
    html_temp = """
    <div style = "background-color: blue;"> <p style = "color:white; font-size:20px;"> Built by I.K Emmanuel</p> </div>

     """
    st.markdown (html_temp, unsafe_allow_html = True) 
   
   
    

    def file_selector (folder_path = './datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox(" Select a file to begin exploration.", filenames)
        return os.path.join(folder_path, selected_filename)
    
    filename = file_selector()
    st.info(" You have just selected {}". format(filename))

    #Reading datasets 
    df= pd.read_csv(filename)
    st.subheader ("Data Exploration")
    #Showing data
    if st.checkbox("Show Dataset"):
        number = st.slider("select the nummber of rows you would like to view",0,1000,1,1)
        st.dataframe (df.head(number))

    #Showing columns 
    if  st.checkbox(" Click here to view the columns of the dataset"):
        st.write(df.columns)
    #Showing Shape 
    if st.checkbox ("Shape of Dataset"):
        data_dim = st.radio("View the Number of Rows or Columns Present in the data ", ("Rows", "Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write (df.shape[0])
        elif data_dim == 'Columns':
            st.text("Number of Columns")
            st.write (df.shape[1])
        else: 
            st.write (df.shape)
  #Showing  Columns
    if st.checkbox ("Select a few columns to be displayed"):
        all_columns = df.columns.tolist()
        selected_columns = st.multiselect("Select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)

    #Showing Values 
    if st.button( "Click here to view the distribution of the Target Variable"):
        st.text("Value Counts By Target Variable")
        st.write(df.iloc[:,-1].value_counts())

 #Showing Datatypes
    if st.button( "Click here to check the various datatypes present in the data"):
        st.text("Data Types")
        st.write(df.dtypes)

    # Showing Summary 

    if st.checkbox ("Statistical Summary of Data set"):
        st.write(df.describe().T)
    # Plots an dVisualizations 
    st.subheader ("Data Visualization ")

    #Correlations 

    #Seaborn Plots 
    if st.checkbox("Correlation Plot[ using seaborn]"):
        st.write(sns.heatmap(df.corr(), annot=True))
        st.pyplot()
    
    #Count plots 
    if st.checkbox("Plot of Value Counts"):
        st.text ("Value Counts by Targets ")
        all_columns_names = df.columns.tolist()
        primary_col = st.selectbox( "Select primary column to groupby", all_columns_names)
        selected_columns_names = st.multiselect( "Select columns", all_columns_names)
        if st.button("Plot"):
            st.text ("Generating your plot please wait....")
            if selected_columns_names:
                vc_plot = df.groupby(primary_col)[selected_columns_names].count()
            else:
                vc_plot = df.iloc[:,-1].value_counts()
            st.write(vc_plot.plot(kind="bar"))
            st.pyplot()


 
    
    #Customizable Plot 
    st.subheader("Customizable Plots")
    all_columns_names = df.columns.tolist()
    types_of_plot = st.selectbox ("Please select a plot type from the drop-down menu", ["area", "bar", "line", "hist", "box", "kde"])
    selected_columns_names = st.multiselect( "Select different columns from the drop-down menu to plot",all_columns_names )

    if st.button("Generate Plot"):
        st.success(" Generating your {} plot  for {} now please wait...".format(types_of_plot, selected_columns_names))

      #main plot 
        if types_of_plot == "area":
            cust_data = df[selected_columns_names]
            st.area_chart(cust_data)

        elif types_of_plot == "bar": 
            cust_data = df[selected_columns_names]
            st.bar_chart(cust_data)

        elif types_of_plot == "line": 
            cust_data = df[selected_columns_names]
            st.line_chart(cust_data)

        elif types_of_plot:
            cust_plot= df[selected_columns_names].plot(kind=types_of_plot)
            st.write(cust_plot)
            st.pyplot()





if __name__ == '__main__':
    main()