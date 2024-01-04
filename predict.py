from PIL import Image
import streamlit as st
import requests
import base64
import datetime 
from datetime import time, datetime
import time 

def make_prediction(input_data):
    url = 'http://127.0.0.1:5000/predict'
    # response = requests.post(url, json={'input': input_data})
    # prediction = response.json()
    #return prediction
    try:
        response = requests.post(url, json={'input': input_data})
        if response.status_code == 200:
            prediction = response.json()
            return prediction
        else:
            print(f"Unexpected status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

st.set_page_config(layout="centered")


def set_background(png_file):
    bin_str = base64.b64encode(open(png_file, 'rb').read()).decode()
    page_bg_img = f"""
    <style>
    body {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}

    .stApp {{
        background-color: rgba(255, 255, 255, 0.05); /* Adjust the opacity value (from 0 to 1) */
    }}

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def main():
    set_background("1.png")
    st.header('_Flight Delay Prediction_', divider='rainbow')
    st.write('Flight delays are a major operational challenge for airlines all over the world, which affects customer satisfaction, raises operating costs, and disrupts the aviation sector as a whole. In addition to interfering with passengers travel plans and causing significant financial losses for airlines, these delays also have wider economic and environmental repercussions. The goal of this project is to create predictive models that can overcome these difficulties by precisely predicting crucial aspects of airline operations, like flight delays.')

    page = st.selectbox('Go to', ['Select a Option', 'Make a Prediction', 'Visualization'])

    if page == 'Make a Prediction' :

        st.sidebar.write('Enter the following details to predict flight delay:')
        selected_date = st.sidebar.date_input("Select a date", datetime.today())
        day_of_month = selected_date.day
        sch_dep_time = st.sidebar.time_input('Scheduled Departure Time')
        sch_dep_time = sch_dep_time.hour*60 + sch_dep_time.minute
        dep_time = st.sidebar.time_input('Departure Time')
        dep_time = dep_time.hour*60 + dep_time.minute
        dep_delay = dep_time - sch_dep_time
        SCHD_ARR_TIME = st.sidebar.time_input('Scheduled Arival Time')
        SCHD_ARR_TIME = SCHD_ARR_TIME.hour*60 + SCHD_ARR_TIME.minute
        SCHD_ELAPSED_TIME =  SCHD_ARR_TIME - sch_dep_time 
        ELAPSED_TIME = st.sidebar.number_input('Journey time in minutes',min_value=0, step =1)
        if ELAPSED_TIME == 0:
            ELAPSED_TIME = SCHD_ELAPSED_TIME
        DISTANCE = st.sidebar.number_input('Distance (in miles)', min_value=0, max_value=10000, step=1)
        other_delay = st.sidebar.selectbox('External Delay - Type', ['NONE', 'Carrier Delay', 'Weather Delay', 'Security Delay', 'Late Aircraft Delay'])

        OVERALL_DELAY = 0 if other_delay == 'NONE' else st.sidebar.number_input('External Delay - Time (in minutes)', min_value=0, max_value=1440, step=1)
            
        day_of_week = st.sidebar.selectbox('Day of the Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
        day_mapping = {'Monday': 1,'Tuesday': 2,'Wednesday': 3,'Thursday': 4,'Friday': 5,'Saturday': 6,'Sunday': 7}
        selected_day = day_mapping.get(day_of_week)  
        DAY_OF_WEEK_1 = 0
        DAY_OF_WEEK_2 = 0
        DAY_OF_WEEK_3 = 0
        DAY_OF_WEEK_4 = 0
        DAY_OF_WEEK_5 = 0
        DAY_OF_WEEK_6 = 0
        DAY_OF_WEEK_7 = 0

        if 1 <= selected_day <= 7:
            globals()[f"DAY_OF_WEEK_{selected_day}"] = 1

        Airlines_Selection = st.sidebar.selectbox('Airlines', ['Endeavor Air', 'American Airlines', 'Alaska Airlines', 'JetBlue Airways', ' Delta Air Lines', 'Frontier Airlines', 'Allegiant Air','Hawaiian Airlines', 'Envoy Air', 'Spirit Airlines', ' PSA Airlines', 'SkyWest Airlines' , 'United Airlines', 'Southwest Airlines', 'American Eagle'])
        Airlines_mapping = {'Endeavor Air' : 1, 'American Airlines' : 2, 'Alaska Airlines' : 3, 'JetBlue Airways' : 4, ' Delta Air Lines' : 5, 'Frontier Airlines' : 6, 'Allegiant Air' : 7,'Hawaiian Airlines' : 8, 'Envoy Air' : 9, 'Spirit Airlines': 10, ' PSA Airlines': 11, 'SkyWest Airlines': 12 , 'United Airlines' : 13, 'Southwest Airlines': 14, 'American Eagle' : 15}

        selected_airlines = Airlines_mapping.get(Airlines_Selection)  
        if selected_airlines == 1:
            AIRLINE_9E = 1
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 2:
            AIRLINE_9E = 0
            AIRLINE_AA = 1
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 3:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 1
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0
        elif selected_airlines == 4:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 1
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 5:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 1
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 6:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 1
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 7:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 1
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 8:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 1
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 9:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 1
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 10:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 1
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 11:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 1
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 12:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 1
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 13:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 1
            AIRLINE_WN = 0
            AIRLINE_YX = 0

        elif selected_airlines == 14:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 1
            AIRLINE_YX = 0
    

        else:
            AIRLINE_9E = 0
            AIRLINE_AA = 0
            AIRLINE_AS = 0
            AIRLINE_B6 = 0
            AIRLINE_DL = 0
            AIRLINE_F9 = 0
            AIRLINE_G4 = 0
            AIRLINE_HA = 0
            AIRLINE_MQ = 0
            AIRLINE_NK = 0
            AIRLINE_OH = 0
            AIRLINE_OO = 0
            AIRLINE_UA = 0
            AIRLINE_WN = 0
            AIRLINE_YX = 1


        Origin_Selection = st.sidebar.selectbox('Origin', ['LGA', 'GSP', 'JFK', 'AVL', 'ALB', 'DTW', 'RDU', 'BNA', 'ROC',
        'CVG', 'MEM', 'ORF', 'ATL', 'HPN', 'BUF', 'PVD', 'ITH', 'MSP',
        'CLE', 'SYR', 'IND', 'ILM', 'PWM', 'CHS', 'MKE', 'OMA', 'SAV',
        'BTV', 'ORD', 'CLT', 'BWI', 'STL', 'BGR', 'LAX', 'DFW', 'AUS',
        'MIA', 'DCA', 'PHX', 'SFO', 'EGE', 'SNA', 'STT', 'SEA', 'PDX',
        'FLL', 'BOS', 'SJU', 'PBI', 'MCO', 'ORH', 'RSW', 'SMF', 'SRQ',
        'JAX', 'SAT', 'IAH', 'MSY', 'PSP', 'DEN', 'MCI', 'TPA', 'LAS',
        'ONT', 'BUR', 'BQN', 'SLC', 'PSE', 'RNO', 'BZN', 'HNL', 'SAN',
        'ISP', 'SWF', 'SFB', 'PBG', 'PIE', 'PGD', 'MYR', 'PHL', 'ELM',
        'EWR', 'DAL', 'MDW', 'HOU', 'TUL', 'PIT', 'GSO', 'CMH', 'SDF',
        'LIT', 'OKC', 'EYW', 'CHO', 'XNA', 'RIC', 'MSN', 'IAD', 'BDL',
        'BGM', 'IAG', 'DAY', 'ROA', 'MTJ', 'JAC', 'TYS', 'GRR', 'BHM',
        'CAE', 'DSM', 'SCE', 'LEX'])
        
        Origin_mapping = {'LGA': 54.0, 'GSP': 37.0, 'JFK': 50.0, 'AVL': 3.0, 'ALB': 0.0, 'DTW': 29.0, 'RDU': 85.0, 'BNA': 8.0, 'ROC': 89.0, 'CVG': 22.0, 'MEM': 59.0, 'ORF': 71.0, 'ATL': 1.0, 'HPN': 40.0, 'BUF': 12.0, 'PVD': 83.0, 'ITH': 47.0, 'MSP': 63.0, 'CLE': 19.0, 'SYR': 107.0, 'IND': 45.0, 'ILM': 44.0, 'PWM': 84.0, 'CHS': 18.0, 'MKE': 61.0, 'OMA': 68.0, 'SAV': 93.0, 'BTV': 11.0, 'ORD': 70.0, 'CLT': 20.0, 'BWI': 14.0, 'STL': 104.0, 'BGR': 6.0, 'LAX': 52.0, 'DFW': 27.0, 'AUS': 2.0, 'MIA': 60.0, 'DCA': 25.0, 'PHX': 78.0, 'SFO': 98.0, 'EGE': 30.0, 'SNA': 102.0, 'STT': 105.0, 'SEA': 96.0, 'PDX': 75.0, 'FLL': 34.0, 'BOS': 9.0, 'SJU': 99.0, 'PBI': 74.0, 'MCO': 57.0, 'ORH': 72.0, 'RSW': 90.0, 'SMF': 101.0, 'SRQ': 103.0, 'JAX': 49.0, 'SAT': 92.0, 'IAH': 43.0, 'MSY': 64.0, 'PSP': 82.0, 'DEN': 26.0, 'MCI': 56.0, 'TPA': 108.0, 'LAS': 51.0, 'ONT': 69.0, 'BUR': 13.0, 'BQN': 10.0, 'SLC': 100.0, 'PSE': 81.0, 'RNO': 87.0, 'BZN': 15.0, 'HNL': 38.0, 'SAN': 91.0, 'ISP': 46.0, 'SWF': 106.0, 'SFB': 97.0, 'PBG': 73.0, 'PIE': 79.0, 'PGD': 76.0, 'MYR': 66.0, 'PHL': 77.0, 'ELM': 31.0, 'EWR': 32.0, 'DAL': 23.0, 'MDW': 58.0, 'HOU': 39.0, 'TUL': 109.0, 'PIT': 80.0, 'GSO': 36.0, 'CMH': 21.0, 'SDF': 95.0, 'LIT': 55.0, 'OKC': 67.0, 'EYW': 33.0, 'CHO': 17.0, 'XNA': 111.0, 'RIC': 86.0, 'MSN': 62.0, 'IAD': 41.0, 'BDL': 4.0, 'BGM': 5.0, 'IAG': 42.0, 'DAY': 24.0, 'ROA': 88.0, 'MTJ': 65.0, 'JAC': 48.0, 'TYS': 110.0, 'GRR': 35.0, 'BHM': 7.0, 'CAE': 16.0, 'DSM': 28.0, 'SCE': 94.0, 'LEX': 53.0}
        
        ORIGIN = Origin_mapping.get(Origin_Selection)


        DEST_Selection = st.sidebar.selectbox('Destination', ['RDU', 'LGA', 'GSP', 'DTW', 'MSP', 'AVL', 'ALB', 'BUF', 'BNA',
        'MKE', 'JFK', 'CLT', 'ROC', 'MEM', 'PWM', 'ORF', 'HPN', 'ATL',
        'ITH', 'CHS', 'SAV', 'CLE', 'SYR', 'ILM', 'IND', 'CVG', 'BTV',
        'MCI', 'ORD', 'BGR', 'PVD', 'STL', 'BWI', 'OMA', 'LAX', 'DFW',
        'MIA', 'DCA', 'PHX', 'EGE', 'SFO', 'AUS', 'STT', 'SNA', 'SEA',
        'SAN', 'PDX', 'PBI', 'MCO', 'BOS', 'LAS', 'TPA', 'JAX', 'RSW',
        'FLL', 'SJU', 'SMF', 'SRQ', 'MSY', 'PSP', 'IAH', 'DEN', 'BQN',
        'ONT', 'BUR', 'SLC', 'SAT', 'PSE', 'ORH', 'RNO', 'BZN', 'ISP',
        'SWF', 'PBG', 'SFB', 'PIE', 'PGD', 'HNL', 'MYR', 'PHL', 'ELM',
        'EWR', 'DAL', 'MDW', 'HOU', 'CMH', 'RIC', 'TUL', 'LIT', 'SDF',
        'OKC', 'XNA', 'EYW', 'CHO', 'PIT', 'GSO', 'MSN', 'IAD', 'BDL',
        'BGM', 'IAG', 'DAY', 'ROA', 'JAC', 'MTJ', 'SCE', 'TYS', 'DSM',
        'BHM', 'GRR', 'CAE', 'LEX'])
        
        DEST_mapping = {'RDU': 85.0, 'LGA': 54.0, 'GSP': 37.0, 'DTW': 29.0, 'MSP': 63.0, 'AVL': 3.0, 'ALB': 0.0, 'BUF': 12.0, 'BNA': 8.0, 'MKE': 61.0, 'JFK': 50.0, 'CLT': 20.0, 'ROC': 89.0, 'MEM': 59.0, 'PWM': 84.0, 'ORF': 71.0, 'HPN': 40.0, 'ATL': 1.0, 'ITH': 47.0, 'CHS': 18.0, 'SAV': 93.0, 'CLE': 19.0, 'SYR': 107.0, 'ILM': 44.0, 'IND': 45.0, 'CVG': 22.0, 'BTV': 11.0, 'MCI': 56.0, 'ORD': 70.0, 'BGR': 6.0, 'PVD': 83.0, 'STL': 104.0, 'BWI': 14.0, 'OMA': 68.0, 'LAX': 52.0, 'DFW': 27.0, 'MIA': 60.0, 'DCA': 25.0, 'PHX': 78.0, 'EGE': 30.0, 'SFO': 98.0, 'AUS': 2.0, 'STT': 105.0, 'SNA': 102.0, 'SEA': 96.0, 'SAN': 91.0, 'PDX': 75.0, 'PBI': 74.0, 'MCO': 57.0, 'BOS': 9.0, 'LAS': 51.0, 'TPA': 108.0, 'JAX': 49.0, 'RSW': 90.0, 'FLL': 34.0, 'SJU': 99.0, 'SMF': 101.0, 'SRQ': 103.0, 'MSY': 64.0, 'PSP': 82.0, 'IAH': 43.0, 'DEN': 26.0, 'BQN': 10.0, 'ONT': 69.0, 'BUR': 13.0, 'SLC': 100.0, 'SAT': 92.0, 'PSE': 81.0, 'ORH': 72.0, 'RNO': 87.0, 'BZN': 15.0, 'ISP': 46.0, 'SWF': 106.0, 'PBG': 73.0, 'SFB': 97.0, 'PIE': 79.0, 'PGD': 76.0, 'HNL': 38.0, 'MYR': 66.0, 'PHL': 77.0, 'ELM': 31.0, 'EWR': 32.0, 'DAL': 23.0, 'MDW': 58.0, 'HOU': 39.0, 'CMH': 21.0, 'RIC': 86.0, 'TUL': 109.0, 'LIT': 55.0, 'SDF': 95.0, 'OKC': 67.0, 'XNA': 111.0, 'EYW': 33.0, 'CHO': 17.0, 'PIT': 80.0, 'GSO': 36.0, 'MSN': 62.0, 'IAD': 41.0, 'BDL': 4.0, 'BGM': 5.0, 'IAG': 42.0, 'DAY': 24.0, 'ROA': 88.0, 'JAC': 48.0, 'MTJ': 65.0, 'SCE': 94.0, 'TYS': 110.0, 'DSM': 28.0, 'BHM': 7.0, 'GRR': 35.0, 'CAE': 16.0, 'LEX': 53.0}
        
        DEST = DEST_mapping.get(DEST_Selection)  

        input_features = [day_of_month, sch_dep_time, dep_time, dep_delay, SCHD_ARR_TIME,
                            SCHD_ELAPSED_TIME, 
                            ELAPSED_TIME,  DISTANCE, 
                            DAY_OF_WEEK_1, DAY_OF_WEEK_2,
                            DAY_OF_WEEK_3, DAY_OF_WEEK_4, DAY_OF_WEEK_5, DAY_OF_WEEK_6, DAY_OF_WEEK_7,
                            AIRLINE_9E, AIRLINE_AA, AIRLINE_AS, AIRLINE_B6, AIRLINE_DL, AIRLINE_F9,
                            AIRLINE_G4, AIRLINE_HA, AIRLINE_MQ, AIRLINE_NK, AIRLINE_OH, AIRLINE_OO,
                            AIRLINE_UA, AIRLINE_WN, AIRLINE_YX, ORIGIN, DEST, OVERALL_DELAY ] 

        prediction = None


        if st.sidebar.button('Predict'):
            prediction = make_prediction(input_features)

        if prediction is not None:
            pre = prediction["prediction"][0]
            pre = round(pre)
            if pre > 0:
                st.markdown(f"<h1 style='color:white; text-align:center;'>Predicted Arrival Delay: {round(pre)} Minutes</h1>", unsafe_allow_html=True)
            elif pre < 0:
                pre = round(-pre)
                st.markdown(f"<h1 style='color:white; text-align:center;'>Predicted Early Arrival: {pre} Minutes</h1>", unsafe_allow_html=True)
            else:
                st.markdown("<h1 style='color:white; text-align:center;'>Flight is on Right Time</h1>", unsafe_allow_html=True)
        else:
            st.error(" ")

    elif page == 'Visualization':
        col1, col2 = st.columns(2)  

        with col1:
            st.image('1st.png', use_column_width=True)
            st.markdown("<p style='color: white;'>Airports Where Fights are delayed at the Origin itself</p>", unsafe_allow_html=True)

            st.image('3rd.png', use_column_width=True)
            st.markdown("<p style='color: white;'>Average Delay Of aircarft by each Airlines</p>", unsafe_allow_html=True)

        with col2:
            st.image('2nd.png', use_column_width=True) 
            st.markdown("<p style='color: white;'>Days on which Most Delays occurs</p>", unsafe_allow_html=True)

            st.image('4th.png', use_column_width=True)
            st.markdown("<p style='color: white;'>Hour Analysis - At which hour most delays occur </p>", unsafe_allow_html=True)


    else:
        st.write('Select One of the two options')

if __name__ == '__main__':
    main()
