b= 'Bazinga!'
t= 'Raj trapaceou!!'
e= 'De novo!'

map_to_winner = {
  'pedra': {
    'pedra': e,
    'papel': t,
    'tesoura': b,
    'lagarto': b,
    'Spock': t,
  },
  'papel': {
    'pedra': b,
    'papel': e,
    'tesoura': t,
    'lagarto': t,
    'Spock': b,
  },
  'tesoura': {
    'pedra': t,
    'papel': b,
    'tesoura': e,
    'lagarto': b,
    'Spock': t,
  },
  'lagarto': {
    'pedra': t,
    'papel': b,
    'tesoura': t,
    'lagarto': e,
    'Spock': b,
  },
  'Spock': {
    'pedra': b,
    'papel': t,
    'tesoura': b,
    'lagarto': t,
    'Spock': e,
  },
}
quantidade = int(input())

for index, valor in enumerate(range(quantidade)):
    sheldon, raj = input().split()
    print(f'Caso #{index+1}: {map_to_winner[sheldon][raj]}')