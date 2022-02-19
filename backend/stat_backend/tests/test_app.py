#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.environ["DATABASE_ENGINE"] = "SQLITE"

from stat_backend.app import create_app

def test_first():
  assert True

def test_health():
  app = create_app()
  response = app.test_client().get("/api/healthz")
  assert response.status_code == 200
  assert response.data == b'"OK"\n'
