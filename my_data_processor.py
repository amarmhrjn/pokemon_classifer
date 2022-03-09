import json

# process the results to get the attributes
def process(rdata):
    #print("process")

    res_data = json.loads(rdata.text)
    num_attributes = len(res_data)

    # collect attributes for single row
    row_attribute = []
    for a in range(num_attributes):
        count = len(res_data)
        row_attribute.append(count)

    return row_attribute