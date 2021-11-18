import pusher

pusher_client = pusher.Pusher(
  app_id='1150637',
  key='4a49e7d498bf59680919',
  secret='42319c1ea0402f4a0e5b',
  cluster='us3',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})