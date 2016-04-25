# weatherYahoo

Simple Python script for the yahoo weather !
========================================================

Find your weather code (woeid) 

* [Get your WOEID code ](http://woeid.rosselliot.co.nz/) 

## How to use

`python weatherYahoo.py 615702`
  
`python weatherYahoo.py location_code`
  

        location_code  [Format woeid] The location code for the region you want to
                       retrieve weather. Example : Paris - 615702. for. See
                       http://woeid.rosselliot.co.nz/lookup/paris


## Test ...

      
        computer:weather cl3m3nt$ python weather.py 615702
        ---------------------------------
        Weather from Yahoo for Paris Ile-de-France, France
        ---------------------------------
        Actually
        ---------------------------------
        Mon 25 Apr 2016
        Temp : 11 C |-| Cloudy
        Temp low : 3 C
        Temp high : 11 C
        ---------------------------------
        Forecast 2 Day
        ---------------------------------
        Tue 26 Apr 2016
        Partly Cloudy
        Temp low : 5 C
        Temp high : 9 C
        ---------------------------------
        Wed 26 Apr 2016
        Partly Cloudy
        Temp low : 3 C
        Temp high : 11 C
        ---------------------------------
