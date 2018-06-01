<html>
<title>CLT Home</title>
<style> /* set the CSS */

.bar { fill: #800000; }
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    border: 1px solid #e7e7e7;
    background-color: #f3f3f3;
}

li {
    float: left;
}

li a {
    display: block;
    color: #000000;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #ddd;
}

li a.active {
    color: white;
    background-color: #000000;
}
</style>
<body>
<ul>
  <li><a class="active" href="test2.php?year=2000-2018">HOME</a></li>
  <li><a href="tables.html">Tables</a></li>
  <li><a href="bubblechart.html">Bubble chart</a></li>
  
</ul>

<script src="https://d3js.org/d3.v4.min.js"></script>
<br></br>
<center><h1>Project Statistics Overview from 2000-2018</h1>

<!--<br></br><h1>Bubble Chart</h1> -->
<br></br>
<form action="test2.php" method="get">
  year: <select name="year">
  <option value="2000-2018"</option>
  <option value="2000">2000</option>
  <option value="2001">2001</option>
  <option value="2002">2002</option>
  <option value="2003">2003</option>
  <option value="2004">2004</option>
  <option value="2005">2005</option>
  <option value="2006">2006</option>
  <option value="2007">2007</option>
  <option value="2008">2008</option>
  <option value="2009">2009</option>
  <option value="2010">2010</option>
  <option value="2011">2011</option>
  <option value="2012">2012</option>
  <option value="2013">2013</option>
  <option value="2014">2014</option>
  <option value="2015">2015</option>
  <option value="2016">2016</option>
  <option value="2017">2017</option>
  <option value="2018">2018</option>
</select>
<input type="submit" value="Submit">
</form>
<?php 
//echo $_GET["year"]; 
$year = $_GET["year"];
//echo $year;
$filename = "bc_".$year.".html";
//echo $filename;

$xml = file_get_contents($filename);
echo $xml;
?>
<br></br>

</body>
</html>