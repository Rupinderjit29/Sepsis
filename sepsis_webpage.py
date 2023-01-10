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
    st.set_page_config(layout="wide")  
    image1 = Image.open('C:/Users/Rupinder/Downloads/2.png')
    image1=image1.resize((350,300))
    
    image2=Image.open('C:/Users/Rupinder/Downloads/Sepsis Six.png')
    image2=image2.resize((350,250))
    
    image3=Image.open('C:/Users/Rupinder/Downloads/1.png')
    image3=image3.resize((425,300))
    
    def title(url):
       st.markdown(f'<p style="background-color:#c0c0c0;color:#8b0000;font-size:38px;text-align: center;border: 1px solid black;border-width: 2px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    def title1(url):
       st.markdown(f'<p style="background-color:#c0c0c0;color:#8b0000 ;font-size:26px;text-align: center;border: 1px solid black;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    def title2(url):
       st.markdown(f'<p style="background-color:#eee8aa;color:#8b0000 ;font-size:24px;text-align: center;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    
    def subtitle(url):
        st.markdown(f'<p style="background-color:#dcdcdc ;color:Black;font-size:22px;text-align: left;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    def write1(url):
        st.markdown(f'<p style="background-color:#FFFFFF ;color:#000000;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    def write2(url):
        st.markdown(f'<p style="background-color:#FFFFFF ;color:#000000;font-size:18px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)
    cola,colb,colc=st.columns((1,0.5,1))
    with colb:
        title("Sepsis")
    col_over,col_over1=st.columns((0.2,1.2)) 
    with col_over:
        st.write('#')
        subtitle('Overview')
    
    write2('Sepsis is an extreme response to an infection by the body. It happens when an existing infection triggers a chain reaction throughout your body. In most of the cases, infections in the lung, urinary tract, skin, or gastrointestinal tract leads to sepsis. It can also be a result of other infections, such as COVID-19, influenza, or fungal infections. Delay in the treatment of sepsis can rapidly lead to tissue damage, organ failure, and even death.')
    
    col_sign,col_sign1=st.columns((0.6,1)) 
    with col_sign:
        subtitle('Signs & Symptoms of Sepsis')
    
    write2('Most often, infection that turns into Sepsis, occurs in the patients who are hospitalized for a while and are in the Intensive care Unit. Symptoms of sepsis are not confined to the following list.')
    
    colc,cold=st.columns((1,1))
    with colc:
        st.markdown(""" 
                    - High heart rate or weak pulse 
                    - Fever, shivering, or feeling very cold 
                    - Shortness of breath 
                    
                    """ )
    with cold:
        st.markdown(""" 
                    - Confusion or disorientation 
                    - Extreme pain or discomfort
                    - Clammy or sweaty skin
                    
                    """ )
    col_risk,col_risk1=st.columns((0.3,1)) 
    with col_risk:
         subtitle('Who are at risk?')                
   
    write2('Anyone can develop sepsis, but some people are at higher risk for sepsis:')                
    cole,colf=st.columns((1,1))
    with cole:
        st.markdown(""" 
                    - Adults 65 or older
                    - People with weakened immune systems
                    - People with recent severe illness or hospitalization 
                    
                    """ )
    with colf:
        st.markdown(""" 
                    - Children younger than one
                    - People who survived sepsis
                    - People with chronic medical conditions, such as diabetes, lung disease, cancer, and kidney disease
                    
                    """ )                    
    title1('Let\'s get to know the Stages of Sepsis')
    write2("On the basis of severity of the condition of a patient, sepsis is classified into four stages SIRS, sepsis, severe sepsis, and septic shock.")
    colstage1,colstage11=st.columns((0.2,1))
    with colstage1:
        title2('SIRS') 
    colstage1_1,colstage11_1=st.columns((0.8,1))    
    with colstage1_1:
        write2(' Systemic Inflammatory Response Syndrome (SIRS) is a clinical syndrome caused by inflammation and widespread tissue injury. Identifying SIRS in a patient includes the following criteria:')
        st.markdown(
          """
          - Temperature >38.5ºC or <35ºC
          - Heart rate >90 beats/min 
          - Respiratory rate >20 breaths/min or PaCO2 <32 mmHg 
          - WBC >12,000 cells/mm3 or < 4000 cells/mm3, or >10 percent immature (band) forms 
          """ )
    with colstage11_1:
        st.image(image1,caption='Ref : Bochud, Glauser, & Calandra; Antibiotics in sepsis. Int Care Med; 2001, 27: S33-48.')
    colstage2,colstage22=st.columns((0.2,1))
    with colstage2:
       title2('Sepsis') 
    write2(' Sepsis, is formerly known as septicemia or blood poisoning. A patient identified with SIRS and a confirmed or suspected infection means, the patient has Sepsis.')
    colstage2_2,colstage22_2=st.columns((1,1))
    with colstage2_2:
        write2('Since 2016, a shortened sequential organ failure assessment score (SOFA score) is also used to diagnose sepsis. SOFA criteria for sepsis include at least two of the following three:')
        st.markdown(""" 
                    - increased breathing rate
                    - change in the level of consciousness 
                    - low blood pressure
                        """)                      
    write2('Sepsis guidelines recommend to obtain blood cultures before starting antibiotics; however, the diagnosis does not require the blood to be infected.')                
    with colstage22_2:
        st.image(image2)
    colstage3,colstage33=st.columns((0.3,1))
    with colstage3:
        title2('Severe Sepsis') 
    #colstage3_3,colstage33_3=st.columns((1,1))
    #with colstage3_3:
     #   st.image(image2)
    #with colstage33_3:    
    write2(' It is diagnosed when acute organ dysfunction begins.  The conditions for Severe Sepsis are : ')
    st.markdown(
      """
    - Hypotension (Systolic Blood Pressure < 90 mmHg)
    - Lactate > 4 mmol 
    - Organ damage
      """ )
      
    colstage4,colstage44=st.columns((0.3,1))
    with colstage4:
        title2('Septic Shock')   
    colstage4_4,colstage44_4=st.columns((0.8,1))
    with colstage4_4:
        write2(' This is the final stages of Sepsis. The patient is identified to be in Septic Shock stage if he has the below conditions:')
        st.markdown(
        """
       - Severe Sepsis and persistant organ damage.
       - Hypotension (Systolic Blood Pressure < 90 mmHg)
       - Lactate > 4 mmol 
        """ )
        write2('Septic shock has the highest chance of mortality, ~ 30% to 50%.')
    with colstage44_4:
         st.image(image3,caption='Ref : McCoy & Matthews, Drotrecogin alpha for the treatment of severe sepsis. Clin Theraeutics, 25(2), 391-421.')
    title1('Know more facts about Sepsis') 
    write2('According to first global report on sepsis of World Health Organization(WHO), the serious gaps in knowledge, particularly in low- and middle-income countries is the main cause of sepsis.  Recent studies shows that 11 million people are killed and millions more are disabled due to sepsis each year.')
    write2('Approximately 85.0% of sepsis cases and sepsis-related deaths are of newborns, pregnant women and people living in low-resource settings. Almost half of the 49 million cases of sepsis each year occur among children, resulting in 2.9 million deaths, most of which could be prevented through early diagnosis and appropriate clinical management. To know more about the facts of sepsis, few of the references are linked below.')
         
    st.write("WHO calls for global action on sepsis [Link](https://www.who.int/news/item/08-09-2020-who-calls-for-global-action-on-sepsis---cause-of-1-in-5-deaths-worldwide)")
    st.write("WHO fact sheet on sepsis [Link](https://www.who.int/news-room/fact-sheets/detail/sepsis)")
    st.write("Sepsis incidence and mortality, 1990–2017 [Link](https://www.thelancet.com/action/showPdf?pii=S0140-6736%2819%2932989-7) ")
    
    if "Predict SIRS" not in st.session_state:
        st.session_state["Predict SIRS"] = False

    if "Predict Sepsis" not in st.session_state:
        st.session_state["Predict Sepsis"] = False
    
    if "Predict Severe Sepsis" not in st.session_state:
        st.session_state["Predict Severe Sepsis"] = False
   
    
    
    with st.sidebar:
        st.header('Prediction of SIRS, Sepsis, Severe Sepsis')
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
        
          