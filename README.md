# File-Based-System-perfom-CRD-Operations

This is a File based System which store key-value data that supports the basic operations like  CRD(create, read, write). 
Data store in the local storage for one single process or single laptop.

The data store will support the following :

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object - capped at 
16KB.
3. If Create is invoked for an existing key, an appropriate error must be returned.
4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.
5. A Delete operation can be performed by providing the key.
6. Every key supports setting a Time-To-Live property when it is created. This property isoptional. If provided, it will be evaluated as an integer defining the number of seconds 
the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.
7. The file is accessed by multi-threading
8. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.
9. The size of file storing data must never exceeds 1GB.

# Please go through the main.py and performed.py file and for given input and there output of main and performed pdf file that are attached to understand the working of code and how to perform the operation in more better and clear way. 
