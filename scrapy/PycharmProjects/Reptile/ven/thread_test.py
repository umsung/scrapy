# import time,  threading
# from multiprocessing import Process,Pool
#
# balance = 0
# lock = threading.Lock()
# local_thread = threading.local()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# # 新线程执行的代码:
# def loop(n):
#     print('thread %s is running...' % threading.current_thread().name)
#     # n = 0
#     for i in range(5):
#         # n = n + 1
#         # lock.acquire()
#         # try:
#         change_it(n)
#         # finally:
#         #     lock.release()
#         print('thread %s >> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s is ended' % threading.current_thread().name)
#
#
# if __name__ == '__main__':
#
#     print('thread %s is runing...' % threading.current_thread().name)
#     # t = threading.Thread(target=loop, args=(6,), name='test_thread_name')
#     # t2 = threading.Thread(target=loop, args=(8,), name='test_thread_name2')
#     # t.start()
#     # t2.start()
#     #
#     # t.join()
#     # t2.join()
#     p = Pool(4)
#     for i in range(4):
#         p.apply_async(loop, args=(i,))
#     p.close()
#     p.join()
#     print('thread %s is ended' % threading.current_thread().name)
#     print(balance)
