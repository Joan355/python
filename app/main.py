import utils

__all__ = ["data", "run"]

keys, values = utils.getPopulation()
data = [{"Country" : k , "Population" : v} for k,v in zip(keys,values)]

def run():
    result = utils.getPopulationByCountry(data,"bolivia")
    print(result)

if __name__ == "__main__":
    run()