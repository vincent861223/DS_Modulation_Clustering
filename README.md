# Genetic Algorithm

## Installation
* Create new virtual environment
```
virtualenv venv
```

* Activate virtual environment
```
. venv/bin/activate
```

* Install packages
```
pip install -r requirements.txt
```



## Usage
* Run Genetic Algorithm
```
python3 start.py --project mockito --maxGen 100
python3 start.py --project java_websocket --maxGen 1000
```

* Visualize original package
```
python3 visualization.py --project mockito --type org 
python3 visualization.py --project java_websocket --type org 
```
* Visualize GA package clustering
```
python3 visualization.py --project mockito --type ga 
python3 visualization.py --project java_websocket --type ga 
```