# # ��ȡ������֤�����ҳ
#   imgelement = driver.find_element_by_xpath('//a[@id="yzm_top"]/img')
#   #  ��λ��֤��
#   location = imgelement.location
#   #  ��ȡ��֤��x,y������
#   size = imgelement.size
#   #  ��ȡ��֤��ĳ���
#   rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
#   #  д��������Ҫ��ȡ��λ������
#   i = Image.open(file_path+'temp.png')
#   #  �򿪽�ͼ
#   frame = i.crop(rangle)
#   #  ʹ��Image��crop�������ӽ�ͼ���ٴν�ȡ������Ҫ������
#   frame.save('temp2.png')
#
#
# # ������д���·���ȡ���ݵ�ʱ�� ��д��ȡ�����·ݼӼ����������ͦ���ã� ��ʱ������ �������
# import datetime
# from dateutil.relativedelta import relativedelta
# print(datetime.date.today()+ relativedelta(months=-1))   # ����monthsΪ����ʾǰһ���£� monthsΪ����ʾ��һ����
#
