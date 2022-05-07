from multiprocessing import cpu_count


def max_workers():
    return cpu_count()*2+1


# Set worker_class to 'gthread'
workers = max_workers()
threads = 4
# Wsgi behaviors
bind = '0.0.0.0:5000'
timeout = 180  # second
daemon = False
backlog = 1024
loglevel = 'info'
errorlog = '/kata/logs/gunicorn/error.log'
accesslog = '/kata/logs/gunicorn/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
limit_request_line = 0
