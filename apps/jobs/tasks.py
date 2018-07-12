import celery
from celery import task
from django.views.decorators.http import require_http_methods
import socket
from celery.task.control import inspect
from django.http import HttpResponse
import os
import subprocess
import shlex


@task()
def execute_py(record):
    if os.name == 'nt':
        execute_file = "C:\Users\Administrator\PycharmProjects\hbgj_statistics\dbClient\utils.py"
    else:
        execute_file = "/home/huolibi/local/hbgj_statistics/dbClient/utils.py"

    job_table = record['job_table']
    job_path = record['job_path']
    job_name = record['job_name']
    job_type = record['job_type']
    job_days = record['days']
    cmd = "python " + execute_file + " -table " + job_table + " -path " + job_path + " -name " + job_name + " -day " + str(job_days) + " -jobType " + str(job_type)
    cmd = shlex.split(cmd)
    p = subprocess.Popen(cmd)
    p.wait()


def get_celery_queue_num():
    hostname = socket.gethostname()
    queue = 'celery@' + hostname
    i = inspect()
    return HttpResponse(len(i.active()[queue]))


@require_http_methods(['POST'])
def execute_day_job(request):
    import json
    request_data = json.loads(request.body)
    for r in request_data['record']:

        if 'startDate' in r and 'endDate' in r:
            diff_start_end, diff_today_end = count_diff_days(r['startDate'], r['endDate'])
            print diff_start_end, diff_today_end
            days = diff_today_end
            for i in xrange(diff_start_end + 1):
                r['days'] = days
                execute_py.delay(r)
                days += 1
        else:
            execute_py.delay(r)

    return HttpResponse(get_celery_queue_num(), content_type="application/json")


def count_diff_days(start_date, end_date):
    import datetime
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    diff_start_end = (end_date - start_date).days

    today_now = datetime.datetime.now().strftime('%Y-%m-%d')
    diff_today_end = (datetime.datetime.strptime(today_now, '%Y-%m-%d') - end_date).days
    return diff_start_end, diff_today_end


if __name__ == '__main__':
    print count_diff_days('2017-12-25', '2017-12-31')