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
  --socket-timeout 86400 \
  --http-timeout 86400 \
  --harakiri 86400
