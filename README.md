# Garden watering script

Just a dead simple script to check if it has rained in my city over the last 2 two days. And if not remind me to water the garden

## How run the script
First of all clone this project:
````git
git clone https://github.com/jbakchr/garden-watering-script.git
````

Following this there's these 2 ways to run this project:
1. Local Python interpreter
2. Docker

### Local Python interpreter
Run this script from the command line by typing:

```python
python app.py
```

### Docker
Build an image first:
```docker
docker build -t <username/image_name:tag_name> .
```

Then run that image:
```docker
docker run <image_name>
```
