import json
import pickle

product = {
    "id":1,
    "name":"p1",
}

json_text = json.dumps(product,indent=2)
restored_product = json.loads(json_text)

with open('product.json','w',encoding="utf-8") as f:
    json.dump(product,f,indent=2)

with open('product.json','r',encoding='utf-8') as f:
    loaded_p = json.load(f)
print(loaded_p)

data = pickle.dumps(product)
print(data)
restored_pkl_p = pickle.loads(data)
print(restored_pkl_p)

with open('product.pkl','wb') as f:
    pickle.dump(product,f)

with open('product.pkl','rb') as f:
    loaded_product_pkl = pickle.load(f)
print(loaded_product_pkl)

