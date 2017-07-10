import requests

# C code test
# res = requests.post('http://localhost:5000', json={'code': '#include <stdio.h> \nint main() { printf(\"Hello World! This is C!\"); }', 'lang': 'C'})

# Python code test
# res = requests.post('http://localhost:5000', json={'code': 'print("Hello World! This is python!")', 'lang': 'python'})

# Java code test
res = requests.post('http://localhost:5000', json={'code': 'public class code {public static void main(String[] args) {System.out.println("Hello World!");} }', 'lang': 'java'})
if res.ok:
    print('POST success')
    print(res.json())

# '#include <stdio.h> main() { printf("Hello World\n"); }'
