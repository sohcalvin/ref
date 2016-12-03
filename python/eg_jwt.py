from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend
import jwt

public_key= '-----BEGIN PUBLIC KEY-----MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzvTWJNAjx9bSmGmcPaVws1rl65tgXE5fGNucsFdUy/y42EZpW48FrqWwgYs33S/AkTxITtZWh82EW9YMXLBY8l3LFi4GGOTRpV1/5+PjCUehNS/LY026GhrmAxNkJip60ZyWQdLLrz7IQownKT+LPPr+IrMgousx62trrWQfjimgSIKXnC4Zcp64bv0zdcrc/HXPc9C7PNj/xzSC08/3Gw4dBgtswYN7NuR8EArd92UkZzsWfXYdvvN1RSyqc/FpKFAEaFDxileRL6TbBGe7A7J1RuEQalp6q5378uzTsiTQb0o+9952SoL2W5l63jrLG9THD1oF4v+Xb4Afb0tKEwIDAQAB-----END PUBLIC KEY-----'
# cert_str = "".join(cert_str.strip().split("\n")[1:-1])
# cert_obj = load_pem_x509_certificate(cert_str, default_backend())
# public_key = cert_obj.public_key()

public_key ='''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzvTWJNAjx9bSmGmcPaVw
s1rl65tgXE5fGNucsFdUy/y42EZpW48FrqWwgYs33S/AkTxITtZWh82EW9YMXLBY
8l3LFi4GGOTRpV1/5+PjCUehNS/LY026GhrmAxNkJip60ZyWQdLLrz7IQownKT+L
PPr+IrMgousx62trrWQfjimgSIKXnC4Zcp64bv0zdcrc/HXPc9C7PNj/xzSC08/3
Gw4dBgtswYN7NuR8EArd92UkZzsWfXYdvvN1RSyqc/FpKFAEaFDxileRL6TbBGe7
A7J1RuEQalp6q5378uzTsiTQb0o+9952SoL2W5l63jrLG9THD1oF4v+Xb4Afb0tK
EwIDAQAB
-----END PUBLIC KEY-----'''


token_string = "022-f7ab8c12-0024-4dab-acba-4e25403d777b"
jwt.decode(token_string, public_key, algorithms=['RS256'])
