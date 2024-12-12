import yaml

with open("data/data.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print(f"Number of classes: {len(data['names'])}")