#29 December 2025

med= ('Advil', 'Tylenol','Aspirin' , 'Vitamin C')
#packing and unpacking a tuple is assigning whatever in meds to a variable we assign
#unpacking is pairing and assinging an element in a tuple to a variable
#(morningmed, afternoonmed, eveningmed, nightmed) =med
#print(morningmed, afternoonmed,eveningmed, nightmed)
#(*other, second_med, third_med) =med
#print(second_med)
#print(third_med)
#print(other)

#(first_med, *others, last_med) = med #position of the = is significant
#print(first_med)
#print(others)
#print(last_med)


#(first_med, second_med, *rest) = med
#print(first_med)
#print(second_med)
#print(rest)

#unpacking just 1 item
#one_med = med[1]
#print(one_med)
#(one_med, *rest) = med # cant use *twice.
#print(rest)
#print(one_med)

#morning = med[0]
#afternoon = med[1]
#evening = med[2]
#night= med[3]
#print(morning)
#print(afternoon)
#print(evening)
#print(night)

#new_meds=list(med)#convert tuples to list
#new_meds[2]='paracetamol'#change Aspirin to paracetamol
#med=tuple(new_meds)#convert list to tuples
#print(med)

#ages= (23,45,67,89,23,45,67,89)
#print(ages.count(23)) #count -number of times a character appears
#print(ages.index(23)) #index

#Dictionary
