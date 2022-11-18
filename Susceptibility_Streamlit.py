import streamlit as st
import flood_cyclone_severity as severity
import pandas as pd
import numpy as np

def main():
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.title("Susceptibility Index")
    option=st.sidebar.selectbox(
        label="Select Disaster",
        options=["Cyclone","Flood"]
    )

    intensity_parameter={
        "Flood":["Rainfall intensity","river density",
        "slope","Elevation","Soil Permeability","Land use",
        "Soil texture","Distance From River","Geology","Flood depth"],
        
        "Cyclone":["windspeed Severity","temprature Severity",
        "humidity Severity","Pressure Severity","Rainfall intensity",
        "Position with respect to Equator NH SH",
        "displacement by latitude from equator"]
    }

    flood_parameters_range={
        "Rainfall intensity":[0,12000],
        "river density":[0,100],
        "slope":[0,100],
        "Elevation":[0,10000],
        "Soil Permeability":[0,20],
        "Distance From River":[0,10000],
        "Flood depth":[0.00,1.00],
        "windspeed Severity":[0,2500],
        "temprature Severity":[0,280],
        "humidity Severity":[0,600],
        "Pressure Severity":[0,3000],
        "Rainfall intensity":[0,10000],
        "displacement by latitude from equator":[0,10]
    }
    flood_parameters_values={
        "Geology":[
            "metamorphic rocks",
            "magmatic rocks",
            "carbonnate rocks",
            "clastic rocks",
            "loose"
        ],
        "Soil texture":[
            "clay loam",
            "loam",
            "sandy clay loam",
            "sandy clay",
            "clay"
        ],
        "Land use":[
            "Forest",
            "Mixed Activity",
            "Urban",
            "Agriculture",
            "Water"
        ],
        "Position with respect to Equator NH SH":[ 
            "South_Hemisphere" , 
            "North_Hemisphere"
        ]
    }

    selected_parameters=st.multiselect(
        "Select Intensity Parameters",
        intensity_parameter[option]
    )
    input_parameters=[]
    range_keys=flood_parameters_range.keys()
    value_keys=flood_parameters_values.keys()

    for parameter in selected_parameters:
        if(parameter in range_keys):
            input_parameters.append(
                [
                    parameter,
                    st.number_input(
                    parameter,
                    min_value=flood_parameters_range[parameter][0],
                    max_value=flood_parameters_range[parameter][1]
                    )
                ]
            )
        elif parameter in value_keys:
            input_parameters.append(
                [
                    parameter,

                    st.selectbox(
                    label=parameter,
                    options=flood_parameters_values[parameter]
                    )
                ]
            )
    print(input_parameters)
    if(len(input_parameters)>0):
        result,final_severity=severity.calculate_severity(input_parameters)
        print(result)
        if((not result is None) and len(result)>0):
            result=pd.DataFrame(
                np.array(result),
                columns=["Parameter","Severity Level"],
            )
            st.table(result)
            if(final_severity>0):
                st.subheader(f"Susceptibility Index for {option} is {final_severity}")


if __name__=="__main__":
    main()