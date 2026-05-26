import sys

# Import Employee from package1
sys.path.append('C:/Users/nshra/git/PythonBasics')




from ModulesPackagesDay13.package1.package2.student import *
from ModulesPackagesDay13.package1.employee import *


e = Employee(101, 'Scott', 40000)
e.displayemp()   # Output: empid:101 empname:Scott empsal:40000


s = Student(141, 'David', 'A')
s.displaystu()   # Output: stuid:141 stuname:David stusal:A
