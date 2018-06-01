import json
#json_data=open("data.csv").read()
 #import csv
#data = json.loads(json_data)
#print(data)

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

year_array = []
with open('clt.project.dbo.json') as json_data:
   d = json.load(json_data)
   #print(d)
   data=d["items"]
with open('data_json.json', 'w') as outfile:
   json.dump(data, outfile)
   
with open('data_json.json') as json_data:
	temp_d1 =json.load(json_data)
for i in range(0,len(temp_d1)):
	d1=temp_d1[i]
	due_date=d1["due_date"]
	#index_year=due_date.index("-")
	#print(due_date)
	
	index_month=find(due_date,"-")
	#print(index_month)
	year_array.append(due_date[0:4])
	
unique_year=list(set(year_array))
completed_dic={}
not_completed_dic={}
final_array=[]
for i in range(0,len(unique_year)):
	count_completed=0;
	count_not_completed=0;
	temp_dic={}
	for j in range(0,len(temp_d1)):
		d1=temp_d1[j]
		due_date=d1["due_date"]
	#index_year=due_date.index("-")
	#p#rint(due_date)
	
		#index_month=find(due_date,"-")
		year_temp=due_date[0:4]
		#print(year_temp)
		
		if int(year_temp)==int(unique_year[i]):
			#print("hi")
			temporary=d1["completed"]
			if "true" not in temporary:
				count_not_completed=count_not_completed+1;
			else:
				count_completed=count_completed+1;
				
				#print("hi")
	
	temp_dic["year"]=unique_year[i];
	temp_dic["completed"]=count_completed;
	temp_dic["not completed"]=count_not_completed;
	completed_dic[unique_year[i]]=count_completed;
	not_completed_dic[unique_year[i]]=count_not_completed;
	final_array.append(temp_dic);
#print(completed_dic)
#print(not_completed_dic)
print(final_array)
with open('data_final_dic_completed_sbar.json', 'w') as outfile:
   json.dump(final_array, outfile)
