import csv
import pandas as pd

f = open('output_eulji.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
list1 = {}
print(type(rdr))
# for line in rdr:
    
f.close()


# column = ['평점', '영화제목', '작성자']
# results= crawling(1,1)

# df = pd.DataFrame(results, columns = column)
# df.to_excel('movie.xlsx', sheet_name='네이버영화', columns=column, header=True, startrow=1)
