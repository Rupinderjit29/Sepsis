# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:41:54 2023

@author: Rupinder
"""

import pickle
import numpy as np
import streamlit as st
import pandas as pd
import base64
from PIL import Image

loaded_model=pickle.load(open('C:/Users/Rupinder/Downloads/sepsis_trained_model.sav','rb'))


def predict_sirs(Temp,HR,Resp,WBC,PaCO2):
    t_hr=(Temp> 38.5 or Temp < 35) and HR > 90   
    t_re_pa=(Temp> 38.5 or Temp < 35) and (Resp>20 or PaCO2 <32)
    t_wbc=(Temp> 38.5 or Temp < 35) and (WBC>10)
    hr_re_pa= HR > 90  and (Resp>20 or PaCO2 <32)
    hr_wbc= HR > 90  and (WBC>10)
    re_pa_wbc=(Resp>20 or PaCO2 <32) and WBC >10
    sirs=(t_hr==True)or (t_re_pa==True)or (t_wbc==True)or (hr_re_pa==True)or (hr_wbc==True) or (re_pa_wbc==True)
    return sirs



def main():

     if "Predict SIRS" not in st.session_state:
            st.session_state["Predict SIRS"] = False
    
     if "Predict Sepsis" not in st.session_state:
          st.session_state["Predict Sepsis"] = False
      
     if "Predict Severe Sepsis" not in st.session_state:
          st.session_state["Predict Severe Sepsis"] = False
     
      
      

     st.title('Prediction of SIRS, Sepsis, Severe Sepsis')
     col1, col2 = st.columns((1,1))
     with col1:
          Temp = st.number_input('Temperature', help=' °C')
     with col2:
           HR=st.number_input('Heart Rate', help='beats/min')
     col3,col4,col5 = st.columns((1,1,1))
     with col3:
          Resp =st.number_input('Respiration', help='breaths/min')
     with col4:
          WBC = st.number_input('WBC', help='count10^3/µL')
     with col5:
           PaCO2=st.number_input('PaCO2',help='mm Hg')    
      
     if st.button('Predict SIRS') :
          st.session_state["Predict SIRS"] = not st.session_state["Predict SIRS"]
          ab=predict_sirs(float(Temp),float(HR),float(Resp),float(WBC),float(PaCO2))
          if ab==True:
              st.success('Diagonosed with SIRS and may have sepsis.')
    #              lab=st.radio('Would you like to predict sepsis?', ['Yes', 'No'],index=1)         
          else: 
              st.success('Not diagonosed with SIRS.')
      #lab=st.radio('Do you have lab results?', ['Yes', 'No'],index=1)    
      #if lab=='Yes':
     ab=predict_sirs(Temp,HR,Resp,WBC,PaCO2)  
     if ab==True:
          if st.session_state["Predict SIRS"]:
              question1=st.radio('Would you like to predict sepsis?', ['Yes', 'No'],index=1)
              if question1=="Yes":
                  st.write ('Enter the following details.')
          
                  col6,col7,col8= st.columns((1,1,1))
                  with col6:
                      MAP= st.number_input('MAP',help='mm Hg')    
                  with col7:
                      BUN= st.number_input('BUN',help='mg/dL')
                  with col8:
                       FiO2= st.number_input('FiO2',help='Fraction of inspired oxygen')   
                  col9, col10,col11= st.columns((1,1,1))
                  with col9:
                       pH= st.number_input('pH',help='N/A')   
                  with col10:
                       BaseExcess= st.number_input('BaseExcess',help='mmol/L')  
                  with col11:
                        Calcium= st.number_input('Calcium',help='mg/dL')   
                  col12, col13 = st.columns((1,1))
                  with col12:
                      Creatinine= st.number_input('Creatinine',help='mg/dL') 
                  with col13:
                       Platelets= st.number_input(' Platelets',help='count10^3/µL')
                  inputdata=pd.DataFrame([[float(HR), float(Temp), float(Resp), float(MAP), float(BUN), float(FiO2), float(Creatinine),float(Platelets), float(WBC), float(pH), float(Calcium), float(BaseExcess),float(PaCO2)]], columns=['HR', 'Temp', 'Resp', 'MAP', 'BUN', 'FiO2', 'Creatinine','Platelets', 'WBC', 'pH', 'Calcium', 'BaseExcess','PaCO2'])
                  a=loaded_model.predict(inputdata)     
                  if st.button('Predict Sepsis'):
                      st.session_state["Predict Sepsis"] = not st.session_state["Predict Sepsis"]
                      if a[0]==1:
                         st.success('Diagonosed with Sepsis.')
                      else:
                         st.success('Sepsis is not diagonosed.') 
                  if st.session_state["Predict Sepsis"]:  
                      if a[0]==1:
                          question2=st.radio('Would you like to predict severe sepsis?', ['Yes', 'No'],index=1)       
                      
                          if question1=="Yes" and question2=="Yes":  
                              if st.session_state["Predict SIRS"] and st.session_state["Predict SIRS"]:
                                  st.write('To predict severe sepsis amd septic shock, enter the below information')      
                                  col20, col21 = st.columns((1,1)) 
                                  with col20:
                                        Lactate= st.number_input("Lactate",help='mg/dL') 
                                  with col21:
                                        SBP= st.number_input('SBP',help='mm Hg')    
                                  organ=st.radio('Is there any organ damage?', ['Yes', 'No']) 
                                  
                                  
                                  if st.button('Predict Sever Sepsis'):     
                                          if (organ=='Yes') and (float(Lactate)>4) and (float(SBP)<90) : 
                                                       st.success('Diagonosed with severe sepsis. And if the organ damage is persistant then it may lead to septic shock.')  
                                          else:
                                                       st.success('Diagonosed with sepsis only.')      
                          
                   
               
            
            
if __name__=='__main__':   
    main()     
        
          