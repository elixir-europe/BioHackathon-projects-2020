FROM npmjs/npm-docker-baseline:12-alpine

RUN npm install  npm install -g @ldf/server
RUN mkdir /config
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 5000


