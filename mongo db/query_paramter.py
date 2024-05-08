import pymongo
'''
//////////////////////////////////Comparison Operators////////////////////////

   $eq: Values are equal

collection.find({"field": {"$eq": value}})

   $ne: Values are not equal

collection.find({"field": {"$ne": value}})

   $gt: Value is greater than another value

collection.find({"field": {"$gt": value}})

$gte: Value is greater than or equal to another value

collection.find({"field": {"$gte": value}})

$lt: Value is less than another value


collection.find({"field": {"$lt": value}})

$in: Value is matched within an array


collection.find({"field": {"$in": [value1, value2, ...]}})

////////////////////////Logical Operators:///////////

$and: Returns documents where both queries match
collection.find({"$and": [{"field1": value1}, {"field2": value2}]})

$or: Returns documents where either query matches
collection.find({"$or": [{"field1": value1}, {"field2": value2}]})

$nor: Returns documents where both queries fail to match

collection.find({"$nor": [{"field1": value1}, {"field2": value2}]})

Certainly! Here's how you can use these MongoDB update operators in PyMongo:

1. **Fields Operators**:
   - `$currentDate`: Sets the field value to the current date
     ```python
     collection.update_many({}, {"$currentDate": {"lastModified": True}})
     ```

   - `$inc`: Increments the field value
     ```python
     collection.update_many({}, {"$inc": {"quantity": 1}})
     ```

   - `$rename`: Renames the field
     ```python
     collection.update_many({}, {"$rename": {"oldField": "newField"}})
     ```

   - `$set`: Sets the value of a field
     ```python
     collection.update_many({}, {"$set": {"status": "active"}})
     ```

   - `$unset`: Removes the field from the document
     ```python
     collection.update_many({}, {"$unset": {"obsoleteField": ""}})
     ```

2. **Array Operators**:
   - `$addToSet`: Adds distinct elements to an array

        collection.update_many({}, {"$addToSet": {"tags": "newTag"}})

   - `$pop`: Removes the first or last element of an array

        collection.update_many({}, {"$pop": {"comments": -1}})  # Removes the last element

   - `$pull`: Removes all elements from an array that match the query
   
     collection.update_many({}, {"$pull": {"tags": "oldTag"}})

   - `$push`: Adds an element to an array
     collection.update_many({}, {"$push": {"comments": {"$each": ["comment4", "comment5"], "$position": 0}}})

'''