import json
status_array = []
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
	#due_date=d1["due_date"]
	status=d1["status"]
	status_array.append(status)
unique_status=list(set(status_array))
print(unique_status)
final_array=[]
temporary_array = []
#for i in range(0,len(unique_year)):
for i in range(0,len(unique_status)):
	#count_submitted=0;
	count_projects=0
	#count_not_submitted=0;
	temp_dic={}
	for j in range(0,len(temp_d1)):
		d1=temp_d1[j]
		#due_date=d1["due_date"]
		status=d1["status"]
		if unique_status[i] not in status:
			#count_projects = count_projects
			dev=0
		else:
			count_projects = count_projects+1
	#print(count_projects)
	temporary_array.append(count_projects)
#print(temporary_array)
	temp_dic["status"]=unique_status[i];
	temp_dic["projects"]=count_projects;
	final_array.append(temp_dic)
	print(final_array)
with open('data_final_dic_status_bar.json', 'w') as outfile:
   json.dump(final_array, outfile) 
