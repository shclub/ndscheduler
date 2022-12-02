"""A job to send a HTTP (GET or DELETE) periodically."""

import logging
import requests
import json

from ndscheduler.corescheduler import job

logger = logging.getLogger(__name__)


class CurlJob(job.JobBase):
    TIMEOUT = 10

    @classmethod
    def meta_info(cls):
        return {
            'job_class_string': '%s.%s' % (cls.__module__, cls.__name__),
            'notes': 'This sends a HTTP request to a particular URL',
            'arguments': [
                # url
                {'type': 'string', 'description': 'What URL you want to make a GET call?'},
                # Request Type
                {'type': 'string', 'description': 'What request type do you want? '
                                                  '(currently supported: GET/DELETE/POST)'},
                # Data
                {'type': 'string', 'data': 'What request type do you want? '
                                                  '(currently supported: GET/DELETE/POST)'},

            ],
            'example_arguments': ('["http://localhost:8888/api/v1/jobs", "GET"]'
                                  '["http://localhost:8888/api/v1/jobs/ba12e", "DELETE"]'
                                 '["http://shclub.synology.me:32773/trade", "POST",{“gubun" : "auto" ,"type": "view","position" : "40","company" : "next”}]')
        }

    def run_old(self, url, request_type,  *args, **kwargs):
        print('Calling GET on url: %s' % (url))

        session = requests.Session()
        result = session.request(request_type,
                                 url,
                                 timeout=self.TIMEOUT,
                                 headers=None,
                                 data=None)
        return result.text
    
    def run(self, url, request_type, data,  *args, **kwargs):
        print('Calling Post on url: %s' % (url))
        
        
        #data = {
        #    'gubun' : 'auto',
        #    'type' : 'view',
        #    'position' : '40',
        #    'company' : 'next'
        #}
        
        headers = {'Content-Type': 'application/json; chearset=utf-8'}
        
        session = requests.Session()
        response = session.post(url, timeout=self.TIMEOUT, data=json.dumps(data) ,headers=headers)

        #print("Status Code", response.status_code)
        #print("JSON Response ", response.json())
        res_text = str(response.status_code) + " | " + response.text
        print(res_text)
        return response.json()


if __name__ == "__main__":
    job = CurlJob.create_test_instance()
    job.run('http://localhost:8888/api/v1/jobs')
