import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/administrador/repo_siro/siro-robot/install/modelo_robot'
