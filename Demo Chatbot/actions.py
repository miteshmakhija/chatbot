# from rasa_core_sdk import Action
# import requests
# import json
# import pymongo
# from bson import json_util


# class action_get_feed(Action):

#     def name(self):
#         return 'action_get_feed'

#     def run(self, dispatcher, tracker, domain):
#         category = tracker.get_slot('category')
#         print(category)
#         # url = 'https://api.nytimes.com/svc/topstories/v2/{category}.json'.format(category=category)
#         # params = {'api-key': "jNl3zkzzvjliODzm8YG2QC8rAtCW5RQg", 'limit': 5}
#         # response = requests.get(url, params).text
#         # json_data = json.loads(response)['results']
#         # i = 0
#         # for results in json_data:
#         #     i = i+1
#         #     message = str(i) + "." + results['abstract']
#         #     dispatcher.utter_message(message)
#         # return[]

# from rasa_core.actions import Action
# from rasa_core.events import SlotSet
# #from IPython.core.display import Image, display

# import requests

# class ApiAction(Action):
#     def name(self):
#         return "action_get_help"

#     def run(self, dispatcher, tracker, domain):
        
#         group = tracker.get_slot('Numpy','Pandas','Matplotlib')
        
#         r = requests.get('http://shibe.online/api/{}?count=1&urls=true&httpsUrls=true'.format(group))
#         response = r.content.decode()
#         response = response.replace('["',"")
#         response = response.replace('"]',"")
