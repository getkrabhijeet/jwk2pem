from jwcrypto import jwk, jws, jwt
import base64
import json
import sys

def jwk_to_pem(jwk_json):
  """
  Converts a JSON Web Key (JWK) to a PEM format public key.

  Args:
    jwk_json (str): The JSON representation of the JWK.

  Returns:
    str: The PEM format public key.

  """
  key = jwk.JWK.from_json(jwk_json)
  return key.export_to_pem(private_key=False, password=None).decode()

if __name__ == "__main__":
  jwk_json = sys.argv[1]

  try:
    jwks = json.loads(jwk_json)
  except json.JSONDecodeError:
    print("Invalid JWK JSON")
    sys.exit(1)

  pem = jwk_to_pem(jwk_json)
  print(pem)