from bs4 import BeautifulSoup
import requests

url = "https://www.worldometers.info/coronavirus/"
web = requests.get(url)

Out = BeautifulSoup(web.text, 'html.parser')
data = []

for i in Out.find_all('tr'):
    for j in Out.find_all('td'):
        data.append(j.text)



#print(data)

## start end data
sep = data.index("USA")
end = data.index("Vanuatu")
data1 = data[sep-1:end+16]

#insert
data_iterator = iter(data1)
dataformat = []
while True: 
    try: 
        id_country = next(data_iterator)
        country = next(data_iterator) 
        total_case = next(data_iterator) 
        newcases = next(data_iterator)
        total_d = next(data_iterator) 
        new_d = next(data_iterator) 
        total_recovered = next(data_iterator)  
        active_case = next(data_iterator) 
        serious_critical= next(data_iterator) 
        totcase_1m = next(data_iterator) 
        dead_1m = next(data_iterator) 
        total_test = next(data_iterator) 
        test_1m = next(data_iterator) 
        population = next(data_iterator)
        continent = next(data_iterator)
        a1 = next(data_iterator)
        a2 = next(data_iterator)
        a3 = next(data_iterator)
        a4 = next(data_iterator)

        
        dataformat.append(( 
            id_country,
            country, 
            total_case,
            newcases,
            total_d,
            new_d,
            total_recovered,
            active_case,
            serious_critical,
            totcase_1m,
            dead_1m,
            total_test,
            test_1m,
            population,
            a1,
            a2,
            a3
        )) 
   
    except StopIteration: 
        break
#print(dataformat)
#convert into list of list
dataformat1 = list(map(list,dataformat))
print(dataformat1)
import pandas as pd
col= ['Country','TotalCases','NewCases','TotalDeaths','NewDeaths','TotalRecovered','ActiveCases','Serious_Critical','TotCases1Mpop','TotDeaths1Mpop','totaltest','test1mpop']
df=pd.DataFrame()

Country=[]
TotalCases=[]
NewCases=[]
TotalDeaths=[]
NewDeaths=[]
TotalRecovered=[]
ActiveCases=[]
Serious_Critical=[]
TotCases1Mpop=[]
TotDeaths1Mpop=[]
total_test = []
test_1m = []
#population = []

for i in (dataformat1):
    Country.append(i[1])
    TotalCases.append(i[2].replace(',',''))
    NewCases.append(i[3].replace(',',''))
    TotalDeaths.append(i[4].replace(',',''))
    NewDeaths.append(i[5].replace(',',''))
    TotalRecovered.append(i[6].replace(',',''))
    ActiveCases.append(i[8].replace(',',''))
    Serious_Critical.append(i[9].replace(',',''))
    TotCases1Mpop.append(i[10].replace(',',''))
    TotDeaths1Mpop.append(i[11].replace(',',''))
    total_test.append(i[12].replace(',',''))
    test_1m.append(i[13].replace(',',''))
    #population.append(i[14].replace(',',''))


df=pd.DataFrame(zip(Country,TotalCases,NewCases,TotalDeaths,NewDeaths,TotalRecovered,
                    ActiveCases,Serious_Critical,TotCases1Mpop,TotDeaths1Mpop,total_test,test_1m),columns=col)
print(df)
