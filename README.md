# eCommerce-API
This is a **RESTful API** written in **Python** using the **Flask** web framework, which allows the user to do basic **CRUD** operations on the data that is the user can Create new objects, Read the data, Update or Delete the objects in the database hosted on **MongoDB Atlas**.

## Get Started ##

### Installation ###
Firstly you must have **Docker** installed on your computer. You can download Docker from [here](https://www.docker.com/101-tutorialclone). Then clone this repository in a new folder.
Now we have to create a **Docker image**. To do so open terminal and go to the newly created folder where you have cloned this repository and run the following command:
```
docker build -t flaskapp
```
Kindly note that instead of 'flaskapp' you can give any name tag of your choice.

### Running the container ###
Once the docker image is ready it is time to start and run an image instance. A running instance of an image is called as container.
To do so enter the following command in the terminal:
```
docker run -ti -p 5000:5000 flaskapp
```
Kindly note that ``` -ti ``` is for interactive terminal mode and ```-p 5000:5000``` will map the port 5000 of the docker container with port 5000 of the host system.

Now our API sould be running on the localhost and listening on port 5000.

## Usage ##

This API allows the user to interact with the data of ***5000 eCommerce products*** stored on the **MongoDB Atlas**. The user can perform **CRUD** operations on the remote database. We will be discussing usage of each operation one by one.
This examples are of running the service locally (localhost), using port 5000.

### 1. Creating new objects ###
Inorder to create a new object we have to first ```import requests``` module. Then set input parameters. Kindly make sure that your request includes all the keys.
```python

# input JSON parameters

params = {
    "name":"Sample Product",
    "brand_name":"Sample Brand",
    "regular_price_value":500,
    "offer_price_value":450,
    "currency":"GBP",
    "classification_l1":"Class 1",
    "classification_l2":"Class 2",
    "classification_l3":"",
    "classification_l4":"",
    "image_url":"https://domain.com/in/image/sample/12345?"
}
```
Now we will send a POST request with the **JSON** parameters to our API
```python

import requests

api_result = requests.post(url='http://127.0.0.1:5000/create', json=params)
api_response = api_result.json()
print(api_response)
```
Then our API will send us a **response**, it will look like this:
```python
{
    'message': 'Product added successfully with ID: 5f87f0f754fb750b274d6214', 
    'status': 201
}
```
Now we know that the product has been added to the database and our database has given it an ID: ```5f87f0f754fb750b274d6214```.
We will use this ID in the following examples.

### 2. Updating Objects ###
So we created an object successfully but what if we want to change its 'name' from 'Sample Product' to 'Sample Product Updated' and 
update the 'offer_price_value' from 450 to 400. Like we did in previous example we will first set the updated parameters
```python
# updated parameters

params = {
    "name":"Sample Product Updated",
    "brand_name":"Sample Brand",
    "regular_price_value":500,
    "offer_price_value":400,
    "currency":"GBP",
    "classification_l1":"Class 1",
    "classification_l2":"Class 2",
    "classification_l3":"",
    "classification_l4":"",
    "image_url":"https://domain.com/in/image/sample/12345?"
}
```
Now we have to send a PUT request to our API to update the product with ID: ```5f87f0f754fb750b274d6214```.
```python
import requests

api_result = requests.put(url='http://127.0.0.1:5000/update/5f87f0f754fb750b274d6214', json=params)
api_response = api_result.json()
print(api_response)
```
Then our API will send us a **response**, it will look like this:
```python
{
    'message': 'Product with ID: 5f87f0f754fb750b274d6214 is successfully updated.', 
    'status': 200
}
```

### 3. Reading Objects ###
To read the objects we will be sending a GET request to the API. The URL for GET request looks like this:
```
http://127.0.0.1:5000/read/<column>/<value>
```
In this API there are a number of ways using ehich a user can read the objects in the database, we will be discussing all of them one by one.
#### a. View a Specific Product ####
To do this we have to search for the specific product using its ID.
```python
import requests

api_result = requests.get(url='http://127.0.0.1:5000/read/_id/5f87f0f754fb750b274d6214')
api_response = api_result.json()
print(api_response)
```
Kindly note that in place of <column> and <value> we have to write '_id' and '5f87f0f754fb750b274d6214' respectively. Then API will search in database for product with given ID and will return a ```List``` of ```JSON``` objects but it will only contain a single object in this case as every ID is unique, response will look like this:
    
```python
[
    {
    '_id': '5f87f0f754fb750b274d6214', 
    'name': 'Sample Product Updated', 
    'brand_name': 'Sample Brand', 
    'regular_price_value': 500, 
    'offer_price_value': 400, 
    'currency': 'GBP', 
    'classification_l1': 'Class 1', 
    'classification_l2': 'Class 2', 
    'classification_l3': '', 
    'classification_l4': '', 
    'image_url': 'https://domain.com/in/image/sample/12345?'
    }
]
```
As you can see this is the product which we first created and then updated.
    
#### b. Search for Products ####
User can also search in the database with other values as well, like if a user wants to see all products with "classification_l2" containing value as "women's knitwear".
To do so we will write "classification_l2" and "women's knitwear" in place of <column> and <value> respectively.
    
```python
import requests

api_result = requests.get(url="http://127.0.0.1:5000/read/classification_l2/women's knitwear")
api_response = api_result.json()
print(api_response)
```

In the response we will receive a ```List``` of ```JSON``` objects which will look lke this:

```python
[
    {'_id': '5f8076080f260a0dd453f370', 'name': 'John Lewis & Partners Relaxed V-Neck Cashmere Sweater', 'brand_name': 'john lewis & partners', 'regular_price_value': 99.0, 'offer_price_value': 99.0, 'currency': 'GBP', 'classification_l1': 'women', 'classification_l2': "women's knitwear", 'classification_l3': '', 'classification_l4': '', 'image_url': 'https://johnlewis.scene7.com/is/image/JohnLewis/004193458?'}, 
    {'_id': '5f8076080f260a0dd453f399', 'name': 'Reiss Turner Colour Block Jumper, Blue', 'brand_name': 'reiss', 'regular_price_value': 115.0, 'offer_price_value': 80.0, 'currency': 'GBP', 'classification_l1': 'women', 'classification_l2': "women's knitwear", 'classification_l3': '', 'classification_l4': '', 'image_url': 'https://johnlewis.scene7.com/is/image/JohnLewis/004235447?'},
    {'_id': '5f8076080f260a0dd453f39a', 'name': 'Warehouse Stitch Diamante Embellished Jumper, Black', 'brand_name': 'warehouse', 'regular_price_value': 46.0, 'offer_price_value': 20.0, 'currency': 'GBP', 'classification_l1': 'women', 'classification_l2': "women's knitwear", 'classification_l3': '', 'classification_l4': '', 'image_url': 'https://johnlewis.scene7.com/is/image/JohnLewis/004795694?'},
    ....
    ....
```

#### c. View all Products ####
If a user want to see all the products stored in the database, the user has to write 'none' and 'none' in place of <column> and <value>. 'none' tells the API that no filters should be applied and show all the data. It should look like this:
    
```python
import requests

api_result = requests.get(url='http://127.0.0.1:5000/read/none/none')
api_response = api_result.json()
print(api_response)
```

In the response we will receive a ```List``` of ```JSON``` objects which will look like this:

```python
[
    {'_id': '5f8076080f260a0dd4540584', 'name': 'French Terry Sweatshirt', 'brand_name': '', 'regular_price_value': 69.0, 'offer_price_value': 35.0, 'currency': 'GBP', 'classification_l1': 'women', 'classification_l2': "women's shirts & tops", 'classification_l3': '', 'classification_l4': '', 'image_url': 'https://lp.arket.com/app006prod?set=source[01_0765893_001_4],type[ECOMLOOK],device[hdpi],quality[80],ImageVersion[201908202327]&call=url[file:/product/style]'}, 
    {'_id': '5f8076080f260a0dd4540585', 'name': 'Cotton Cashmere Beanie', 'brand_name': '', 'regular_price_value': 18.0, 'offer_price_value': 9.0, 'currency': 'GBP', 'classification_l1': 'men', 'classification_l2': "men's accessories", 'classification_l3': "men's hats, gloves & scarves", 'classification_l4': '', 'image_url': 'https://lp.arket.com/app006prod?set=source[02_0668567_003_1],type[PRODUCT],device[hdpi],quality[80],ImageVersion[201908231104]&call=url[file:/product/style]'}, 
    {'_id': '5f8076080f260a0dd4540586', 'name': 'Half-Zip Merino Bib', 'brand_name': '', 'regular_price_value': 99.0, 'offer_price_value': 99.0, 'currency': 'GBP', 'classification_l1': 'baby & child', 'classification_l2': 'feeding & healthcare', 'classification_l3': 'bibs', 'classification_l4': '', 'image_url': 'https://lp.arket.com/app006prod?set=source[01_0808761_001_2],type[ECOMLOOK],device[hdpi],quality[80],ImageVersion[201908231525]&call=url[file:/product/style]'},
    ....
    ....
```
### 4. Deleting an Object ###
Inorder to delete a product the user must provide ID of that project. The user needs to send a DELETE request to the API. The request should look like this:

```python
import requests

api_result = requests.delete(url='http://127.0.0.1:5000/delete/5f87f0f754fb750b274d6214')
api_response = api_result.json()
print(api_response)
```

Then our API will send us a **response**, it will look like this:

```python
{
    'message': 'Product with ID: 5f87f0f754fb750b274d6214 is successfully deleted.', 
    'status': 200
}
```
