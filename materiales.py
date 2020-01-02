# -*- coding: utf-8 -*-
import json

with open('DATA.json','r') as f:
		datos = f.read()
		print(datos)

objeto = json.loads(datos)
#print(json.dumps(objeto,indent=4))
print(objeto.get(ESTRUCUTRA))

