import pickle as pkl

picklefile = open("../data/raw_payloads/search_results.pkl", "rb")
results = pkl.load(picklefile)

for result in results:
    print(result)
