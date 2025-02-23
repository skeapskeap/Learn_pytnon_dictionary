"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов со средним налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger",
                "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey",
                "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez",
                "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley",
                "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker",
                "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert",
                "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley",
                "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman",
                "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

# 1. Вывести названия всех отделов
for dictionary in departments:
    print(f'{dictionary["title"]}')

# 2. Вывести имена всех сотрудников компании.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        print(dicts['first_name'])


# 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        name = dicts["first_name"]
        print(name, dictionary["title"])

# 4. Вывести имена всех сотрудников компании, которые получают больше 100к.
for dictionary in departments:
    for dicts in dictionary["employers"]:
        name = dicts["first_name"]
        if dicts["salary_rub"] > 100000:
            print(name)

# 5 Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
for dictionary in departments:
    for dicts in dictionary["employers"]:
        position = dicts["position"]
        if dicts["salary_rub"] < 80000:
            print(position)

# 6 Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела


for dictionary in departments:
    dep_spendings = list()
    for dicts in dictionary["employers"]:
        sallary = dicts["salary_rub"]
        dep_spendings.append(sallary)

        final_dep_spendings = sum(dep_spendings)
    print(f"затраты {dictionary['title']} - {final_dep_spendings}")

# 7. Вывести названия отделов с указанием минимальной зарплаты в нём.
for employers_info in departments:
    all_sallary = list()
for info in employers_info["employers"]:
    sallary = info["salary_rub"]
    all_sallary.append(sallary)
minimum_sallry = min(all_sallary)
print(f"минимальная зарплата в отделе {employers_info['title']} : {minimum_sallry}")


# 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
ultimate_sallary = list()
for employers_info in departments:
    all_sallary = list()
    for info in employers_info["employers"]:
        sallary = info["salary_rub"]
        all_sallary.append(sallary)
    minimum_sallry = min(all_sallary)
    midium_sallry = sum(all_sallary)/len(all_sallary)
    maximum_sallary = max(all_sallary)
    print(f"""минимальная зарплата в отделе {employers_info['title']}:{minimum_sallry},
           средняя: {midium_sallry}, максимальная: {maximum_sallary}""")

# 9. Вывести среднюю зарплату по всей компании.
ultimate_sallary.extend(all_sallary)
medium_ultimate_sallary = max(ultimate_sallary)/len(ultimate_sallary)
print(medium_ultimate_sallary)
# 10. Вывести названия должностей, которые получают больше 90к без повторений.
positioin_set = set()
for employers_info in departments:
    for info in employers_info["employers"]:
        position = info["position"]
        if info["salary_rub"] > 90000:
            positioin_set.add(position)

for position_ in positioin_set:
    print(position_)


# 11. Посчитать среднюю зарплату по каждому отделу среди девушек
# (их зовут Мишель, Николь, Кристина и Кейтлин).
WOMEN_NAMES = {"Michelle", "Nicole", "Caitlin", "Christina"}
for employers_info in departments:
    all_women_sallary = list()
    for info in employers_info["employers"]:
        sallary = info["salary_rub"]
        name = info["first_name"]
        if name in WOMEN_NAMES:
            all_women_sallary.append(sallary)
    sum_all_women_sallary = sum(all_women_sallary)
    print(f"""средняя зарплата дувушек в {employers_info['title']}
           :{sum_all_women_sallary}""")

# 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
vowels_list = ["a", "e", "i", " o", "u", "y"]
surnames_set = set()
for employers_info in departments:
    for info in employers_info["employers"]:
        if info["last_name"][-1] in vowels_list:
            surnames_set.add(info["first_name"])
            
for name_ in surnames_set:
    print(name_)

#13. Вывести список отделов со средним налогом на сотрудников этого отдела.

for employers_info in departments:
    department_name = employers_info['title']
    for tax in taxes:
        if department_name == "HR department":
            if tax["department"] is None:
                total_tax = tax["value_percents"]
                print(department_name, total_tax)
        if department_name == "IT department":
            if tax["department"] == None:
                total_tax_for_all = tax["value_percents"]
            else:
                if tax["department"] == "IT Department":
                    total_tax = total_tax_for_all + tax["value_percents"]
                    print(department_name, total_tax)
                else:
                    department_name = "BizDev Department"
                    total_tax = total_tax_for_all + tax["value_percents"]
                    print(department_name, total_tax)
