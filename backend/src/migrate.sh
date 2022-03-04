#!/bin/sh

env_var=${NODE_ENV:-"production"}

if [ "$env_var" = production ]
then
  ./wait-for.sh db:$POSTGRES_PORT -- npx sequelize db:migrate
fi

if [ "$env_var" = test ]
then
  npx sequelize-cli db:migrate
  npx sequelize-cli db:seed:all
fi
