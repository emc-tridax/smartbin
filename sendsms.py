import smsapi
api = smsapi.ovh()


api.set_username('savitha')
api.set_password('susan')

#sending SMS

api.service('sms').action('send')

api.set_content('Hello [%1%] [%2%]')
api.set_params('name', 'last name')
api.set_to('9900506092')
api.set_from('Info') 

result = api.execute()
for r in result:
    print r.id, r.points, r.status

