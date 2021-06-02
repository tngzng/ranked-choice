import operator
from typing import List, Tuple

import numpy as np
from pyrankvote import Candidate, Ballot, instant_runoff_voting
from pyrankvote.helpers import ElectionResults, CandidateStatus
from progressbar import progressbar


SIMULATIONS = 100
VOTERS = 1000
# rank up to 5 candidates in order of preference
# source: https://www1.nyc.gov/site/civicengagement/voting/ranked-choice-voting.page
VOTES = 5
# source: https://emersonpolling.reportablenews.com/pr/garcia-surges-to-lead-in-nyc-mayor-race-while-adams-holds-his-base
CANDIDATE_WEIGHTS = [
    ("kathryn garcia", 0.21),
    ("eric adams", 0.2),
    ("andrew yang", 0.16),
    ("scott stringer", 0.1),
    ("maya wiley", 0.09),
    ("dianne morales", 0.07),
    ("shaun donovan", 0.05),
    ("ray mcguire", 0.02),
]


def generate_ballot(candidates=List[Candidate], weights=List[float]) -> Ballot:
    ballot = np.random.choice(candidates, p=weights, replace=False, size=VOTES)
    return Ballot(ranked_candidates=ballot)


def run_election(candidate_weights: List[Tuple[str, float]]) -> ElectionResults:
    candidates = [Candidate(p[0]) for p in candidate_weights]
    weights = np.array([p[1] for p in candidate_weights])
    adjusted_weights = weights / weights.sum()

    ballots = [generate_ballot(candidates, adjusted_weights) for v in range(VOTERS)]
    results = instant_runoff_voting(candidates, ballots)
    return results


def get_eliminated(results: ElectionResults) -> List[Candidate]:
    """
    get list of candidates eliminated in the round that corresponds with the
    number of choices each voter gets.

    for example, if voters get to select five candidates, return the candidates who
    have been eliminated by the fifth round.

    this attempts to identify which ballots may lead to the following scenario:
    "Say there are five candidates running, but the voter ranks only three, and all three are eliminated prior to the last round. As a result, none of their votes will have gone to the winning candidate or the runner-up. In effect, their ballot doesn’t figure in the outcome."

    source: https://democracyjournal.org/arguments/ranked-choice-voting-is-not-the-solution/
    """
    try:
        _round = results.rounds[VOTES - 1]
    except IndexError:
        # the election was decided before the number of votes were exhausted
        return []
    eliminated_candidates = [
        candidate_result.candidate
        for candidate_result in _round.candidate_results
        if candidate_result.status == CandidateStatus.Rejected
    ]
    return [c.name for c in eliminated_candidates]


def simulate_elections():
    results = []
    [
        results.append(run_election(CANDIDATE_WEIGHTS))
        for n in progressbar(range(SIMULATIONS))
    ]
    rounds = np.array([len(r.rounds) for r in results])
    avg_rounds = np.median(rounds)

    eliminated = []
    [eliminated.extend(get_eliminated(r)) for r in results]
    eliminated = np.array(eliminated)
    eliminated, counts = np.unique(eliminated, return_counts=True)
    eliminated_counts = zip(eliminated, counts)
    eliminated_counts = sorted(
        eliminated_counts, key=operator.itemgetter(1), reverse=True
    )

    print("=================== REPORT ===================")
    print("------------------ avg rounds ----------------")
    print(f"candidate selected after {avg_rounds} rounds on average")
    print("--------------- num simulations --------------")
    print(SIMULATIONS)
    print("------------------ num voters ----------------")
    print(VOTERS)
    print(f"------------- eliminated by round {VOTES} ----------")
    for candidate, count in eliminated_counts:
        print(f"{candidate}: {count}/{SIMULATIONS} times")


if __name__ == "__main__":
    simulate_elections()
