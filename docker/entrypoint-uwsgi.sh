#!/bin/sh

umask 0002

exec uwsgi \
  "--${DD_UWSGI_MODE}" "${DD_UWSGI_ENDPOINT}" \
  --protocol uwsgi \
  -b 32768 \
  --enable-threads \
  --processes 2 \
  --threads 2 \
  --wsgi dojo.wsgi:application \
  --socket-timeout 10800 \
  --http-timeout 10800 \
  --harakiri 10800
