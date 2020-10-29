from tqdm import tqdm 
import time 

for i in tqdm (range (100), desc="Loading..."): 
	pass

  
  
for i in tqdm (range (100), desc="Loading…",  ascii=False, ncols=75): 
    time.sleep(0.02)
