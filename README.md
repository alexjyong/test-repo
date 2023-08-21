# Easy Mongo experimentation set up

(stolen from ChatGPT and modified)

When running the MongoDB container, it's essential to map a local directory on your host machine to the data directory inside the container. This ensures that your MongoDB data persists even if the container is removed or restarted.

Here's the revised step with the volume mapping:

### Setting Up MongoDB with Docker:

1. **Pull the MongoDB Docker Image**:
   ```bash
   docker pull mongo:latest
   ```

2. **Run MongoDB in a Docker Container with Volume Mapping**:
   ```bash
   docker run --name mongodb-container -d -p 27017:27017 -v /path/to/gitcheckout/mongoData:/data/db mongo:latest
   ```
   Here, `/path/to/gitcheckout/mongoData` is a directory on your host machine where you want to store the MongoDB data. This directory will be mapped to `/data/db` inside the container, which is the default data directory for MongoDB.

3. **Access the MongoDB Shell**:
   ```bash
   docker exec -it mongodb-container mongosh
   ```

4. **Enable Authentication** (Optional but recommended):
   - First, access the MongoDB shell inside the container:
     ```bash
     docker exec -it mongodb-container mongosh
     ```
   - In the MongoDB shell, create an admin user:
     ```javascript
     use admin
     db.createUser({ user: 'admin', pwd: 'yourpassword', roles: [{ role: 'userAdminAnyDatabase', db: 'admin' }] })
     ```
   - Restart the MongoDB container with authentication enabled:
     ```bash
     docker stop mongodb-container
     docker start mongodb-container
     ```

### Connecting to MongoDB from a Python Script:

1. **Install the MongoDB Python Driver**:
   ```bash
   pip install pymongo
   ```

2. **Python Script to Connect to MongoDB**:
   ```python
   from pymongo import MongoClient

   # Connect to MongoDB running in Docker container
   client = MongoClient('mongodb://admin:yourpassword@localhost:27017/')

   # List all databases
   print(client.list_database_names())
   ```

3. **Run the Python Script**:
   ```bash
   python your_script_name.py
   ```

With the volume mapping in place, your MongoDB data will be stored on your host machine, ensuring data persistence.


The scripts `test.py` and `crudtest.py` demostrate fetching database names and CRUD commands with MongoDB respectively.

After installing `pymongo` with `pip install pymongo`, run them with `python test.py` and `python crudtest.py`
