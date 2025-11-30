def generate_full_name(firstname,  lastname):
    return firstname + ' ' + lastname


def sum_two_nums(a, b):
    return a + b

person = {
    'first_name' : 'raj',
    'last_name'  : 'Keshri',
    'age'        : 26,
    'country'    : 'India',
    'is_married' : False,
    'skills'     : ['python', 'html', 'css', 'javascript', 'reactjs', 'bootstrap', 'mysql', 'sql', 'php'],
    'address'    : {
        'pincode' : 800001,
        'street'  : 'boring road'
    }
}

def weight_of_object (mass, gravity):
    weight = str(mass * gravity) + ' N' # the value has to be changed to a string first
    return weight


gravity = 4

