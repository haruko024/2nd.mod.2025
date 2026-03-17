import pandas as pd

data = [
    (1, "Gocotano, Izeah Aerikiel", "DHVD-0021"),
    (2, "Del Castillo, Mark Anthony Jr. M.", "DHVD-0504"),
    (3, "Hular, Jobert L.", "DHVD-0231"),
    (4, "Ballarbare, Nelyn D.", "DHVD-0134"),
    (5, "Borja, Cathlene Pearl D.", "DHVD-0475"),
    (6, "Fuentes, Darelle P.", "DHVD-0065"),
    (7, "Pelias, Althea L.", "DHVD-0229"),
    (8, "Policarpio, Reynante A.", "DHVD-0254"),
]
df = pd.DataFrame(data, columns=["No.", "Fullname", "Permit Number"])

df.to_excel("data.xlsx", index=False)

print("Excel file created!")
