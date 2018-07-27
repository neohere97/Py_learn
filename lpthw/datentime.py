from datetime import *
from parse import *


inp0 = "1D6h5m5s9ms" 
inp1 = "9h6m4s6ms"

IN0 = inp0.lower().replace('ms','j')
IN1 = inp1.lower().replace('ms','j')
inp = [IN0,IN1]

timeDictionary = {"d":"{}d","h":"{}h","m":"{}m","s":"{}s","j":"{}j"}
timeList = [['d','h','m','s','j'],['d','h','m','s','j']]
parseCode = ['','']

for j in range(0,2):    
    for i in range(0,5):        
        if(inp[j].find(timeList[j][i])>0 ):                        
            parseCode[j] += timeDictionary[timeList[j][i]]
        else:
            timeList[j][i] = ''
    p = 0  
    a = parse(parseCode[j],inp[j])
    for k in range(0,5):
        if(timeList[j][k] != ''):            
            timeList[j][k] = int(a[p])
            p +=1
        else:
            timeList[j][k] = 0

inp1_data = timedelta(days = timeList[0][0],hours = timeList[0][1], minutes = timeList[0][2],seconds = timeList[0][3], milliseconds = timeList[0][4])
inp2_data = timedelta(days = timeList[1][0],hours = timeList[1][1], minutes = timeList[1][2],seconds = timeList[1][3], milliseconds = timeList[1][4])


 # timeDictionary = {"d":"{}d","h":"{}h","m":"{}m","s":"{}s","j":"{}j"}
        # timeList = [['d','h','m','s','j'],['d','h','m','s','j']]
        # parseCode = ['','']
        # out_data = None

        # try:
        #     for j in range(0,2):    
        #         for i in range(0,5):        
        #             if(inp[j].find(timeList[j][i])>0 ):                        
        #                 parseCode[j] += timeDictionary[timeList[j][i]]
        #             else:
        #                 timeList[j][i] = ''
        #         p = 0  
        #         a = parse(parseCode[j],inp[j])
        #         for k in range(0,5):
        #             if(timeList[j][k] != ''):            
        #                 timeList[j][k] = float(a[p])
        #                 p +=1
        #             else:
        #                 timeList[j][k] = 0
        
        
        #     inp1_data = timedelta(days = timeList[0][0],hours = timeList[0][1], minutes = timeList[0][2],seconds = timeList[0][3], milliseconds = timeList[0][4])
        #     inp2_data = timedelta(days = timeList[1][0],hours = timeList[1][1], minutes = timeList[1][2],seconds = timeList[1][3], milliseconds = timeList[1][4])
            
        #     sum_time = inp1_data + inp2_data 

        #     out_days= str(sum_time.days) + 'd'
        #     out_hours = str(sum_time.seconds//3600) + 'h'
        #     out_minutes = str((sum_time.seconds%3600)//60) + 'm'
        #     out_seconds = str(sum_time.seconds%60) + 's'
        #     out_milliseconds = str(sum_time.microseconds/1000) + 'ms'

        #     if(out_days == '0d'):
        #         out_days = ''
        #         if(out_hours == '0h'):
        #             out_hours = ''
        #             if(out_minutes == '0m'):
        #                 out_minutes = ''
        #                 if(out_seconds == '0s'):
        #                     out_seconds = ''        
        # except (TypeError,ValueError):
        #     out_data = "error"
        #     framework.errors.append("input data in the functional_block "+self.name+" is not formatted or invalid")

        # if(out_data != 'error'):
        #     out_data = f"{out_days}{out_hours}{out_minutes}{out_seconds}{out_milliseconds}"   



