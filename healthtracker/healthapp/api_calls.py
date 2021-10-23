import requests

url = "https://fitness-api.p.rapidapi.com/fitness"


headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "1028412bafmsh4e76670100a15dep1e2198jsn571d5dd04aef",
    'x-rapidapi-host': "fitness-api.p.rapidapi.com"
}


def getStats(heightInCms, weightInKg, age, gender='male'):
    payload = "height="+str(heightInCms)+"&weight=" + \
        str(weightInKg)+"&age="+str(age)+"&gender="+str(gender)

    response = requests.request(
        "POST", url, data=payload, headers=headers).json()
    # print(response)
    min_range = min(response['idealBodyWeight']['hamwi']['metric']['value'],
                    response['idealBodyWeight']['devine']['metric']['value'],
                    response['idealBodyWeight']['robinson']['metric']['value'],
                    response['idealBodyWeight']['miller']['metric']['value'])-10

    max_range = max(response['idealBodyWeight']['hamwi']['metric']['value'],
                    response['idealBodyWeight']['devine']['metric']['value'],
                    response['idealBodyWeight']['robinson']['metric']['value'],
                    response['idealBodyWeight']['miller']['metric']['value'])

    final_stats = {'height': response['height'],
                   'weight': response['weight'],
                   'age': response['age'],
                   'gender': response['gender'],
                   'BMI': str(response['bodyMassIndex']['value'])+' '+response['bodyMassIndex']['unit'],
                   'conclusion': response['bodyMassIndex']['conclusion'],
                   'idealWeightRange': str(min_range)+" kg - "+str(max_range)+" kg"
                   }
    # print(final_stats)
    return(final_stats)


# print(getStats(heightInCms=813, weightInKg=89, age=21, gender='male'))
