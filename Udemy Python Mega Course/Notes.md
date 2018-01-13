# Notes

## Data types

### String
print raw string (as is without interpretation)

    print(r'C:\Documents\')
### List
    l = [a,b,c]

### Tuple
    t = (a,b,c)
    
### Dictionary
    d = {"red": 1, "green": 2, "blue": 3}
    
 * red,green,blue - keys
 * 1,2,3 - values     

## Properties
type(variable) - to display variable type
    
    type(cars)
    <class 'tuple'>   

    type(2.4)
    <class 'float'>

dir(type) - to display type properties
    e.g.: dir(tuple)
    
    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']


### Hints 

to reload already loaded module

    from importlib import reload
    importlib.reload(module_name)
 
 to display doc (help) of a module, function, etc.
 
        module_name.__doc__
        module_name.function_name.__doc__
 
 to create doc section
 
      r"""
      that's a text inside __doc__ section
      """
  ## Virtual Env
  
        pip install virtualenv
        mkdir roboapp1
        mv flaskapp1/ roboapp1
        cd roboapp1
        python -m virtualenv virtual
        
        #   ./roboapp1/
                |
                |-/flaskapp1/
                |-/virtual/
        
        ./roboapp1/virtual/bin/pip install flask
        ./roboapp1/virtual/bin/pip install gunicorn
        
        #test if webapp1.py runs from virtual python instance
        ./roboapp1/virtual/bin/python ./roboapp1/flaskapp1/webapp1.py
  
  ## Heroku
        sudo apt-get install snapd
        sudo snap install heroku --classic
        
        # check if heroku is installed
        heroku --version
        
        # login to heroku
        heroku login 
        
        # create heroku application container (Dyno)
        heroku create app_unique_name
        
        #display heroku containers
        heroku apps
        
        # get information about deployed apps
        heroku info
        
        # stop heroku dynos
        heroku ps:scale web=1
  
  #### deploy application to Heroku
  
        ./roboapp1/virtual/bin/pip freeze > ./roboapp1/flaskapp1/requirements.txt
        echo 'web: gunicorn webapp1:app1' > ./roboapp1/flaskapp1/Procfile
        echo 'python-3.6.4.' > ./roboapp1/flaskapp1/runtime.txt
        git init
        git add .
        git commit -m 'message'
        heroku git:remote --app roboapp1
        