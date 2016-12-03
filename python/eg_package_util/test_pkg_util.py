import pkgutil

data = pkgutil.get_data('datax', 'abcx.dat')

data = pkgutil.get_data(__package__, './def.dat')

print(data)