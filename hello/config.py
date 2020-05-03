SECRET_KEY = 'CHANGE_ME'
# database connection uri
import cx_Oracle
dsnStr = cx_Oracle.makedsn('gleb-bastion-us','1521','XEPDB1')
#SQLALCHEMY_DATABASE_URI = 'oracle://appdb:ShittyPassword01#@gleb-bastion-us/XEPDB1'
SQLALCHEMY_DATABASE_URI = 'oracle://appdb:UnfixableRelieve01#@' + dsnStr.replace('SID', 'SERVICE_NAME')
STATIC_ROOT = None


