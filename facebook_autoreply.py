import requests
import json

ACCESS_TOKEN = "CAACEdEose0cBAECBMwWKOepaPCBTVYXdVQmddIWpzkguS1IfXxD2gyx6oi5T9qqd5FgSme4rYCxZAPHzZBXCWw9d64b2v9AoikNS8ZADeD6Koe8LboVkNlJmFAw7znVMuxrvZCBCSFTidZBYrAl7CPgq83zbiBhwZD"

CREATED_TIME = 1374863399

def fire():
    query = "SELECT post_id, actor_id, message FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time > " + CREATED_TIME + " LIMIT 200"
    response = requests.get("https://graph.facebook.com/fql/?q=" + query + "&access_token=" + ACCESS_TOKEN)
    allPosts = json.loads(response.text)['data']
    #allPost = allPosts[0]
    for eachPost in allPosts:
        user = getUserFirstName(str(eachPost['actor_id']))
        fname = user['first_name']
        print fname

        like_status = likePost(eachPost['post_id'])
        if like_status == 'true':
            print 'Post from ' + user['name'] + ' liked'

        message = 'Thanks ' + fname + ' :)'
        comment_id = commentOnPost(eachPost['post_id'],message)
        if 'id' in comment_id:
            print 'Commented on post from ' + user['name']


def getUserFirstName(user_id):
    who_url = "https://graph.facebook.com/" + user_id
    who = requests.get(who_url)
    who = json.loads(who.text)
    return who

def likePost(post_id):
    like_url = "https://graph.facebook.com/" + post_id + "/likes?access_token=" + ACCESS_TOKEN
    a = requests.post(like_url)
    return a.text

def commentOnPost(post_id,message):
    post_url = "https://graph.facebook.com/" + post_id + "/comments?message=" + message + "&access_token=" + ACCESS_TOKEN
    b = requests.post(post_url)
    return b.text

fire()
