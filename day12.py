''''
A Dictionary
'''
details = {'ids':['CGVI0242','CGVI0249',
                  'CGVI0224','CGVI0240'],
           'names':['Nikitha','Deepthi',
                    'Vinay','Tej'],
           'batch':'PFS-VSP-007',
           'place':('Vizag','Vjwda','Hyd','Bnglre'),
           'subjects':{'Python','Aptitude','Softskills'}}
'''
print(len(details))
#membership
print('ids' in details)
print('vinay' in details['names'])
print('python' in details['subjects'])

'''
#dictionary is a mutable collection
details['marks'] = [25,20,18,20]
print(details)
print(len(details))

#methods on dictionaries:
print(dir(details))
print(details.keys())
print(details.values())
print(details.items())

#print(details['ids'])
#print(details.get('ids'))
#print(details.get('ids'))

#Inserting multiple keys into the dictionary

data = {'email_ids':['nkt@gmail.com','dpt@icloud.com',
                     'vny@yahoo.com','tej@gmail.com'],
        'linkedin_ids':['nkt_123','dpt_234',
                        'vinay345','tej13']}
details.update(data)
print(details.keys())

#delete data from the dictionary
#pop(key) -->
'''
print(details.pop('marks'))
print(details.keys())
print(details.popitem())
print(details.clear())
print(details)
'''
#del
del details['marks'],details['ids']
print(details.keys())



