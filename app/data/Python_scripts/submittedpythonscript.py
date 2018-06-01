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
submitted_dic={}
not_submitted_dic={}
final_array=[]
for i in range(0,len(unique_year)):
	count_submitted=0;
	count_not_submitted=0;
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
			temporary=d1["submitted"]
			if "true" not in temporary:
				count_not_submitted=count_not_submitted+1;
			else:
				count_submitted=count_submitted+1;
				
				#print("hi")
	
	temp_dic["year"]=unique_year[i];
	temp_dic["submitted"]=count_submitted;
	temp_dic["not submitted"]=count_not_submitted;
	submitted_dic[unique_year[i]]=count_submitted;
	not_submitted_dic[unique_year[i]]=count_not_submitted;
	final_array.append(temp_dic);
#print(submitted_dic)
#print(not_submitted_dic)
print(final_array)
with open('data_final_dic_submitted_sbar.json', 'w') as outfile:
   json.dump(final_array, outfile)
