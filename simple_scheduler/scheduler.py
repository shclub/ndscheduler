"""Run the scheduler process."""

from ndscheduler.server import server


class SimpleServer(server.SchedulerServer):

    def post_scheduler_start(self):
        # New user experience! Make sure we have at least 1 job to demo!
        jobs = self.scheduler_manager.get_jobs()
        if len(jobs) == 0:
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.sample_job.AwesomeJob',
                name='My Awesome Job',
                pub_args=['first parameter', {'second parameter': 'can be a dict'}],
                minute='*/30')
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.curl_job.CurlJob',
                name='invest_view',
                pub_args=['http://shclub.synology.me:32773/trade', 'POST',{'gubun' : 'auto' ,'type': 'view','position' : '40','company' : 'next'}],
                minute='40')
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.curl_job.CurlJob',
                name='invest_call_long_30',
                pub_args=['http://shclub.synology.me:32773/trade', 'POST',{'gubun' : 'auto' ,'type': 'long','position' : '30','company' : 'next','pc_name' : 'LENOVO-M79'}],
                minute='40',hour='0')
             self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.curl_job.CurlJob',
                name='invest_call_short_30',
                pub_args=['http://shclub.synology.me:32773/trade', 'POST',{'gubun' : 'auto' ,'type': 'short','position' : '30','company' : 'next','pc_name' : 'LENOVO-M79'}],
                minute='41',hour='0')
            self.scheduler_manager.add_job(
                job_class_string='simple_scheduler.jobs.curl_job.CurlJob',
                name='invest_sett',
                pub_args=['http://shclub.synology.me:32773/trade', 'POST',{'gubun' : 'auto' ,'type': 'sett','position' : '30','company' : 'next'}],
                minute='30',hour='4')
            
if __name__ == "__main__":
    SimpleServer.run()
