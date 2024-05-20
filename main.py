from pystyle import Colors, Colorate
from colorama import init
import argparse
import base64
import zlib
import ast
import re
import os

init()

def get_layer(code: str) -> dict:
  if re.findall(r'\(\D+ \+ \D+ \+ \D+ \+ \D+\)', code):
    return 'l1'
  elif re.findall(r'\^ .+ == .+', code):
    return 'l2'
  elif re.findall(r'[\D]+ = \[[\'\d., ]+\]', code):
    return 'l3'
  else:
    raise Exception('This file is not obfuscated with BlankObfV2')

def l1(code) -> str:
  print(Colors.purple+'[*] Deobfuscating layer1')
  slices = re.findall(r'\.decode\(\)\[[\d \-()+/:]+\]', code)
  tree = ast.parse(code)
  byte: list[ast.Call] = []
  for i in ast.walk(tree):
    if not isinstance(i, ast.Call):continue
    if not isinstance(i.func, ast.Name):continue
    if i.func.id != 'bytes':continue
    byte.append(i)
  important: list[list[ast.Constant]] = []
  for i in byte:
    lst = i.args[0].value.elts
    if len(lst) < 500:continue
    important.append(lst)
  _ = bytes([i.value for i in important[0]][::-1]).decode()[eval(slices[0].split('[')[-1].split(']')[0].split(':')[0]):eval(slices[0].split('[')[-1].split(']')[0].split(':')[1])]
  __ = bytes([i.value for i in important[1]][::-1]).decode()[eval(slices[1].split('[')[-1].split(']')[0].split(':')[0]):eval(slices[1].split('[')[-1].split(']')[0].split(':')[1])]
  ___ = bytes([i.value for i in important[2]][::-1]).decode()[eval(slices[2].split('[')[-1].split(']')[0].split(':')[0]):eval(slices[2].split('[')[-1].split(']')[0].split(':')[1])]
  ____ = bytes([i.value for i in important[3]][::-1]).decode()[eval(slices[3].split('[')[-1].split(']')[0].split(':')[0]):eval(slices[3].split('[')[-1].split(']')[0].split(':')[1])]
  return zlib.decompress(base64.b64decode(_+__+___+____)).decode(errors='replace')

def l2(code) -> str:
  print(Colors.purple+'[*] Deobfuscating layer2')
  obfuscated=eval('[' + re.findall(r'[\D]+ = \[[\d.,+/\-() ]+\]', code)[0].split('[')[-1])
  loc = re.findall(r'\[[\d+ /\-()]+\]', re.findall(r'if .+:', code)[0])
  in_loc = eval(loc[0].replace('[',' ').replace(']', ''))
  re_loc = eval(loc[1].replace('[', '').replace(']', ''))
  for it1 in range(1, 100):
    if obfuscated[in_loc] ^ it1 == obfuscated[re_loc]:
      kaka=zlib.decompress(bytes(map(lambda arg1: arg1 ^ it1, obfuscated[0:in_loc] + obfuscated[in_loc+1:re_loc] + obfuscated[re_loc+1:])))
      break
  return kaka.decode(errors='replace')

def l3(code) -> str:
  print(Colors.purple+'[*] Deobfuscating layer3')
  obfuscated = eval('['+re.findall(r'[\D]+ = \[[\'\d., ]+\]', code)[0].split('[')[-1])
  deobfuscated = ''
  for i in obfuscated:
    for _ in i.split('.'):
      deobfuscated=deobfuscated+chr(int(_))
  return zlib.decompress(base64.b64decode(deobfuscated)).decode()

def deobf(code: str) -> str:
  if """:: You managed to break through BlankOBF v2; Give yourself a pat on your back! ::""" in code:
    return code.replace(""":: You managed to break through BlankOBF v2; Give yourself a pat on your back! ::""", """Deobfuscated using github.com/lululepu/UnblankObfV2""")
  else:
    match get_layer(code):
      case 'l1':
        return deobf(l1(code))
      case 'l2':
        return deobf(l2(code))
      case 'l3':
        return deobf(l3(code))

def main() -> None:
  parser = argparse.ArgumentParser(prog=os.path.basename(__file__), description='UnblankObfV2: A BlankObf2 Deobfuscator')
  parser.add_argument('--input', '-i', required=True, help='Path Of The File To Deobfuscate', metavar='PATH')
  parser.add_argument('--output', '-o', required=False, help='Path Of The File To Write The Deobfuscate Script (Default: deobfuscated_(filename).py)', metavar='PATH')
  args = parser.parse_args()

  if not os.path.isfile(args.input):
    raise FileNotFoundError('Incorect file input')
  
  output = args.output or f'deobfuscated_{os.path.basename(args.input)}'
  
  with open(args.input, 'rb') as f:
    obfuscated = f.read().decode(errors='replace')

  deobfuscated = deobf(obfuscated)

  with open(output, 'w') as f:
    f.write(deobfuscated)

  print(Colors.purple+f'[+] Succesfully Deobfuscated To {output} !')
  
  
if __name__ == '__main__':
  main()