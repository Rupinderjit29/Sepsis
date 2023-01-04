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
    image1 = Image.open('sepsis_mortality.PNG')
    image2=Image.open('sepsis_category.PNG')
    #st.image(image,width=700)
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
    col_over,col_over1=st.columns((1,3)) 
    with col_over:
        st.write('#')
        subtitle('Overview')
    
    write2('Sepsis is an extreme response to an infection by the body.It happens when an existing infection triggers a chain reaction throughout your body. In most of the cases, infections in the lung, urinary tract, skin, or gastrointestinal tract leads to sepsis. It can also be a result of other infections, such as COVID-19, influenza, or fungal infections. Delay in the treatment of sepsis can rapidly lead to tissue damage, organ failure, and even death.')
    col_sign,col_sign1=st.columns((0.7,1)) 
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
    title1('Let s get to know the Stages of Sepsis')
    write2("On the basis of severity of the condition of a patient, sepsis is classified into four stages SIRS, sepsis, severe sepsis, and septic shock.")
    colstage1,colstage11=st.columns((0.2,1))
    with colstage1:
        title2('SIRS') 
    colstage1_1,colstage11_1=st.columns((0.8,1))    
    with colstage1_1:
        write2(' Systemic Inflammatory Response Syndrome. It is a clinical syndrome caused by inflammation and wid espread tissue injury.Identifying SIRS in a patient include the following criteria:')
        st.markdown(
          """
          - Temperature >38.5ºC or <35ºC
          - Heart rate >90 beats/min 
          - Respiratory rate >20 breaths/min or PaCO2 <32 mmHg 
          - WBC >12,000 cells/mm3 or < 4000 cells/mm3, or >10 percent immature (band) forms 
          """ )
    with colstage11_1:  
        st.image(image2)
    
    colstage2,colstage22=st.columns((0.2,1))
    with colstage2:
       title2('Sepsis') 
    write2('A patient identified with SIRS and a confirmed or suspected infection means the patient has Sepsis.')
    colstage3,colstage33=st.columns((0.3,1))
    with colstage3:
        title2('Severe Sepsis') 
    colstage3_3,colstage33_3=st.columns((1.4,1))
    with colstage3_3:
        st.image(image2)
    with colstage33_3:    
        write2(' It is diagnosed when acute organ dysfunction begins.  The conditions for Severe Sepsis are : ')
        st.markdown(
        """
      - Hypotension (Systolic Blood Pressure < 90 mmHg)
      - Lactate > 4 mmol 
      - Organ damage
        """ )
        st.write('#')
    
    colstage4,colstage44=st.columns((0.3,1))
    with colstage4:
        title2('Septic Shock')   
    colstage4_4,colstage44_4=st.columns((0.8,1))
    with colstage4_4:
        write2(' This is the final stages of Sepsis. The patient is identified to be in Septic Shock stage if they have the below conditions:')
        st.markdown(
        """
       - Severe Sepsis and persistant organ damage. - Hypotension (Systolic Blood Pressure < 90 mmHg)
       - Lactate > 4 mmol 
        """ )
        write1('Septic shock has the highest chance of mortality, ~ 30% to 50%.')
    with colstage44_4:
         st.image(image1)
    title1('Know more facts about Sepsis') 
    write1('According to first global report on sepsis of World Health Organization(WHO), the serious gaps in knowledge, particularly in low- and middle-income countries causes millions of deaths and disabilities due to sepsis.  Recent studies shows that 11 million people are killed and millions more are disabled due to sepsis each year.sepsis during that hospitalization.')
    write1('Approximately 85.0% of sepsis cases and sepsis-related deaths occur are of newborns, pregnant women and people living in low-resource settings.Almost half of the 49 million cases of sepsis each year occur among children, resulting in 2.9 million deaths, most of which could be prevented through early diagnosis and appropriate clinical management. To know more about the facts of sepsis, few of the references are linked below.')
         
    st.write("WHO calls for global action on sepsis [Link](https://www.who.int/news/item/08-09-2020-who-calls-for-global-action-on-sepsis---cause-of-1-in-5-deaths-worldwide)")
    st.write("WHO fact sheet on sepsis [Link](https://www.who.int/news-room/fact-sheets/detail/sepsis)")
    st.write("Sepsis incidence and mortality,1990–2017 [Link](https://www.thelancet.com/action/showPdf?pii=S0140-6736%2819%2932989-7) ")
    # with open('C:/Users/Iqbal/Desktop/web/Stages of Sepsis.pdf',"rb") as f:
    #    base64_pdf = base64.b64encode(f.read()).decode('utf-8')    
   # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'    
   # st.markdown(pdf_display, unsafe_allow_html=True)
   # st.title('What is Sepsis?')
    #st.write('Sepsis is the body’s extreme response to an infection. It is a life-threatening medical emergency.  Sepsis happens when an infection you already have triggers a chain reaction throughout your body.  Infections that lead to sepsis most often start in the lung, urinary tract, skin, or gastrointestinal tract. Without timely treatment, sepsis can rapidly lead to tissue damage, organ failure, and death.')
   # st.image("""https://www.thestreet.com/.image/ar_4:3%2Cc_fill%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTY4NjUwNDYyNTYzNDExNTkx/why-dominion-diamonds-second-trip-to-the-block-may-be-different.png""")
    #st.header('What causes sepsis?')
    #st.write('Infections can put you or your loved one at risk for sepsis. When germs get into a person’s body, they can cause an infection. If you don’t stop that infection, it can cause sepsis. Bacterial infections cause most cases of sepsis. Sepsis can also be a result of other infections, including viral infections, such as COVID-19 or influenza, or fungal infections.')
    #st.header('Stages of Sepsis')
    #st.write('Stage one: Systemic Inflammatory Response Syndrome (SIRS)Sepsis can be hard to identify, but is typically denoted by a very high or low body temperature, high heart rate, high respiratory rate, high or low white blood cell count and a known or suspected infection. The aforementioned signs are actually used to identify Systemic Inflammatory Response Syndrome (SIRS), which only becomes sepsis when an infection is present.SIRS is, in some circles, a more commonly used term because sepsis is only seen as a subcategory of SIRS. For sepsis, two of the mentioned SIRS signs, as well as an infection, need to be present.')
    #st.write('Stage two: severe sepsisThe second stage, called severe sepsis, is diagnosed when acute organ dysfunction begins. Severe sepsis can also be diagnosed when sepsis is present along with hypotension (low blood pressure) or hypoperfusion (decreased blood flow through an organ).')
    #st.write('Stage three: septic shock Septic shock is the most severe stage of sepsis. It is defined as the presence of hypotension, induced by sepsis, despite fluid resuscitation. In addition, perfusion abnormalities such as elevated lactate levels. Septic shock has the highest chance of mortality, with estimates ranging from 30% to 50%.')
  #st.markdown(
   #     """
    #    <style>
     #   [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
      #      width: 800px;
       # }
        #[data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
         #   width: 500px;
          #  margin-left: -500px;
        #}
        #</style>
        #""",
        #unsafe_allow_html=True,
        #)

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
            WBC = st.number_input('WBC', help='% immature band form')
        with col5:
             PaCO2=st.number_input('PaCO2',help='mm/Hg')    
        #t_hr=(float(Temp)> 38.5 or float(Temp) < 35) and  float(HR) > 90   
        #t_re_pa=(float(Temp)> 38.5 or float(Temp) < 35) and (float(Resp)>20 or float(PaCO2) <32)
        #t_wbc=(float(Temp)> 38.5 or float(Temp) < 35) and (float(WBC)>10)
        #hr_re_pa= float(HR) > 90  and (float(Resp)>20 or float(PaCO2) <32)
        #hr_wbc= float(HR) > 90  and (float(WBC)>10)
        #re_pa_wbc=(float(Resp)>20 or float(PaCO2) <32) and (float(WBC)>10)
        if st.button('Predict SIRS') :
            ab=predict_sirs(float(Temp),float(HR),float(Resp),float(WBC),float(PaCO2))
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
            col6,col7,col8= st.columns((1,1,1))
            with col6:
                MAP= st.number_input('MAP',help='breaths/min')    
            with col7:
                BUN= st.number_input('BUN',help='breaths/min')
            with col8:
                 FiO2= st.number_input('FiO2',help='breaths/min')   
            col9, col10,col11= st.columns((1,1,1))
            with col9:
                 pH= st.number_input('pH',help='breaths/mn')   
            with col10:
                 BaseExcess= st.number_input('BaseExcess',help='breaths/min')  
            with col11:
                  Calcium= st.number_input('Calcium',help='breaths/min')   
            col12, col13 = st.columns((1,1))
            with col12:
                Creatinine= st.number_input('Creatinine',help='breaths/min') 
            with col13:
                 Platelets= st.number_input(' Platelets',help='breaths/min')
            
                 
           
        inputdata=pd.DataFrame([[float(HR), float(Temp), float(Resp), float(MAP), float(BUN), float(FiO2), float(Creatinine),float(Platelets), float(WBC), float(pH), float(Calcium), float(BaseExcess),float(PaCO2)]], columns=['HR', 'Temp', 'Resp', 'MAP', 'BUN', 'FiO2', 'Creatinine','Platelets', 'WBC', 'pH', 'Calcium', 'BaseExcess','PaCO2'])
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
                 Lactate= st.number_input("Lactate",help='breaths/min') 
            with col21:
                 SBP= st.number_input('SBP',help='breaths/min')    
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
        
          
