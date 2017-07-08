import requests
res = requests.post('http://localhost:5001', json={'code':'#include <stdio.h> main() { printf("Hello World\n"); }', 'lang':'C'})
if res.ok:
    print(res.json())

# '#include <stdio.h> main() { printf("Hello World\n"); }'
