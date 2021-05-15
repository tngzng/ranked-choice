from typing import List, Tuple
import numpy as np


candidate_weights = [
    ("andrew yang", 0.21),
    ("eric adams", 0.17),
    ("scott stringer", 0.1),
    ("maya wiley", 0.1),
    ("kathryn garcia", 0.08),
    ("shaun donovan", 0.06),
    ("ray mcguire", 0.06),
    ("dianne morales", 0.04),
]


def generate_choices(candidate_weights: List[Tuple[str, float]]):
    # rank up to 5 candidates in order of preference
    # source: https://www1.nyc.gov/site/civicengagement/voting/ranked-choice-voting.page
    votes = 5
    candidates = [p[0] for p in candidate_weights]
    weights = np.array([p[1] for p in candidate_weights])
    adjusted_weights = weights / weights.sum()
    return np.random.choice(candidates, p=adjusted_weights, replace=False, size=votes)


def run_election():
    # 2.97 million New York City voters cast a ballot in the 2020 general election
    # source: https://www.gothamgazette.com/city/9907-voter-turnout-new-york-city-increased-7-5-percent-2016-to-2020
    # voters = int(2.97 * 1000000)
    voters = 1000
    results = [generate_choices(candidate_weights) for v in range(voters)]
