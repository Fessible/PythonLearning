# import os
# import platform
# import logging
#
# if platform.platform().startswith("Windows"):
#
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
#
# else:
#     print(os.getenv('HOME'))
#     logging_file = os.path.join(os.getenv('HOME'), 'test.log')
#
#
# print('Logging', logging_file)
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename=logging_file,
#     filemode='w'
# )
#
#
# logging.debug("Start of the program")
# logging.info("Doing something")
# logging.warning("Dying now")
#
#

import sys

print('you entered', len(sys.argv), 'arguments ...')
print('there were ', str(sys.argv))
