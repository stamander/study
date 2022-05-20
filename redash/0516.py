
def get_query_result(){

}

def add_result_column(){

}

def add_result_row(){
    
}

int result = 0

events_count = get_query_result(62)['rows'][0]['id']

print(get_query_result(1))

print(get_query_result(62)['rows'])

print(get_query_result(62)['rows'][0])

print(get_query_result(62)['rows'][0]['id'])

print (events_count)



add_result_row(result, {'name': 'test', 'count': events_count})
print(result)

add_result_column(result, 'name', '', 'string')
print(result)
add_result_column(result, 'count', '', 'integer')
print(result)

