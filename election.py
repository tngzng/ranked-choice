from typing import List, Tuple
import numpy as np

from pyrankvote import Candidate, Ballot, instant_runoff_voting
from pyrankvote.helpers import ElectionResults


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


def generate_ballot(candidates=List[Candidate], weights=List[float]) -> Ballot:
    # rank up to 5 candidates in order of preference
    # source: https://www1.nyc.gov/site/civicengagement/voting/ranked-choice-voting.page
    votes = 5
    ballot = np.random.choice(candidates, p=weights, replace=False, size=votes)
    return Ballot(ranked_candidates=ballot)


def run_election(candidate_weights: List[Tuple[str, float]]) -> ElectionResults:
    # total votes in 2017 nyc democratic mayoral primary
    # source: https://en.wikipedia.org/wiki/2017_New_York_City_mayoral_election
    voters = 437517

    candidates = [Candidate(p[0]) for p in candidate_weights]
    weights = np.array([p[1] for p in candidate_weights])
    adjusted_weights = weights / weights.sum()

    ballots = [generate_ballot(candidates, adjusted_weights) for v in range(voters)]
    return instant_runoff_voting(candidates, ballots)


def simulate_elections():
    NUM_SIMULATIONS = 10
    results = []
    [results.append(run_election(candidate_weights)) for n in range(NUM_SIMULATIONS)]
    rounds = np.array([len(r.rounds) for r in results])
    winner = np.array([r.get_winners()[0].name for r in results])
    avg_rounds = np.median(rounds)
    winners, frequencies = np.unique(winner, return_counts=True)

    print("============ REPORT ============")
    print("---------- avg rounds ----------")
    print(avg_rounds)
    print("----------- winners ------------")
    for winner, freq in zip(winners, frequencies):
        print(f"{winner}: {freq}/{NUM_SIMULATIONS} wins")


if __name__ == "__main__":
    simulate_elections()
    run_election(candidate_weights)
