import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type",data={"method":"PUT"})

print(response1.request,"\t","text:",response1.text,"\t","status:",response1.status_code,"\n" )
print(response2.request,"\t","text:",response2.text,"\t","status:",response2.status_code,"\n" )
print(response3.request,"\t","text:",response3.text,"\t","status:",response3.status_code,"\n" )

methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]

for param in methods_list:
        result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method GET with parameter params={param} has following result {result} with status code {result.status_code}")
        result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method GET with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method POST with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method POST with parameter params ={param} has following result {result} with status code {result.status_code}")
        result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method PUT with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method PUT with parameter params ={param} has following result {result} with status code {result.status_code}")
        result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"method DELETE with parameter data={param} has following result {result} with status code {result.status_code}")
        result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"method DELETE with parameter params ={param} has following result {result} with status code {result.status_code}")

