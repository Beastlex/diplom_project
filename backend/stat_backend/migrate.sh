#!/usr/bin/env bash

flask db migrate
flask db upgrade
