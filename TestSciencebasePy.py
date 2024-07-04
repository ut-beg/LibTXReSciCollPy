import sciencebasepy
import json

sb = sciencebasepy.SbSession()

sb.login("aaron.averett@beg.utexas.edu", "Idriveapolestar2!")

myItemsId = sb.get_my_items_id()

childIds = sb.get_child_ids('4f4e4762e4b07f02db47dff0')

for childId in childIds:
    itemProps = sb.get_item(childId)
    
    print(itemProps)

