from locust import HttpLocust, TaskSet, task, between
import json
import os
import redis

class LoginWithUniqueUsersSteps(TaskSet):
    def on_start(self):
        self.email = "Not_Exists"
        self.password = "Not_Exists"
        if len(user_list) > 0:
            self.email, self.password = user_list.pop()
            #print(self.email, self.password)

    @task
    def login(self):
        h = {
        'Content-Type': "application/json"
        }
        payload = {'email': self.email, 'password': self.password}
        r = self.client.post("/api/v1/auth/login",data=json.dumps(payload),headers=h)
        #print(r.text)
        print('current user is........: ' + self.email)
        #assert self.RESPONSE_TEXT.search(r.text) is not None


class LoginWithUniqueUsers(HttpLocust):
    task_set = LoginWithUniqueUsersSteps
    wait_time = between(5, 9)
    host = "http://amanmisra.io"
    def setup(self):
        global user_list
        User_Credentials = []
        base_folder = os.path.dirname(__file__)
        filename = os.path.join(base_folder,'data','users.json')
        with open(filename,'r',encoding='utf-8') as fin:
            data = json.load(fin)
            print(type(data),data)
        for user_credential in data:
            uc = (user_credential['email'], user_credential['password'])
            User_Credentials.append(uc)
        user_list = User_Credentials