print('--------------')

#14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.


for employers_info in departments:
    sallary_per_dep = {}
    for info in employers_info["employers"]:
        name = info["first_name"]
        surname = info["last_name"]
        sallary_gross = info["salary_rub"]
        departments_name = employers_info["title"]
        sallary_per_dep[departments_name] = (name, surname, sallary_gross)
        #print(sallary_per_dep)
        for department_name in sallary_per_dep.keys():
            taxes_per_dep = 0
            for tax in taxes:
                if tax["department"] is None or departments_name.lower() == tax["department"].lower():
                    taxes_per_dep += int(tax["value_percents"])
                    netto = sallary_per_dep[department_name][2] - (sallary_per_dep[department_name][2] * taxes_per_dep/100)
                    
            print(f'{department_name}, {sallary_per_dep[department_name][0]}, {sallary_per_dep[department_name][1]}, {sallary_per_dep[department_name][2]}, зп нетто: {netto}')


# 15. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
for employers_info in departments:
    sallary_per_dep = {}
    sallary_sum =[]
    for info in employers_info["employers"]:
        name = info["first_name"]
        surname = info["last_name"]
        sallary_gross = info["salary_rub"]
        departments_name = employers_info["title"]
        sallary_sum.append(sallary_gross)
    sallary_sum = sum(sallary_sum)
    sallary_per_dep[departments_name] = sallary_sum

    for department_name in sallary_per_dep.keys():
        taxes_per_dep = 0
        taxes_per_dep_final = 0
        all_taxes = {}
        for tax in taxes:
            
            if tax["department"] is None or department_name.lower() == tax["department"].lower():
                taxes_per_dep += int(tax["value_percents"])
                taxes_per_dep_final = (int(sallary_per_dep[department_name])
                                 * (int(taxes_per_dep)/100))
                all_taxes[department_name] = taxes_per_dep_final
               
        print(f'{all_taxes}')
        print("------")


# # 16. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
for employers_info in departments:
    sallary_per_dep = {}
    for info in employers_info["employers"]:
        name = info["first_name"]
        surname = info["last_name"]
        sallary_gross = info["salary_rub"]
        departments_name = employers_info["title"]
        sallary_per_dep[departments_name] = (name, surname, sallary_gross)
        for department_name in sallary_per_dep.keys():
            taxes_per_dep = 0
            for tax in taxes:
                if tax["department"] is None or departments_name.lower() == tax["department"].lower():
                    taxes_per_dep += int(tax["value_percents"])
                    tax_per_person = sallary_per_dep[department_name][2] * (taxes_per_dep/100)
            if tax_per_person > 100000:
                print((sallary_per_dep[department_name][0],
                        sallary_per_dep[department_name][1]))
                print("------")


# #17. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
# 
tax_per_person_dict = {}

for employers_info in departments:
    sallary_per_dep = {}
    
    for info in employers_info["employers"]:
        name = info["first_name"]
        surname = info["last_name"]
        sallary_gross = info["salary_rub"]
        departments_name = employers_info["title"]
        sallary_per_dep[departments_name] = (name, surname, sallary_gross)
        
        for department_name in sallary_per_dep.keys():
            taxes_per_dep = 0
            
            for tax in taxes:
                if tax["department"] is None or departments_name.lower() == tax["department"].lower():
                    taxes_per_dep += int(tax["value_percents"])
                    tax_per_person = sallary_per_dep[department_name][2] * (taxes_per_dep/100)
                    name_ = sallary_per_dep[department_name][0]
                    surname_ = sallary_per_dep[department_name][1]
                    tax_per_person_dict[name, surname_] = tax_per_person
            
sallary_range = []
for name_surname_, sallary_in_dict in tax_per_person_dict.items():
    sallary_range.append(sallary_in_dict)
min_sallary = min(sallary_range)
print(name_surname_, min_sallary)
            