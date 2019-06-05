import pymysql

# 由于python3 版本中mysql模块改了模块名为pymysql，所以要声明pymysql模块，就是MySQLdb
pymysql.install_as_MySQLdb()