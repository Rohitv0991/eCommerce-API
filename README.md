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
Inorder to create a new object we have to first set input parameters. Kindly make sure that your request includes all the keys.
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

