import requests

# Base URL for the server
base_url = "https://127.0.0.1:5000"

# Test cases for FBS endpoint
fbs_data_0 = {
    "age": 30,
    "gender": 0,
    "polyuria": 0,
    "polydipsia": 0,
    "sudden weight loss": 0,
    "weakness": 0,
    "polyphagia": 0,
    "genital thrush": 0,
    "visual blurring": 0,
    "itching": 0,
    "irritability": 0,
    "delayed healing": 0,
    "partial paresis": 0,
    "muscle stiffness": 0,
    "alopecia": 0,
    "obesity": 0,
    "sugar_level": 80,
}

fbs_data_1 = {
    "age": 50,
    "gender": 1,
    "polyuria": 1,
    "polydipsia": 1,
    "sudden weight loss": 1,
    "weakness": 1,
    "polyphagia": 1,
    "genital thrush": 1,
    "visual blurring": 1,
    "itching": 1,
    "irritability": 1,
    "delayed healing": 1,
    "partial paresis": 1,
    "muscle stiffness": 1,
    "alopecia": 1,
    "obesity": 1,
    "sugar_level": 180,
}

# Test cases for RBS endpoint
rbs_data_0 = {
    "age": 40,
    "gender": 0,
    "polyuria": 0,
    "polydipsia": 0,
    "sudden weight loss": 0,
    "weakness": 0,
    "polyphagia": 0,
    "genital thrush": 0,
    "visual blurring": 0,
    "itching": 0,
    "irritability": 0,
    "delayed healing": 0,
    "partial paresis": 0,
    "muscle stiffness": 0,
    "alopecia": 0,
    "obesity": 0,
    "sugar_level": 120,
}

rbs_data_1 = {
    "age": 60,
    "gender": 1,
    "polyuria": 1,
    "polydipsia": 1,
    "sudden weight loss": 1,
    "weakness": 1,
    "polyphagia": 1,
    "genital thrush": 1,
    "visual blurring": 1,
    "itching": 1,
    "irritability": 1,
    "delayed healing": 1,
    "partial paresis": 1,
    "muscle stiffness": 1,
    "alopecia": 1,
    "obesity": 1,
    "sugar_level": 250,
}

# Test cases for HbA1c endpoint
hba1c_data_0 = {
    "age": 35,
    "gender": 0,
    "polyuria": 0,
    "polydipsia": 0,
    "sudden weight loss": 0,
    "weakness": 0,
    "polyphagia": 0,
    "genital thrush": 0,
    "visual blurring": 0,
    "itching": 0,
    "irritability": 0,
    "delayed healing": 0,
    "partial paresis": 0,
    "muscle stiffness": 0,
    "alopecia": 0,
    "obesity": 0,
    "sugar_level": 50,
}

hba1c_data_1 = {
    "age": 55,
    "gender": 1,
    "polyuria": 1,
    "polydipsia": 1,
    "sudden weight loss": 1,
    "weakness": 1,
    "polyphagia": 1,
    "genital thrush": 1,
    "visual blurring": 1,
    "itching": 1,
    "irritability": 1,
    "delayed healing": 1,
    "partial paresis": 1,
    "muscle stiffness": 1,
    "alopecia": 1,
    "obesity": 1,
    "sugar_level": 90,
}

# Make requests and print results
print("FBS endpoint:")
response_0 = requests.post(f"{base_url}/FBS", json=fbs_data_0)
print(f"Case 0: {response_0.json()}")
response_1 = requests.post(f"{base_url}/FBS", json=fbs_data_1)
print(f"Case 1: {response_1.json()}")

print("\nRBS endpoint:")
response_0 = requests.post(f"{base_url}/RBS", json=rbs_data_0)
print(f"Case 0: {response_0.json()}")
response_1 = requests.post(f"{base_url}/RBS", json=rbs_data_1)
print(f"Case 1: {response_1.json()}")

print("\nHbA1c endpoint:")
response_0 = requests.post(f"{base_url}/HbA1c", json=hba1c_data_0)
print(f"Case 0: {response_0.json()}")
response_1 = requests.post(f"{base_url}/HbA1c", json=hba1c_data_1)
print(f"Case 1: {response_1.json()}")
