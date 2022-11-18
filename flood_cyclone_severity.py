def calculate_severity(inputs):
    result=[]
    avg_severity=0
    total_severity=0
    for input_val in inputs:
        parameter=input_val[0]
        severity=0
        if parameter=="Rainfall intensity":
            rainfall_intensity=input_val[1]
            if rainfall_intensity<=900:
                severity= 1
            elif rainfall_intensity>900 and rainfall_intensity<=1000:
                severity= 2
            elif rainfall_intensity>1000 and rainfall_intensity<=1100:
                severity= 3
            elif rainfall_intensity>1100 and rainfall_intensity<=1200:
                severity= 4
            elif rainfall_intensity>1200:
                severity= 5
        elif parameter=="river density":
            river_density=input_val[1]
            if river_density>0 and river_density<=2:
                severity= 1
            elif river_density>2 and river_density<=4:
                severity= 2
            elif river_density>4 and river_density<=6:
                severity= 3
            elif river_density>6 and river_density<=8:
                severity= 4
            elif river_density>8:
                severity= 5
        elif parameter=="slope":
            slope=input_val[1]
            if slope>4 and slope<4.9:
                severity= 1
            elif slope>5 and slope<5.9:
                severity= 2
            elif slope>6 and slope<6.9:
                severity= 3
            elif slope>7 and slope<7.9:
                severity= 4
            elif slope>8:
                severity= 5
        elif parameter=="Elevation":
            elevation=input_val[1]
            if elevation >=800:
                severity= 1
            elif elevation>=600 and elevation<800:
                severity= 2
            elif elevation>=400 and elevation<600:
                severity= 3
            elif elevation>=200 and elevation<400:
                severity= 4
            elif elevation<200:
                severity= 5
        elif parameter=="Soil Permeability":
            soil_permeability=input_val[1]
            if soil_permeability >=12.5:
                severity= 1
            elif soil_permeability>=6.25 and soil_permeability<12.5:
                severity= 2
            elif soil_permeability>=2 and soil_permeability<6.25:
                severity= 3
            elif soil_permeability>=0.5 and soil_permeability<2:
                severity= 4
            elif soil_permeability<0.5:
                severity= 5
            break
        elif parameter=="Land use":
            Land_use=input_val[1]
            if Land_use =="Forest":
                severity= 1
            elif Land_use=="Mixed Activity":
                severity= 2
            elif Land_use=="Urban":
                severity= 3
            elif Land_use=="Agriculture":
                severity= 4
            elif Land_use=="Water":
                severity= 5
        elif parameter=="Soil texture":
            Soil_text=input_val[1]
            if Soil_text =="clay loam":
                severity = 1
            elif Soil_text=="loam":
                severity= 2
            elif Soil_text=="sandy clay loam":
                severity= 3
            elif Soil_text=="sandy clay":
                severity= 4
            elif Soil_text=="clay":
                severity= 5
        elif parameter=="Distance From River":
            Dist_river=input_val[1]
            if Dist_river <=50:
                severity= 1
            elif Dist_river>=51 and Dist_river<150:
                severity= 2
            elif Dist_river>=150 and Dist_river<400:
                severity= 3
            elif Dist_river>=401 and Dist_river<1000:
                severity= 4
            elif Dist_river>=1000:
                severity= 5
        elif parameter=="Geology":
            Geology=input_val[1]
            if Geology =="metamorphic rocks":
                severity= 1
            elif Geology=="magmatic rocks":
                severity= 2
            elif Geology=="carbonnate rocks":
                severity= 3
            elif Geology=="clastic rocks":
                severity= 4
            elif Geology=="loose":
                severity= 5
        elif parameter=="Flood depth":
            flood_depth=input_val[1]
            if flood_depth <=0.1:
                severity= 1
            elif flood_depth>0.1 and flood_depth<0.2:
                severity= 2
            elif flood_depth>=0.2 and flood_depth<0.5:
                severity= 3
            elif flood_depth>=0.5 and flood_depth<0.8:
                severity= 4
            elif flood_depth>=0.8:
                severity= 5
        elif parameter =="windspeed Severity":
            windspeed=input_val[1]
            if windspeed<=79:
                severity=0
            elif windspeed >=80 and windspeed<149:
                severity=1
                
            elif windspeed>=150 and windspeed<180:
                severity=2
                
            elif windspeed >=180 and windspeed<210:
                severity=3
                
            elif windspeed>=210  and windspeed<250:
                severity=4
                
            elif windspeed>=250:
                severity=5 
        elif "temprature Severity"==parameter:
            temprature=input_val[1]
            if temprature<=20:
                severity=0
            elif temprature >=21 and temprature<24:
                severity=1
                
            elif temprature>=24 and temprature<25:
                severity=2
                
            elif temprature >=25 and temprature<27:
                severity=3
                
            elif temprature>=27  and temprature<28:
                severity=4
                
            elif temprature>=28:
                severity=5  
        elif "humidity Severity"==parameter:
            humidity=input_val[1]
            if humidity <30:
                severity=0
            elif humidity >=30 and humidity<40:
                severity=1
                
            elif humidity>=40 and humidity<45:
                severity=2
                
            elif humidity >=45 and humidity<50:
                severity=3
                
            elif humidity>=50  and humidity<60:
                severity=4
                
            elif humidity>=60:
                severity=5  
        elif "Pressure Severity"==parameter:
            Pressure=input_val[1]
            if Pressure <100:
                severity=0
            elif Pressure >=100 and Pressure<150:
                severity=1
                
            elif Pressure>=150 and Pressure<200:
                severity=2
                
            elif Pressure >=200 and Pressure<250:
                severity=3
                
            elif Pressure>=250  and Pressure<300:
                severity=4
                
            elif Pressure>=300:
                severity=5
        elif "Rainfall intensity"==parameter:
            Rainfall=input_val[1]
            if Rainfall <30:
                severity=0
            elif Rainfall >=30 and Rainfall<108:
                severity=1
                
            elif Rainfall>=108 and Rainfall<337:
                severity=2
                
            elif Rainfall >=337 and Rainfall<863:
                severity=3
                
            elif Rainfall>=863 and Rainfall <1000:
                severity=4
                
            elif Rainfall>=1000:
                severity=5  
        elif parameter=="Position with respect to Equator NH SH":
            Hemisphere=input_val[1]
            if Hemisphere=="South_Hemisphere":
                severity=3
                print(Hemisphere ) 
            elif Hemisphere=="North_Hemisphere":
                print(Hemisphere )
                severity=5
        elif parameter== "displacement by latitude from equator":
            displacement_by_latitude=input_val[1]
            if displacement_by_latitude<2:
                severity=0
            elif displacement_by_latitude>=2 and displacement_by_latitude<3:
                severity=1
            elif displacement_by_latitude>=3 and displacement_by_latitude<5:
                severity=3
            elif displacement_by_latitude==5:
                severity=4
            elif displacement_by_latitude>5 :
                severity=5
        total_severity+=severity
        result.append((parameter,severity))
    avg_severity=int(total_severity/len(inputs))
    return result,avg_severity

