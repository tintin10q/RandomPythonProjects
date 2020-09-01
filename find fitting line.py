# Should be list of points
points = [(1,-1),(2,1),(3,5),(4,15),(2.5,-3)]

x_list = [i[0] for i in points]
y_list = [i[1] for i in points]
x_p_list = [i[0] * i[0] for i in points]
x_t_y_list = [i[0] * i[1] for i in points]

n = len(points)
x_sum = sum(x_list)
y_sum = sum(y_list)
x_p_sum = sum(x_p_list)
x_t_y_sum = sum(x_t_y_list)

print('x:\t\t∑ {}\t\t{}\n'
      'y:\t\t∑ {}\t{}\n'
      'x^2:\t∑ {}\t{}\n'
      'x*y:\t∑ {}\t{}\n'
      'n:\t\t{}\n'.format(x_sum, x_list, y_sum, y_list, x_p_sum, x_p_list, x_t_y_sum, x_t_y_list, n))

# Calculate everything
b_string = '{}a + {}'.format(-x_sum / n, y_sum / n)
b1 = -x_sum / n
b2 = y_sum / n

a = (x_t_y_sum - x_sum * b2) / (x_sum * b1 + x_p_sum)
b = (x_t_y_sum - x_p_sum * a) / x_sum

# Display 
print('nb + ∑(x)a = ∑(y)\n∑(x)b + ∑(x^2)a = ∑(x*y)', end="\n\n")
print('{n}b + {x_sum}a = {y_sum}'.format(n=n, x_sum=x_sum, y_sum=y_sum))
print('{x_sum}b + {x_p_sum}a = {x_t_y_sum}'.format(x_sum=x_sum, x_p_sum=x_p_sum, x_t_y_sum=x_t_y_sum), end="\n\n")

print("Find b formula:")
print('{n}b + {x_sum}a = {y_sum}'.format(n=n, x_sum=x_sum, y_sum=y_sum))
print('{}b = {}a + {}'.format(n, -x_sum, y_sum))
print('b = {}'.format(b_string), end="\n\n")

print('Solve a with b in other formula:')
print('{}({}) + {}a = {}'.format(x_sum, b_string, x_p_sum, x_t_y_sum))
print('{}a + {} + {}a = {}'.format(x_sum * b1, x_sum * b2, x_p_sum, x_t_y_sum))
print('{}a = {}'.format(x_sum * b1 + x_p_sum, x_t_y_sum - x_sum * b2))
print('a = {}'.format(a), end='\n\n')

print('Solve b with a:')
print('{}b + {}*{} = {}'.format(x_sum, x_p_sum, a, x_t_y_sum))
print('{}b + {} = {}'.format(x_sum, x_p_sum * a, x_t_y_sum))
print('{}b = {}'.format(x_sum, x_t_y_sum - x_p_sum * a))
print('b = {}'.format(b), end="\n\n")

print('Final formula:')
print('y = {}x + {}'.format(a, b))


# Some functions these are not used but can be used if other things want to use this
class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def find_y(self, x):
        return self.a * x + b


def find_line(points):
    x_list = [i[0] for i in points]
    y_list = [i[1] for i in points]
    x_p_list = [i[0] * i[0] for i in points]
    x_t_y_list = [i[0] * i[1] for i in points]

    n = len(points)
    x_sum = sum(x_list)
    y_sum = sum(y_list)
    x_p_sum = sum(x_p_list)
    x_t_y_sum = sum(x_t_y_list)
    a = (x_t_y_sum - x_sum * y_sum / n) / (x_sum * -x_sum / n + x_p_sum)
    b = (x_t_y_sum - x_p_sum * (x_t_y_sum - x_sum * y_sum / n) / (x_sum * -x_sum / n + x_p_sum)) / x_sum
    return Line(a, b)
