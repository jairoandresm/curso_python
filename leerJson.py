# -*- coding: utf-8 -*-

import json

def run():
    with open('DATA.json','r') as f:
        datos = f.read()
    objeto = json.loads(datos)
    print(json.dumps(objeto,indent=4)) #imprime todo el json de forma clara
    #print[objeto[1]["ESTRUCTURA"]] forma de acceder a un elemento

    

    



if __name__ == '__main__':
    run()