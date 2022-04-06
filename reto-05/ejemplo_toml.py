#!/usr/bin/env python
# -*- coding: utf-8 -*-

import toml

#toml.load('ejemplo.toml')
#print(toml.load('ejemplo.toml'))
valores = toml.load('ejemplo.toml')
print(f"Contenido del fichero config = {valores}")
#print(valores['Directorios'])
#print("las claves son:")
#print(valores.keys())
print("los items son:")
print(valores.items())
#print("sacamos valores, espero")
#sustancia = valores['Directorios']
#print(f"sustancia = {sustancia}")
#sustancia2 = sustancia['1']
#print(f"sustancia2 = {sustancia2}")
## Nos vamos a basar en esta rama: 
print("vamos a imprimir directamente el contenido toml.load('ejemplo.toml')['Directorios']")
contenido = toml.load('ejemplo.toml')['Directorios']
print(contenido)
print(f"la longitud de keys es {len(contenido)}")
print('Los items de contenido son: ')
print(contenido.items())
