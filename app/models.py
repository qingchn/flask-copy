#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by carlin.wang
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    password_hash = db.Column(db.String(128))
