# ranked-choice
This is a simple ranked choice election simulation meant to: 1) ballpark the number of elimination rounds in NYC's 2021 mayoral race, and 2) see which of the more popular candidates are likely to be eliminated before the final round of tabulations.

## takeaways
While it may be tempting for progressive voters to list only one or two progressive candidates, this strategy can have the effect of not voting at all.

Democracy Journal warns us about this [very scenario](https://democracyjournal.org/arguments/ranked-choice-voting-is-not-the-solution/):

"Say there are five candidates running, but the voter ranks only three, and all three are eliminated prior to the last round. As a result, none of their votes will have gone to the winning candidate or the runner-up. In effect, their ballot doesn’t figure in the outcome."

Since the results below show a high likelihood that ranked choice ballot tabulations for NYC's competitive 2021 mayoral race will go through five or more rounds of elimination, many progressive ballots with fewer than five selections may be eliminated. 

**The bottom line:** progressive voters should make sure their ballots count by voting for five candidates total (the maximum allowed).

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

## methodology 
The approach to generate ballots for the election simulation is very simplistic. Each ballot selection is randomly chosen using recent polling stats to weight each subsequent selection:

```
ballot = np.random.choice(candidates, p=weights, replace=False, size=VOTES)
```

Since the goal is not to simulate an actual election with high fidelity, but to ballpark the number of ranked choice elimination rounds there might be, this simplistic approach should suffice.

## usage
1. install dependencies
```
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
2. run election simulation
```
python election.py
```

## feedback
If you have feedback or suggestions, please let me know [here](https://forms.gle/HU6fPNUWF7xtpLUV9).
