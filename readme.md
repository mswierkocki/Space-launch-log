# Filmoteka
> "rocket science" script. 

Parse [log](http://planet4589.org/space/log/launchlog.txt) of satellite orbital [lauches](http://planet4589.org/space/log/launch.html)

Function  which will parse  object, aggregate count by,
filter if launch succeeded (or group_by( , , =None) stream field success stream field not) and return dict of aggregations.

***

### Inputs

- **stream - stream object like from open**
- **field  - or  "year" "month"**
- **success -**
    - None (don't filter) 
    - True (success)
    - False (failed) - use column Suc 

### Output
dict with format ```{FIELD: int} ```

## Example
```python
 group_by(open("launchlog.txt"), 'year')

 Out[]: { 
'1957': 4,
'1958': 28,
'1959': 31,
'1960': 66,
 … 
}
 group_by(open("launchlog.txt"), 'month', success=False)

 Out[]: {
    'Apr': 940,
    'Aug': 847, 
    … 
}
```






