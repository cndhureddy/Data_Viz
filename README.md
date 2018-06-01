# About the Application

Application visualises the Project Statistics over the years 2000 to 2018. These Projects are done by Center for Learning and Teaching Department of Old Dominion University.  

## Building of the Application:  

### Data Collection:  
  
`CLT/App/data/clt.project.dbo.json` is the original source of data containing details of the Projects.  
  
I have written Python Scripts to parse and get the required data in the form of .json and .csv to visualize the data. Those Python scripts can be found at `CLT/App/data/Python_Scripts`.  
  
### Data Visualization:  

I have used json and csv data files to form charts using D3.js java script Library. I have used Bubble Chart, Horizontal Bar Chart, Stacked Bar Chart and Pie Chart to serve the purpose. Tooltips used in the Chart help us to view some additional information while hovering over those charts. 

### Coding:

Coding is done using Python,PHP and Javascript.

## Starting the Web Application:

Open `CLT/App/Index/Home.php` which is the Home page of the App in a Web Server Compatible with PHP and HTML.

## Using the Application:

In the home page, there are 3 options in the navigation bar:
1. Home, 
2. Tables and
3. Bubble Chart

* Home: Home page Gives the overview of Project Statistices from 2000-2018. It contains a dropdown list containing all the years from 2000 to 2018. When an year is selected, project statistics of that year are displayed. 

* Tables: Navigating to tables displays a page with tables give some additional details about the projects. This file can be found at `CLT/App/Index/tables.html`

* Bubble Chart: This page contains the bubbles corresponding to years and their size is based on the number of projects done in those years. Hovering over the Chart gives the number of projects done and On-Click of the bubble contacing year, one can see the project statistics of the respective year. This file can be found at `CLT/App/Index/bubblechart.html`

At any instance, one can navigate to any of the above 3 pages using the options in the navigation bar. 


