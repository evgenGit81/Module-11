# -*- coding: utf-8 -*-
import numpy
import urllib3
import requests
from pprint import pprint
import inspect


def introspection_info(obj):
    result = {}
    frst = {'classmethod': classmethod(obj)}
    scnd = {'type': type(obj)}
    thd = {'dir': dir(obj)}
    fth = {'hasattr': hasattr(obj, 'angle')}
    sx = {'module': inspect.getmodule(obj)}
    svn = {'classes': inspect.getmembers(obj, inspect.isclass)}
    edth = {'functions': inspect.getmembers(obj, inspect.isfunction)}
    elv = {'Methods': inspect.getmembers(obj, inspect.ismethod)}
    for_res = [frst, scnd, thd, fth, sx, svn, edth, elv]
     for i in range(len(for_res)):
        result.update(for_res[i])
    return result

if __name__ == '__main__':
    what_a_obj = ''
    ch = ['1', '2', '3', '4', '5']
    while what_a_obj != 'stop':
        what_a_obj = input("Введите цифру объекта который хотите рассмотреть - 1 - numpy, "
                           "2 - urllib3, 3 - requests, 4 - pprint, 5 - inspect: ")
        if what_a_obj == '1':
            obj = numpy
            pprint(introspection_info(obj))
        elif what_a_obj == '2':
            obj = urllib3
            pprint(introspection_info(obj))
        elif what_a_obj == '3':
            obj = requests
            pprint(introspection_info(obj))
        elif what_a_obj == '4':
            obj = pprint
            pprint(introspection_info(obj))
        elif what_a_obj == '5':
            obj = inspect
            pprint(introspection_info(obj))
        else:
            for i in ch:
                if what_a_obj != 'stop' and what_a_obj != i:
                    obj = '0'
            print("Введено неправильное значение.")

