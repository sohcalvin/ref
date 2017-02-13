array_of_objects = [
     { 'name' : "aaa" , 'age' : 10},
     { 'name' : "bbb" , 'age' : 9},
     { 'name' : "ccc" , 'age' : 8}
]

print("Before\n", array_of_objects)

sorted_cv_list = sorted(array_of_objects, key=lambda x: x['name'], reverse=True)

print("After\n", sorted_cv_list)
'''============================================================='''
list = [
  {
    "category": "Software-Quality Assurance",
    "mean": 2.643459177411592
  },
  {
    "category": "Consulting  and Professional Services",
    "mean": 2.4158017053660368
  },
  {
    "category": "Software-Design and Development",
    "mean": 2.398192648017362
  },
  {
    "category": "Software-Development Operations",
    "mean": 2.298801377236644
  },
  {
    "category": "Software-Research",
    "mean": 2.2769881163923626
  },
  {
    "category": "Solution and Product Management",
    "mean": 2.225062952720345
  },
  {
    "category": "Finance",
    "mean": 2.2011014050177993
  },
  {
    "category": "Software-User Experience",
    "mean": 2.142929280738698
  },
  {
    "category": "Customer Service and Support",
    "mean": 2.109341657075039
  },
  {
    "category": "Information Technology",
    "mean": 1.9275579631456372
  },
  {
    "category": "Administration",
    "mean": 1.8384698740725136
  },
  {
    "category": "Sales Support",
    "mean": 1.7474193021037134
  },
  {
    "category": "Presales",
    "mean": 1.6865308858998047
  },
  {
    "category": "Corporate Operations",
    "mean": 1.677410058981199
  },
  {
    "category": "Sales Operations",
    "mean": 1.6438368957830596
  },
  {
    "category": "Legal",
    "mean": 1.5759237370214219
  },
  {
    "category": "Human Resources",
    "mean": 1.5681842323031285
  },
  {
    "category": "Sales",
    "mean": 1.567478077837337
  },
  {
    "category": "Education and Training",
    "mean": 1.5270562039523143
  },
  {
    "category": "Communication",
    "mean": 1.454593727299921
  },
  {
    "category": "Marketing",
    "mean": 1.3347795572885122
  },
  {
    "category": "Software-Design und Entwicklung",
    "mean": 1.2127282862735547
  },
  {
    "category": "Bildung und Training",
    "mean": 0.7775512914937461
  },
  {
    "category": "Pre-Sales",
    "mean": 0.5167904989614273
  },
  {
    "category": "Kundenservice und Unterstützung",
    "mean": 0.2820655447101124
  },
  {
    "category": "Solution und Produkt Management",
    "mean": 0.18880629261368528
  },
  {
    "category": "Sekretariat / Assistenz",
    "mean": 0.17587600470811451
  },
  {
    "category": "Personal",
    "mean": 0.05624946244445833
  }
]


sorted_list = sorted(list, key=lambda x: x['mean'], reverse=True)
print(sorted_list)