import json
import datetime
from dateutil.relativedelta import relativedelta

targetAccounts = {{targetAccounts}}

print("targetAccountsは" + str(targetAccounts))

accountQuery='''select id,name from ftra.account where id in(%s) order by id'''% (targetAccounts)

print(accountQuery)

accounts = execute_query('forte_ftra_readonly',accountQuery)['rows']
print(accounts)

for data in accounts:
    print("id:"+ str(data['id']))
    print("name:" + str(data['name']))
    
    add_result_row(result,{
        "id":data['id'],
        "name":data['name']
    
    })
    
add_result_column(result,'id','','integer')
add_result_column(result,'name','','string')
