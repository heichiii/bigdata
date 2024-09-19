#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22,"liu":50}
    m = 'li'
    v = 0
    for key in person.keys():
        if person[m] < person[key]:
            m = key
            v = person[m]

    # print('%s,%d' % (m, person[m]))
    for key in person.keys():
        if person[key] == v:
            print(key)

    print(v)
