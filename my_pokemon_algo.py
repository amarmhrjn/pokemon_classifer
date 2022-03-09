import requests
import json
import my_data_processor
from sklearn.linear_model import LogisticRegression

logreg_clf = None

# train model (multi-class classifier)
def train():
    
    # source url for training
    src_url = "https://pokeapi.co/api/v2/pokemon/"

    # get json data
    data = requests.get(src_url)
    jdata = json.loads(data.text)

    # get results
    results = jdata['results']

    # prepare training table
    train_table = []
    labels = []

    for r in results:
        print(r)

        url = r['url']
        rdata = requests.get(url)

        # load json data
        res_data = json.loads(rdata.text)

        # collect attributes for single row
        # number of tems for each items/properties are taken as the attributes
        row_attribute = my_data_processor.process(res_data)
        
        # add into the training table
        train_table.append(row_attribute)

        # collect the label for the current row
        t = res_data["types"][0]
        lab = t["type"]["name"]
        labels.append(lab)
    
    # train the model
    #print(len(train_table))

    # use logistic regression for multi-class classifier
    if logreg_clf is None:
        logreg_clf = LogisticRegression()
        logreg_clf.fit(train_table, labels)

# pokemon type predictor
def predict(pokemon):
    # predict the class
    return logreg_clf.predict(pokemon)