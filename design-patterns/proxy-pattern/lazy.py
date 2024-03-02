
class LazyProperty: 
    def __init__(self, method): 
        self.method = method 
        # Get the name of the method (function)
        self.method_name = method.__name__ 
      
    # This method is called when the property is accessed
    def __get__(self, obj, cls): 
        # If the property is accessed on the class (not an instance), return None
        if not obj: 
            return None 
        # Call the method to get the value
        value = self.method(obj) 
        # Cache the value by setting it as an attribute on the object
        setattr(obj, self.method_name, value) 

        return value 


class Test: 
    def __init__(self): 
        self.x = 'foo' 
        self.y = 'bar' 
        self._resource = None
        
    # Use LazyProperty as a decorator for the resource property
    @LazyProperty 
    def resource(self): 
        # This method is lazily evaluated when resource is accessed
        print(f'initializing self._resource which is: {self._resource}')        
        self._resource = tuple(range(5))  # Expensive computation
        return self._resource


def main():     
    t = Test() 

    print(t.x) 
    print(t.y) 

    # Access the lazy property (resource) twice
    print(t.resource) 
    print(t.resource)


if __name__ == '__main__': 
    main()
