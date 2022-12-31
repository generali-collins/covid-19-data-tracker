import requests

response = requests.get("https://coronavirus-19-api.herokuapp.com/countries")
# print(response.json())

data = []
for num in range(len(response.json())):
    datas = list(response.json()[num].items())[1:]
    data.append(datas)
    #print(datas)
#print(data)

countries = []
data_dict = {}
for num in range(len(response.json())):
    country_name = (list(response.json()[num].values())[0]).lower()
    data_dict[country_name] = list(response.json()[num].items())[1:]

    countries.append(country_name.lower())
    # print(data_dict)
# print(countries)

dictionary = {key: value for key, value in zip(countries, data)}
# print("%s: %s" % (data_dict[country_lower][i][0], data_dict[country_lower][i][1]))



class CovidData:
    def __init__(self, country):
        self.country = country.lower()
        self.country_name = self.country.capitalize()
        self.total_cases = data_dict[self.country][0][1]
        self.cases_today = data_dict[self.country][1][1]
        self.deaths = data_dict[self.country][2][1]
        self.recovered = data_dict[self.country][4][1]

    def get_country_name(self):
        return self.country_name

    def get_cases(self):
        return self.total_cases

    def get_cases_today(self):
        return self.cases_today

    def get_deaths(self):
        return self.deaths

    def get_recovered(self):
        return self.recovered
