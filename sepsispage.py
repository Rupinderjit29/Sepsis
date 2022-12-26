# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 13:57:46 2022

@author: Iqbal
"""
import pickle
import numpy as np
import streamlit as st
import pandas as pd
import base64

loaded_model=pickle.load(open('sepsis_trained_model.sav','rb'))


def predict_sirs(Temp,HR,Resp,WBC,PaCO2):
    t_hr=(float(Temp)> 38.5 or float(Temp) < 35) and  float(HR) > 90   
    t_re_pa=(float(Temp)> 38.5 or float(Temp) < 35) and (float(Resp)>20 or float(PaCO2) <32)
    t_wbc=(float(Temp)> 38.5 or float(Temp) < 35) and (float(WBC)>10)
    hr_re_pa= float(HR) > 90  and (float(Resp)>20 or float(PaCO2) <32)
    hr_wbc= float(HR) > 90  and (float(WBC)>10)
    re_pa_wbc=(float(Resp)>20 or float(PaCO2) <32) and (float(WBC)>10)
    sirs=(t_hr==True)or (t_re_pa==True)or (t_wbc==True)or (hr_re_pa==True)or (hr_wbc==True) or (re_pa_wbc==True)
    return sirs



def main():
    
    st.set_page_config(layout="wide")   
   # with open('C:/Users/Iqbal/Desktop/web/Stages of Sepsis.pdf',"rb") as f:
    #    base64_pdf = base64.b64encode(f.read()).decode('utf-8')    
   # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'    
   # st.markdown(pdf_display, unsafe_allow_html=True)
    st.title('What is Sepsis?')
    st.write('Sepsis is the body’s extreme response to an infection. It is a life-threatening medical emergency.  Sepsis happens when an infection you already have triggers a chain reaction throughout your body.  Infections that lead to sepsis most often start in the lung, urinary tract, skin, or gastrointestinal tract. Without timely treatment, sepsis can rapidly lead to tissue damage, organ failure, and death.')
   # st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
    st.header('What causes sepsis?')
    st.write('Infections can put you or your loved one at risk for sepsis. When germs get into a person’s body, they can cause an infection. If you don’t stop that infection, it can cause sepsis. Bacterial infections cause most cases of sepsis. Sepsis can also be a result of other infections, including viral infections, such as COVID-19 or influenza, or fungal infections.')
    st.header('Stages of Sepsis')
    st.write('Stage one: Systemic Inflammatory Response Syndrome (SIRS)Sepsis can be hard to identify, but is typically denoted by a very high or low body temperature, high heart rate, high respiratory rate, high or low white blood cell count and a known or suspected infection. The aforementioned signs are actually used to identify Systemic Inflammatory Response Syndrome (SIRS), which only becomes sepsis when an infection is present.SIRS is, in some circles, a more commonly used term because sepsis is only seen as a subcategory of SIRS. For sepsis, two of the mentioned SIRS signs, as well as an infection, need to be present.')
    st.write('Stage two: severe sepsisThe second stage, called severe sepsis, is diagnosed when acute organ dysfunction begins. Severe sepsis can also be diagnosed when sepsis is present along with hypotension (low blood pressure) or hypoperfusion (decreased blood flow through an organ).')
    st.write('Stage three: septic shock Septic shock is the most severe stage of sepsis. It is defined as the presence of hypotension, induced by sepsis, despite fluid resuscitation. In addition, perfusion abnormalities such as elevated lactate levels. Septic shock has the highest chance of mortality, with estimates ranging from 30% to 50%.')
    with st.sidebar:
        st.header('Prediction of SIRS, Sepsis, Severe Sepsis')
        col1, col2,col3 = st.columns((1,1,1))
        with col1:
            Age = st.text_input('Age',help='years')
        with col2:
            Temp = st.text_input('Temperature', help=' °C')
        with col3:
             HR=st.text_input('Heart Rate', help='beats/min')
        col4,col5,col6 = st.columns((1,1,1))
        with col4:
            Resp = st.text_input('Respiration', help='breaths/min')
        with col5:
            WBC = st.text_input('WBC', help='% immature band form')
        with col6:
             PaCO2=st.text_input('PaCO2',help='mm/Hg')    
        #t_hr=(float(Temp)> 38.5 or float(Temp) < 35) and  float(HR) > 90   
        #t_re_pa=(float(Temp)> 38.5 or float(Temp) < 35) and (float(Resp)>20 or float(PaCO2) <32)
        #t_wbc=(float(Temp)> 38.5 or float(Temp) < 35) and (float(WBC)>10)
        #hr_re_pa= float(HR) > 90  and (float(Resp)>20 or float(PaCO2) <32)
        #hr_wbc= float(HR) > 90  and (float(WBC)>10)
        #re_pa_wbc=(float(Resp)>20 or float(PaCO2) <32) and (float(WBC)>10)
        if st.button('Predict SIRS') :
            ab=predict_sirs(Temp,HR,Resp,WBC,PaCO2)
            if ab==True:
                st.success('Diagonosed with SIRS. You may have sepsis.  And to predict sepsis enter other laboratory values and vitals.')
            else: 
                st.success('Not diagonosed with SIRS.')
                     #st.write('bbjbj') 
               #st.success('SIRS') 
            #else:
            #    st.success(' Not SIRrite('Sirs')
       
        #lab=st.radio('Do you have lab results?', ['Yes', 'No'],index=1)    
        #if lab=='Yes':
        ab=predict_sirs(Temp,HR,Resp,WBC,PaCO2)  
        if ab==True:
            col7,col8,col9,col10,col17 = st.columns((1,1,1,1,1))
            with col7:
                O2Sat= st.text_input('O2Sat')    
            with col8:
                MAP= st.text_input('MAP')    
            with col9:
                BUN= st.text_input('BUN')
            with col10:
                 FiO2= st.text_input('FiO2') 
            with col17:
                  Hct= st.text_input('Hct')  
            col11, col12,col13,col14 = st.columns((1,1,1,1))
            with col11:
                 Creatinine= st.text_input('Creatinine')   
            with col12:
                 Platelets= st.text_input(' Platelets')
            with col13:
                  pH= st.text_input('pH')    
            with col14:
                  Calcium= st.text_input('Calcium')   
            col15, col16,col18,col19 = st.columns((1,1,1,1)) 
            with col15:
                  BaseExcess= st.text_input('BaseExcess') 
            with col16:
                  Potassium= st.text_input('Potassium') 
            with col18:
                  Magnesium= st.text_input('Magnesium') 
            with col19:
                  Glucose= st.text_input('Glucose') 
        inputdata=pd.DataFrame([[float(HR), float(Temp), float(Resp), float(O2Sat), float(MAP), float(BUN), float(FiO2), float(Creatinine),float(Platelets), float(WBC), float(Age), float(pH), float(Calcium), float(BaseExcess), float(Potassium),float(PaCO2), float(Hct), float(Magnesium), float(Glucose)]], columns=['HR', 'Temp', 'Resp', 'O2Sat', 'MAP', 'BUN', 'FiO2', 'Creatinine','Platelets', 'WBC', 'Age', 'pH', 'Calcium', 'BaseExcess', 'Potassium','PaCO2', 'Hct', 'Magnesium', 'Glucose'])
        a=loaded_model.predict(inputdata)     
        if st.button('Predict Sepsis'):
            if a[0]==1:
               st.success('Diagonosed with Sepsis.')
            else:
               st.success('Sepsis is not diagonosed.')   
        if a[0]==1:
            st.write('To predict severe sepsis amd septic shock, enter the below information')      
            col20, col21 = st.columns((1,1)) 
            with col20:
                 Lactate= st.text_input("Lactate") 
            with col21:
                 SBP= st.text_input('SBP')    
            organ=st.radio('Is there any organ damage?', ['Yes', 'No']) 
            if st.button('Predict Sever Sepsis'):
                if (organ=='Yes') and (float(Lactate)>4) and (float(SBP)<90) : 
                        st.success('Diagonosed with severe sepsis. And if the organ damage is persistant then it may lead to septic shock.')  
                else:
                        st.success('Diagonosed with sepsis only.')      
       
        #a=loaded_model.predict(inputdata)
        #if st.button('Predict Sepsis'):
         #   if a[0]==1:
          #      st.success('Sepsis')
            #else:
               # st.success('No Sepsis')

    #if st.button('Predict Sever Sepsis'):
    
        
if __name__=='__main__':   
    main()     
        
          
