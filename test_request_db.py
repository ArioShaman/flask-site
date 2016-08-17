#!/usr/bin/env python
from app import models

u = models.User.query.all()
print u

for i in u:
	role = 'user'
	if i.role == 1:
		role = 'admin'
	print 'id:',i.id,'  name:',i.nickname,'  role:',role