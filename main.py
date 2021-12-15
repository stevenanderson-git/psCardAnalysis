from handanalysis import championship_hands
from metagameanalysis import binomial_analysis, create_from_csv as tourndata, export_to_csv, geometric_analysis


if __name__ == "__main__":
    # tournament rounds
    rounds = 12
    # wins needed for money
    record = 10
    tournament_records = tourndata('standard_breakdown.csv')

    binomial_analysis(tournament_records, rounds, record)
    rnd = 3
    geometric_analysis(tournament_records, rnd)

    tourn, deckdata, table = championship_hands()
    export_to_csv('hypergeometricoutput.csv', table)
    
