primeans = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def check_domain(number):
  domains = ''
  # Find the domains this number belongs to
  if number % 5 == 0:
    domains = domains + 'Pentadian '
  # Check if it belongs to other domains after this
  if number < 0:
    domains = domains + 'Minutian '

  if '2' in str(number):
    domains = domains + 'Disiphine '

  if number in primeans:
    domains = domains + 'Primean '

  return domains

# Write the rest of your program after this
numbers = input('Enter numbers: ').split()

free_number_counter = 0

for n in numbers:
  n = int(n)
 
  if check_domain(n) == '':
    free_number_counter = free_number_counter + 1
  
  else:
    print(f'{n} is a {check_domain(n)}citizen.')

print(f'Free numbers: {free_number_counter}')
