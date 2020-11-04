import json


def load():
  f = open('config.json', 'r')

  f = f.read()

  f = json.loads(f)

  return f