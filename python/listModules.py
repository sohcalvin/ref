import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages])

for i in installed_packages_list :
    parts = str(i).split('==',2);
    print('Module : {0:25}   {1}'.format(parts[0],parts[1]))

