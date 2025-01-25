import pv_1_2_bess

model = pv_1_2_bess.model()

model.ini({},'xy_0.json')

print(f"V_POI = {model.get_value('POI'):3.2f} pu")