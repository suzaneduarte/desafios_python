while True:
  try: 
    senha = input()

    tem_maisucula = False
    tem_minuscula = False
    tem_digito = False
    fora_do_alfabeto = False
    tamanho = len(senha)

    for letra in senha:
      if ord(letra) > 64 and ord(letra) < 91:
        tem_maisucula = True
      elif ord(letra) > 96 and ord(letra) < 123:
        tem_minuscula = True
      elif ord(letra) > 47 and ord(letra) < 58:
        tem_digito = True
      else:
        fora_do_alfabeto = True
        break
    
    if tem_maisucula and tem_minuscula and tem_digito and not fora_do_alfabeto and tamanho >= 6 and tamanho <= 32:
      print('Senha valida.')
    else:
      print('Senha invalida.')

  except EOFError:
    break