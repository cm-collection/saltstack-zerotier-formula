import requests
from os.path import exists as _exists

def main():
  if not _exists('/var/lib/zerotier-one/authtoken.secret'):
    return {
      'zerotier': None
    }

  s = requests.Session()
  s.headers.update({
    'X-ZT1-AUTH': open('/var/lib/zerotier-one/authtoken.secret', 'r').read()
  })

  try:
    info = s.get('http://localhost:9993/status', timeout=10).json()
    networks = s.get('http://localhost:9993/network', timeout=10).json()
  except:
    return {
      'zerotier': None
    }

  data = {
    'zerotier': {
      'address': info.get('address'),
      'network': []
    }
  }

  for row in networks:
    data['zerotier']['network'].append({
      'id': row.get('id'),
      'mac': row.get('mac'),
      'name': row.get('name'),
      'status': row.get('status'),
      'assignedAddresses': row.get('assignedAddresses')
    })

  return data
