from src.extract import Extract
from src.load import Load

extract = Extract()
pnadc = extract.extract_pnadc()

load = Load()
load.load_json("Bahia", pnadc)
print(pnadc)