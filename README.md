Welcome to the documentation of our wonderful Address Book App!

Since you are here, you must have cloned the repository as of now. Kindly see some of the actions to take below:

1. Starting the project:

   - Navigate to the project directory and open cmd at this path. Make sure that docker is installed on your machine or the VM you are using.
   - Run the command "docker build -t my_address_app ." to build docker image.
   - Run the command "docker run -p 8000:8000 my_address_app" to start the container.
   - At this point, you should be able to access startup page (swagger docs, in this case) at http://localhost:8000/

2. Testing the API:

   - Now, the first page is the swagger document. You should be able to see the API details here.
   - This API offers a number of operations for addresses: List all, list by id, create, delete and update.
   - Open the file, "dummy_data.txt" and copy the given JSON.
   - Using the Swagger editor, paste the request in the Create [POST] and hit execute.
   - Now, you can list all addresses using the 'api/addresses' [GET] request and individual ones using 'api/address/{id}' endpoints.

3. Testing through POSTMAN:

   - If required, a postman collection is included in the repo as well. You can optionally import that and test out using POSTMAN.

Hope you have a good time managing addresses! :)
