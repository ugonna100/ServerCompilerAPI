import requests
res = requests.post('http://localhost:5000', json={'code':'#include <stdio.h> \nint main() { printf(\"Hello World\"); }', 'lang':'C'})
if res.ok:
    print('POST success')
    print(res.json())

# '#include <stdio.h> main() { printf("Hello World\n"); }'
