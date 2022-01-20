# Shalean API

## Request & Response

### Stats
#### GET /api/stat/
  
Get overall site statistics for uploaded files and comments.

```c++
curl -G "http://localhost:8000/api/stat/"
```
     
Response body:

```json
{
  "Total_Images" : 3,
  "Total_Unique_Images" : 3,
  "Total_Size_Mb" : 0.2984,
  "Total_Descriptons" : 3,
  "Total_Unique_Descriptons" : 2
}
```

## Images

### Upload Image
#### POST /api/create_image/
  
Upload new image to server

```c++
curl "http://localhost:8000/api/create_image/" -d "image=@/home/user1/Desktop/test.jpg"
```
     
Response body:

```json
{
  "id" : 13,
  "image" : "http://127.0.0.1:8000/m/site_media/test.jpg"
}
```
    
### Change Image
#### PUT /api/update_image/ID
  
Change a single image using the ID

```c++
curl -X PUT "http://localhost:8000/api/update_image/13" -d "image=@/home/user1/Desktop/test2.jpg"
```
     
`Where 13 is image ID`
  
Response body:

```json
{
  "id" : 13,
  "image" : "http://127.0.0.1:8000/m/site_media/test2.jpg"
}
```
        
### Read Image
#### GET /api/retrieve_image/ID
  
Get a single image using the ID

```c++
curl -G "http://localhost:8000/api/retrieve_image/13"
```
     
`Where 13 is image ID`
  
Response body:

```json
{
  "id" : 13,
  "image" : "http://127.0.0.1:8000/m/site_media/test2.jpg"
}
```
    
### Delete Image
#### DELETE /api/delete_image/ID
  
Delete a single image using the ID

```c++
curl -X DELETE "http://localhost:8000/api/delete_image/13"
```
     
`Where 13 is image ID`
  
Response body:

    {
    }
    
## Descriptions

### Create Description
#### POST /api/create_description/
  
Create new description for a standalone image

```c++
curl "http://localhost:8000/api/create_description/" -d "description=sueta&image=1"
```
     
Response body:

```json
{
  "id" : 5,
  "description" : "sueta",
  "image" : "1"
}
```
    
### Change Description
#### PUT /api/update_description/ID
  
Change a single description using the ID

```c++
curl -X PUT "http://localhost:8000/api/update_description/1" -d "description=new"  
```

`Where 1 is description ID`
  
Response body:

```json
{
  "id" : 1,
  "description" : "new",
  "image" : 1
}
```
        
### Read Description
#### GET /api/retrieve_description/ID
  
Get a single description using the ID

```c++
curl -G "http://localhost:8000/api/retrieve_description/1"
```

`Where 1 is description ID`
  
Response body:

```json
{
  "id" : 1,
  "description" : "safwa",
  "image" : 1
}
```
    
### Delete Description
#### DELETE /api/delete_description/ID
  
Delete a single description using the ID

```c++
curl -X DELETE "http://localhost:8000/api/delete_description/1"
```

`Where 1 is description ID`
  
Response body:

    {
    }
    
* 200 - OK
* 201 - Created
* 204 - No content
* 400 - Bad Request
