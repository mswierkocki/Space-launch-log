
"rocket science" script.
Parse log of satellite orbital lauches  (descr http://planet4589.org/space/log/launchlog.txt iption: ). http://planet4589.org/space/log/launch.html
Write a function  which will parse  object, aggregate count by,
filter if launch succeeded (or group_by( , , =None) stream field success stream field not) 
and return dict of aggregations.

Inputs
stream - stream object like from open field  - or  "year" "month" success -  (don't filter) ,  (success),  (failed) - please use column Suc None True False

Output
dict with format {FIELD: int}

Example

 group_by(open("launchlog.txt"), 'year')
 Out[]: { '1957': 4, '1958': 28, '1959': 31, '1960': 66, … }
 
 group_by(open("launchlog.txt"), 'month', success=False)
 Out[]: { 'Apr': 940, 'Aug': 847, 