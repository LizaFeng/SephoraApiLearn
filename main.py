import requests
import json


############# endpoints categories/v2/list-root
# url = "https://sephora.p.rapidapi.com/categories/v2/list-root"

# headers = {
# 	"x-rapidapi-key": "3a76ca0863msh1d8daf4bb187140p1e8cb5jsnc9be8101eb64",
# 	"x-rapidapi-host": "sephora.p.rapidapi.com"
# }
#############

# ############# endpoints categories/list
# url = "https://sephora.p.rapidapi.com/categories/list"

# querystring = {"categoryId":"cat160006"}

# headers = {
# 	"x-rapidapi-key": "3a76ca0863msh1d8daf4bb187140p1e8cb5jsnc9be8101eb64",
# 	"x-rapidapi-host": "sephora.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# ############

############## to populate the Fragrances.json file
url = "https://sephora.p.rapidapi.com/us/products/v2/list"

querystring = {"pageSize":"60","currentPage":"1","categoryId":"cat1230039"}

headers = {
	"x-rapidapi-key": "3a76ca0863msh1d8daf4bb187140p1e8cb5jsnc9be8101eb64",
	"x-rapidapi-host": "sephora.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

#########


# #########To print out just the keys of the response ##########
# def extract_keys(data, parent_key="root"):
#     """ Recursively extract all keys and maintain parent-child relationships. """
#     keys_structure = {}

#     if isinstance(data, dict):
#         for key, value in data.items():
#             keys_structure[key] = extract_keys(value, key)
#     elif isinstance(data, list) and len(data) > 0:
#         keys_structure[parent_key] = extract_keys(data[0], parent_key)  # Assume first item structure

#     return keys_structure
# #########


# Assuming `response` is your API response
data = response.json()

# # Get the structured keys
# keys_hierarchy = extract_keys(data)

# # Pretty-print the keys as JSON
# # print(json.dumps(keys_hierarchy["categories"], indent=4))


# # print(json.dumps(data, indent=4))
# # # Write the data to a file
with open('Fragrances.json', 'w') as file:
    json.dump(data, file, indent=4)

