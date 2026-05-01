def response_messages(**kwargs):
    response_dict = {}
    for key, value in kwargs.items():
        response_dict[key] = value

    return response_dict

response = response_messages(name="Alice", age=30, city="New York")
print(response)