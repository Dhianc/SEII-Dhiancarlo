

try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/testfile.txt')
except Exception:
    print('Sorry. This file does not exist')

print('')
try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')

print('')
try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/test_file.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

print('')
try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

print('')
try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('')
try:
    f = open('/home/dhian/SEII-Dhiancarlo/Semana02/prog20/corrupt_file.txt')
    if f.name == '/home/dhian/SEII-Dhiancarlo/Semana02/prog20/corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")