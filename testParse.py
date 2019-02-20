import time
import boto3
import datetime
import json

with open('transcriptedFileData.json') as f:
    data = json.load(f)


result_obj = data['results']
result_obj = result_obj['transcripts']
result_obj = result_obj[0]
print(result_obj['transcript'])


result_obj = data['results']["speaker_labels"]["segments"][0]

itemNumber = 0
contentNumber = itemNumber
for k in result_obj["items"]:
    # get the start time listed in the json response of each utterance
    print(result_obj["items"][itemNumber]["start_time"])
    #get the content associated with the above response time


    # check to avoid periods
    #if 'None' not in str(data['results']["items"][contentNumber]["alternatives"][0]["confidence"]):
    content = data['results']["items"][itemNumber]["alternatives"][0]["content"]
    #    contentNumber = contentNumber + 1
    print(content)
    itemNumber = itemNumber + 1
