#!/usr/bin/env python
"""
Show system information of Linux host.

Very simple alternative to sysinfo2html_ and phpWebSysInfo_ apps.

.. _sysinfo2html: http://www.mrleejohn.nl/sysinfo2html/
.. _phpSysInfo: http://phpsysinfo.sourceforge.net/
"""

import copy
import datetime
import os
import socket
import sys

from string import Template
from subprocess import PIPE, Popen
from wsgiref.simple_server import make_server


CONFIG = {
    'DATETIME_FORMAT': '%a %b %d %H:%M %Z %z %Y',
    'REFRESH_SECONDS': 300,
    'TITLE': 'sysinfo2web.py',
}
IP = '0.0.0.0'
NOW = datetime.datetime.now
PORT = 8000
PRETTIFY_NAMES = {
    'Avail': 'Available',
    'Use%': 'Used %',
}
SCRIPT_NAME = os.path.basename(sys.argv[0])
TEMPLATE = """<!DOCTYPE html>
<html>

<head>
    <title>$server_name &bull; $TITLE</title>

    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="Refresh" content="$REFRESH_SECONDS">

    <style media="screen, projection" type="text/css">
        table {
            width: 100%;
        }

        table tbody td {
            vertical-align: top;
        }

        table thead th {
            text-align: left;
        }

        table thead th:first-child {
            font-size: large;
        }
    </style>
</head>

<body>

    <h1>$server_name</h1>

    <hr>

    <table>
        <thead>
            <tr>
                <th colspan="2">System information</th>
            </tr>
        </thead>

        <tbody>
            <tr>
                <td width="20%">OS:</td>
                <td>$uname</td>
            </tr>

            <tr>
                <td width="20%">Python:</td>
                <td>$python_version</td>
            </tr>

            <tr>
                <td width="20%">Date and time:</td>
                <td>$date</td>
            </tr>

            <tr>
                <td width="20%">Uptime:</td>
                <td>$uptime</td>
            </tr>
        </tbody>
    </table>

    <hr>

    <table>
        <thead>
            <tr>
                <th colspan="$memory_num_columns">Memory usage</th>
            </tr>
            $memory_headers
        </thead>
        $memory_data
    </table>

    <hr>

    <table>
        <thead>
            <tr>
                <th colspan="$filesystems_num_columns">Mounted filesystems</th>
            </tr>
            $filesystems_headers
        </thead>
        $filesystems_data
    </table>

    <hr>

    <table>
        <thead>
            <tr>
                <th colspan="$users_num_columns">Logged in users</th>
            </tr>
            $users_headers
        </thead>
        $users_data
    </table>

    <hr>

    <table>
        <thead>
            <tr>
                <th colspan="2">Network usage</th>
            </tr>
        </thead>
    </table>


</body>

</html>
"""


def get_info(key, cmd):
    output = Popen(cmd, stdout=PIPE).communicate()[0]
    output = output.splitlines()

    if key == 'users':
        del output[0]
        output = filter(lambda line: not SCRIPT_NAME in line and \
                                     not line.endswith(' '.join(cmd)), output)

    headers = filter(lambda item: item, output[0].split(' '))

    if key == 'filesystems':
        headers[-2] += ' ' + headers[-1]
        del headers[-1]
    elif key == 'memory':
        headers.insert(0, '')

    data = []

    for line in output[1:]:
        line_data = filter(lambda item: item, line.split(' '))

        if len(line_data) < len(headers):
            while len(line_data) != len(headers):
                line_data.append('')
        elif len(line_data) > len(headers):
            index = len(headers) - 1
            line_data[index] = ' '.join(line_data[index:])
            del line_data[index + 1:]

        data.append(line_data)

    return {key + '_data': make_table_content(data),
            key + '_headers': make_table_content([headers], True),
            key + '_num_columns': len(headers)}


def get_sysinfo():
    # Default values
    result = {'date': NOW().strftime(CONFIG['DATETIME_FORMAT']),
              'host_name': os.environ.get('HOSTNAME'),
              'host_type': os.environ.get('HOSTTYPE'),
              'python_version': sys.version.replace("\n", "<br>\n"),
              'python_version_short': ' '.join(map(str, sys.version_info)),
              'server_name': socket.gethostname(),
              'server_type': os.environ.get('MACHTYPE'),
              'uname': ' '.join(os.uname())}

    # Get uptime information
    output = Popen('uptime', stdout=PIPE).communicate()[0]
    result.update({'uptime': output.strip().split(' ', 1)[1]})

    # Get memory information
    result.update(get_info('memory', ['free', '-mot']))

    # Get information about mounted filesystems
    result.update(get_info('filesystems', ['df', '-hT', '--total']))

    # Get information about logged in users
    result.update(get_info('users', ['w', '-f']))

    return result


def main():
    # Read host and port values from user argument
    if len(sys.argv) == 2:
        try:
            ip, port = sys.argv[1].split(':')
        except ValueError:
            return usage()
        else:
            try:
                port = int(port)
            except (TypeError, ValueError):
                sys.exit('ERROR: <port> must be a valid integer.')

            if not ip:
                ip = IP
    elif len(sys.argv) > 2:
        return usage()
    else:
        ip, port = IP, PORT

    # Start WSGI server
    httpd = make_server(ip, port, sysinfo_app)

    print('Server is running at http://%s:%d/') % (ip, port)
    print('Quit the server with CONTROL-C.')

    httpd.serve_forever()


def make_table_content(lines, use_th=False):
    content = ''

    for data in lines:
        content += '<tr>\n'

        for item in data:
            item = prettify_item(item)

            if use_th:
                content += '<th>' + item + '</th>'
            else:
                content += '<td>' + item + '</td>'

        content += '</tr>\n'

    return content


def prettify_item(item):
    return PRETTIFY_NAMES.get(item, item)


def sysinfo_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    context = get_sysinfo()
    context.update(CONFIG)

    return [Template(TEMPLATE).safe_substitute(context)]


def usage():
    print('Usage: %s <ip>:<port>') % SCRIPT_NAME


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
