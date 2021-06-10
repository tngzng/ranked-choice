# ranked-choice

## usage
1. install dependencies
```
install python dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
2. run election simulation
```
python election.py
```

## results
With polling from [May 23, 2021](https://emersonpolling.reportablenews.com/pr/garcia-surges-to-lead-in-nyc-mayor-race-while-adams-holds-his-base):

```
=================== REPORT ===================
------------------ avg rounds ----------------
candidate selected after 6.0 rounds on average
--------------- num simulations --------------
100
------------------ num voters ----------------
1000
------------- eliminated by round 5 ----------
dianne morales: 100/100 times
maya wiley: 100/100 times
ray mcguire: 100/100 times
scott stringer: 100/100 times
shaun donovan: 100/100 times
andrew yang: 53/100 times
eric adams: 2/100 times
kathryn garcia: 1/100 times
```

With polling from [May 12, 2021](https://www.nydailynews.com/news/politics/nyc-elections-2021/ny-nyc-mayoral-race-poll-latest-20210513-o6g7vjptdfgwzelttmin5t6qla-story.html):
```
=================== REPORT ===================
------------------ avg rounds ----------------
candidate selected after 7.0 rounds on average
--------------- num simulations --------------
100
------------------ num voters ----------------
1000
------------- eliminated by round 5 ----------
dianne morales: 100/100 times
kathryn garcia: 100/100 times
ray mcguire: 100/100 times
shaun donovan: 100/100 times
maya wiley: 52/100 times
scott stringer: 51/100 times
```