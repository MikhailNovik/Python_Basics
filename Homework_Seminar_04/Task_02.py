# Задача 2. В первом списке находится информация об ассортименте мороженного, 
# во втором списке - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.

assortment_ice_cream = ['Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка']
storage_ice_cream = ['Сливочное', 'Вафелька', 'Сладкоежка']
assortment_ice_cream = set(assortment_ice_cream)
storage_ice_cream = set(storage_ice_cream)

difference = assortment_ice_cream.difference(storage_ice_cream)

print(f'Товар(ы) {difference} закончился(лись)')
