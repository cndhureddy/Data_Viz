import json
from datetime import datetime
year_array = []
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]
due_date_array = []
completed_date_array = []
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
	#proj_no = d1[proj]
	due_date=d1["due_date"]
	index_month=find(due_date,"-")
	year_array.append(due_date[0:4])
	
	#index_month=find(due_date,"-")
	#year_array.append(due_date[0:4])
	try:
		completed_date=d1["completed_date"]
	except Exception as e:
		completed_date='2020-12-12'
	
	#print(due_date)
	#index_month=find(due_date,"-")
	#print(index_month)
	due_date_array.append(due_date[0:10])
	#try:
	completed_date_array.append(completed_date[0:10])
	#except ValueError:
	#comleted_date_array.append('0000-00-00')
#print(due_date_array)
#print("hi")
#print(completed_date_array)
#print("hello")

unique_year=list(set(year_array))
for i in range(0,len(unique_year)):
	tcount_projects_not_completed = 0
	tcount_duedata_greater_completeddate = 0
	tcount_duedata_less_completeddate = 0
	tcount_duedata_equal_completeddate = 0
	d= datetime.strptime(unique_year[i] , '%Y').date()

	#print(d.year)
	for i in range(0,len(due_date_array)):
		from datetime import datetime
		ta = datetime.strptime(due_date_array[i] , '%Y-%m-%d').date()
		tb = datetime.strptime(completed_date_array[i] , '%Y-%m-%d').date()
		tc = datetime.strptime('2020-12-12','%Y-%m-%d').date()
		if d.year == ta.year:
	#print(b)
			if tb== tc:
				tcount_projects_not_completed = tcount_projects_not_completed + 1
			else: 
				if ta>tb:
					tcount_duedata_greater_completeddate = tcount_duedata_greater_completeddate + 1
				if ta<tb:
					tcount_duedata_less_completeddate = tcount_duedata_less_completeddate + 1
				if ta==tb:
					tcount_duedata_equal_completeddate = tcount_duedata_equal_completeddate + 1 
	#print("hi")
    #datetime.datetime(d[i])
	print(tcount_duedata_greater_completeddate)
	print(tcount_duedata_less_completeddate)
	print(tcount_duedata_equal_completeddate)
	print(tcount_projects_not_completed)
	final_array=[]
	temp_dic={}
	temp_dic["duedate<completeddate"]=tcount_duedata_less_completeddate;
	temp_dic["duedate=completeddate"]=tcount_duedata_equal_completeddate;
	temp_dic["duedate>completeddate"]=tcount_duedata_greater_completeddate;
	temp_dic["projects_notcompleted"]=tcount_projects_not_completed;
	final_array.append(temp_dic)
	print(final_array)
	file_name="data_final_dic_pie"+str(d.year)+".json"
	with open(file_name, 'w') as outfile:
		json.dump(final_array, outfile) 

count_projects_not_completed = 0
count_duedata_greater_completeddate = 0
count_duedata_less_completeddate = 0
count_duedata_equal_completeddate = 0

for i in range(0,len(due_date_array)):
	from datetime import datetime
	a = datetime.strptime(due_date_array[i] , '%Y-%m-%d').date()
	b = datetime.strptime(completed_date_array[i] , '%Y-%m-%d').date()
	c = datetime.strptime('2020-12-12','%Y-%m-%d').date()
	#print(b)
	if b== c:
		count_projects_not_completed = count_projects_not_completed + 1
	else: 
		if a>b:
			count_duedata_greater_completeddate = count_duedata_greater_completeddate + 1
		if a<b:
			count_duedata_less_completeddate = count_duedata_less_completeddate + 1
		if a==b:
			count_duedata_equal_completeddate = count_duedata_equal_completeddate + 1 

	#print("hi")
    #datetime.datetime(d[i])
print(count_duedata_greater_completeddate)
print(count_duedata_less_completeddate)
print(count_duedata_equal_completeddate)
print(count_projects_not_completed)

	#print(datetime.date(due_date))
	#progress_array.append(progress)
'''unique_progress=list(set(progress_array))
print(unique_progress)'''
final_array=[]
#temporary_array = []
#for i in range(0,len(unique_year)):
#for i in range(0,len(unique_year)):
	#count_submitted=0;
	#count_projects=0
	#count_not_submitted=0;'''
temp_dic={}
'''for j in range(0,len(temp_d1)):
		d1=temp_d1[j]
		#due_date=d1["due_date"]
		progress=d1["progress"]
		if unique_progress[i] not in progress:
			#count_projects = count_projects
			dev=0
		else:
			count_projects = count_projects+1
	#print(count_projects)
	temporary_array.append(count_projects)
#print(temporary_array)
	temp_dic["progress"]=unique_progress[i];'''
temp_dic["duedate<completeddate"]=count_duedata_less_completeddate;
temp_dic["duedate=completeddate"]=count_duedata_equal_completeddate;
temp_dic["duedate>completeddate"]=count_duedata_greater_completeddate;
temp_dic["projects_notcompleted"]=count_projects_not_completed;
final_array.append(temp_dic)
print(final_array)
with open('data_final_dic_pie.json', 'w') as outfile:
   json.dump(final_array, outfile) 

'''for i in range(0,len(temp_d1)):
	d1=temp_d1[i]
	#proj_no = d1[proj]
	due_date=d1["due_date"]
	index_month=find(due_date,"-")
	year_array.append(due_date[0:4])
unique_year=list(set(year_array))


for i in range(0,len(unique_year)):
	d= datetime.strptime(unique_year[i] , '%Y').date()
	print(d.year)

#print(unique_year)'''

	


