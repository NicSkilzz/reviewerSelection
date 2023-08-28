import requests

base_url = "https://api.openalex.org/works/"

oa_id_list = ["W2741809807", "W1560783210", "W2029057325", "W2160597895"]


def extract_cited_works(oa_id_list):
    refs = [requests.get(base_url + id).json()["referenced_works"] for id in oa_id_list]
    return {i for lists in refs for i in lists}  # list comprehension returning a set


first_layer_refs = extract_cited_works(oa_id_list)
second_layer_ids = [urls.split("/")[-1] for urls in first_layer_refs]
second_layer_refs = extract_cited_works(second_layer_ids)
