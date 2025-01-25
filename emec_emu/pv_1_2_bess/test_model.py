import pv_1_2

model = pv_1_2.model()

model.ini({},'xy_0.json')

print(f"V_POI = {model.get_value('V_POI'):3.2f} pu")