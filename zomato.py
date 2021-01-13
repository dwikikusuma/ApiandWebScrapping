############### XOMATO
# key = 2c68df63207ef3a2d51d84607c22d23f


#######
import requests
resto = "/restaurant" # alamat,rating,review,telephone,cuisine,city,
cat = "/categories"
esta = "/establishmentsGet"
cuisines = "/cuisines"


#url = host + cat

# data = requests.get(url, headers = head)
# output = data.json() 
#print(output)


key = "2c68df63207ef3a2d51d84607c22d23f"
host = "https://developers.zomato.com/api/v2.1"
head = {"user-key" : key}

print("==== Zomato ====")
print("1. cari resto")
print("2. lihat daily menu")
choose = (input(">> "))



if choose.isalpha():
    print("invalid input")

elif float(choose) < 1:
    print("invalid input")
elif float(choose) > 2:
    print("invalid input")
# # CARI RESTO
elif int(choose) == 1:
    nama = input("city: ")
    if nama.isdigit():
        print("invalid format")
    else:
        name = nama.replace(" ","%20")
        display = (input("display restaurant: "))

        if display.isalpha():
            print("must be integer")
        else:
        #print(name)

            loc = "/locations?query="
            url = host + loc + name
            data = requests.get(url, headers = head)
            output = data.json() 


            #location
            try:
                entity_id = output['location_suggestions'][0]['entity_id']
                entity_type = output['location_suggestions'][0]['entity_type']

                # print("entity")
                # print(output)
                # print(f"id: {entity_id}")
                # print(f"type: {entity_type}")

                # search
                # url = https://developers.zomato.com/api/v2.1/search?entity_id=80107&entity_type=subzone
                search = f"/search?entity_id={entity_id}&entity_type={entity_type}"
                url = host + search
                data = requests.get(url, headers = head)
                output = data.json()

                # # #review
                # # #url = 



                print("search")

                for i in range(int(display)):
                    print("="*30)
                    print(f"Name: {output['restaurants'][i]['restaurant']['name']}")
                    print(f"Establishment: {output['restaurants'][i]['restaurant']['establishment'][0]}")
                    print(f"Cuisines: {output['restaurants'][i]['restaurant']['cuisines']}")
                    print(f"Address: {output['restaurants'][i]['restaurant']['location']['address']}")
                    print(f"Phone: {output['restaurants'][i]['restaurant']['phone_numbers']}")
                    print(f"Rating: {output['restaurants'][i]['restaurant']['user_rating']['aggregate_rating']}")
                    #print(output['restaurants'][i]['restaurant']['all_reviews'])
                    print("="*30)
                
            except:
                print("city not found")


elif int(choose) == 2:
    ## MENU HARIAN
    nama = input("city: ")
    name = nama.replace(" ","%20")
    resto = input("restaurants : ")
    display = int(input("display menu : "))
    # #print(name)

    loc = "/locations?query="
    url = host + loc + name
    data = requests.get(url, headers = head)
    output = data.json() 


    #location
    entity_id = output['location_suggestions'][0]['entity_id']
    entity_type = output['location_suggestions'][0]['entity_type']
    # print(entity_id)
    # print(entity_type)


    # search
    #surl = https://developers.zomato.com/api/v2.1/search?entity_id=80107&entity_type=subzone
    search = f"/search?entity_id={entity_id}&entity_type={entity_type}&q={resto}"
    url = host + search
    data = requests.get(url, headers = head)
    output = data.json()
    #print(output)   
    print(f"Name: {output['restaurants'][0]['restaurant']['name']}")
    print(f"id: {output['restaurants'][0]['restaurant']['R']['res_id']}")

    # #       DAILY MENU
    # # url = https://developers.zomato.com/api/v2.1/dailymenu?res_id=18484464

    id_resto = output['restaurants'][0]['restaurant']['R']['res_id']
    #print(id_resto)
    daily_menu = f"/dailymenu?res_id={id_resto}"
    url_daily = host + daily_menu
    data_daily = requests.get(url_daily, headers = head)
    output_daily = data_daily.json()
    print(output_daily)

    # print(output)
