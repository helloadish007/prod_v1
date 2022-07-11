#Author : ADISH007
from cmath import nan
import pandas as pd
import numpy as np
import streamlit as st
from math import ceil
from annotated_text import annotated_text


dfd=pd.read_csv(r'https://raw.githubusercontent.com/helloadish007/prod_v1/main/demo0.csv')

st.markdown("""
<style>div[data-testid="stToolbar"] { display: none;}</style>
""", unsafe_allow_html=True)



st.header(' ANNOTATION TOOL ')
option = st.sidebar.selectbox(
    'Select the System :',
     ('BERTS2S', 'TConvS2S', 'Gold' , 'PtGen', 'TranS2S')
)

with st.sidebar.expander("Annotation info: "):
     st.write("""
         Intrinsic hallucinations: a span of word(s) in
        G contains incorrect information due to synthesizing content using information present in S.
     """,width=10,use_column_width=20)
     st.write("""
         Extrinsic hallucinations: a span gi
        , · · · , gi+j in
        G consists of additional content without clear
        grounding in the input
     """,width=10,use_column_width=20)
    
     
     st.header(' S : source sequence  ')
     st.header(' G : output sequence  ')
     st.text('Creator : ADISH007')

with st.sidebar.expander("Demo File"):
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    csv = convert_df(dfd)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='demo_df.csv',
        mime='text/csv',
    )
    st.sidebar.image("https://apaie2022.net/wp-content/uploads/2019/05/APAIE2020_header_bg_4.png")

uploaded_file = st.file_uploader("Upload File : ", type={"csv", "txt"})
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)






    if "updated_df" not in st.session_state:
                st.session_state.updated_df = df

    row = st.session_state["updated_df"].loc[st.session_state["updated_df"]['system'] == option]
    df1= row['summary']

    with st.expander("How to use ?"):
        st.write("""
            See the annotations and replace the phrase , if necessary 
        """,width=10,use_column_width=20)
        st.image("data:image/jpeg;base64,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")


    page_size = 1
    page_number = st.number_input(
        label="Page Number",
        min_value=1,
        max_value=ceil(len(df1)/page_size),
        step=1,
    )
    st.write('Total Pages :',ceil(len(df1)/page_size))
    current_start = (page_number-1)*page_size
    current_end = page_number*page_size


    
    hsi=int(row[current_start:current_end].index[0])
    start=int(row['hallucinated_span_start'][hsi])-1
    end=int(row['hallucinated_span_end'][hsi])
    s=row['start'][hsi]
    h=row['hallucinated_span_new'][hsi]
    e=row['end'][hsi]
    hst=row['hallucinated_span'][hsi]
    tag=row['hallucination_type'][hsi]
    alp=df1[hsi]




    st.write('**ORIGINAL OUTPUT  :**')
    if start >= 0 and end >= 0 :
        
        annotated_text(alp[:start],(alp[start:end],tag),alp[end:])
        st.write("##")
        st.write('**CHANGED OUTPUT  :**')

        if (type(s)==float and type(e)==float):
            annotated_text((h,tag))
        elif (type(s)==float and type(e)!=float):
            annotated_text((h,tag),e)
        elif (type(s)!=float and type(e)==float):
            annotated_text(s,(h,tag))
        else:
            annotated_text(s,(h,tag),e)

        st.write("##")
        change = st.text_input('Change Annotated Text ', '')
        if st.button('Submit'):
            st.session_state["updated_df"].loc[hsi,'hallucinated_span_new']=change
            st.experimental_rerun()
            
    else:
        st.caption('SUMMARY IS NOT ANNOTATED')

    agree = st.checkbox('Made Changes? Download the CSV file from here')

    if agree:
        @st.cache
        def convert_df(df):
            # Cache the conversion to prevent computation on every rerun
            return df.to_csv(index=False).encode('utf-8')

        csv = convert_df(st.session_state["updated_df"])

        st.download_button(
            label="DOWNLOAD CHANGES",
            data=csv,
            file_name='changes.csv',
            mime='text/csv',
        )

        st.info('Changes would be reflected in hallucinated_span_new column')



