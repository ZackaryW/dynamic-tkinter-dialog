from dynTinkDialog import create_window

if __name__ == "__main__":
    create_window(data={
        "test" : ["text","hi"], 
        "test2" : ["file", "C://test.txt"],
        "test3" : ["int", 10]
    })
    
    
    