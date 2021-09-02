# Hashtables

Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge

## Approach & Efficiency

Time: O(1)
space:O(n)

## API

add: Arguments: key, value Returns: nothing
This method hash the key, and add the key and value pair to the table, handling collisions as needed.
get: Arguments: key, Returns: Value associated with that key in the table

contains: Arguments: key Returns: Boolean, indicating if the key exists in the table already.
hash Arguments: key Returns: Index in the collection for that key.
