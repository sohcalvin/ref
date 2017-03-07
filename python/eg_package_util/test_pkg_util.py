import pkgutil

data = pkgutil.get_data('eg_package_util', 'datax/abc.dat')

# data = pkgutil.get_data(__package__, './def.dat')

b"abcde".decode("utf-8")

print(data)