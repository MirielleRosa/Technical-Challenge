# Libraries:
* requests
* json
* os
* numpy
* from cgi import test
* pandas as pd

- Each frequency (daily, monthly and yearly) has a function for its calculations
from the function `def day():`,`def month():`,`def year():` it is possible to obtain the calculations of capital and earned values ​​from what is being available in the API. 

# Using the `for` looping structure to read the json-formatted API(response)

* The functions mentioned above are basically composed of:
    - A counter being incremented to gain access to data through indexes.
    - Calculation:
        `valorTotal += valorTotal * (float(n['valor'])/100)`
        `valorGanho = valorTotal - valorInicial` 
    - .csv file (for better visualization generated in a spreadsheet).

**The resolution of the functions may have some differences due to the fact that their frequencies (day, month and year) are different**

* Menu:
    - Finally, a menu of instructions is used to generate daily, monthly and annual frequency calculations..

# Question answer:
- In the `period():` function it is possible to get the answer to the question:

    * What was the most profitable period of 500 calendar days since 2000-01-01 until 2022-03-31? That is, if you had to invest `C` amount of capital for 500 days, what would have been the most profitable period from the beginning of 2000 until the end of March/2022? Your answer should be the start and end dates of the period you found.

    * Most profitable period of 500 days: 
    The most profitable period of 500 between 01/01/2000 to 03/31/2022 was:
    - 30/10/2001 to 23/10/2003.



**I'm sorry about my English. I ended up losing a lot of practice. Anyway, thanks.**
