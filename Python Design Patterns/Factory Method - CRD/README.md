# Factory Method – Python Design Patterns

Factory Method is a `Creational Design Pattern` that allows an interface or a class to create an object, but let subclasses decide which class or object to instantiate. Using the Factory method, we have the best ways to create an object. Here, objects are created without exposing the logic to the client and for creating the new type of the object, the client uses the same common interface.

**Problems we face without Factory Method**:

Imagine you are having your own startup which provides ridesharing in the different parts of the country. The initial version of the app only provides the Two-Wheeler ridesharing but as time passes, your app becomes popular and now you want to add Three and Four-Wheeler ridesharing also.
It’s a piece of great news! but what about the software developers of your startup. They have to change the whole code because now the most part of the code is coupled with the Two-Wheeler class and developers have to make changes into the entire codebase.
After done with all these changes, either the developers end with the messy code or with the resignation letter.

![images][1]

Let’s understand the concept with one more example which is related to the translations and localization of the different languages.
Suppose we have created an app whose main purpose is to translate one language into another and currently our app works with 10 languages only. Now our app has become widely popular among people but the demand has grown suddenly to include 5 more languages.
It’s a piece of great news! only for the owner not for the developers. They have to change the whole code because now the most part of the code is coupled with the existing languages only and that’s why developers have to make changes into the entire codebase which is really a difficult task to do.

**Without Factory Method**:

```py
if __name__ == "__main__": 
  
    # main method to call others 
    f = FrenchLocalizer() 
    e = EnglishLocalizer() 
    s = SpanishLocalizer() 
  
    # list of strings 
    message = ["car", "bike", "cycle"] 
  
    for msg in message: 
        print(f.localize(msg)) 
        print(e.localize(msg)) 
        print(s.localize(msg)) 
```

**With Factory Method**:

```py
def Factory(language ="English"): 
  
    """Factory Method"""
    localizers = { 
        "French": FrenchLocalizer, 
        "English": EnglishLocalizer, 
        "Spanish": SpanishLocalizer, 
    } 
  
    return localizers[language]() 
  
if __name__ == "__main__": 
  
    f = Factory("French") 
    e = Factory("English") 
    s = Factory("Spanish") 
  
    message = ["car", "bike", "cycle"] 
  
    for msg in message: 
        print(f.localize(msg)) 
        print(e.localize(msg)) 
        print(s.localize(msg)) 
```

[1]: https://media.geeksforgeeks.org/wp-content/uploads/20200117094810/localizer2.jpg