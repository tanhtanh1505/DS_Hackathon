import numpy as np
import pandas as pd

def age(df):
  mapping_age = [
                df['bithYear'].between(0, 18),
                df['bithYear'].between(18, 24),
                df['bithYear'].between(24, 35),
                df['bithYear'].between(35, 45),
                df['bithYear'].between(45, 60),
                df['bithYear'].between(60, 110)
  ]
  values_age = [0,1,2,3,4,5]
  # values_age = ['<18','<24','<35','<45','<60','>60']
  df['bithYear'] = np.select(mapping_age,values_age,0)

def job_time(df):

  df['from_date'] = df['from_date'] + 1
  df['to_date'] = df['to_date'] + 1
  df['from_date'] = pd.to_datetime(df['from_date'], format='%Y%m%d')
  df['to_date'] = pd.to_datetime(df['to_date'], format='%Y%m%d')
  df['time_days'] =  df['to_date'] - df['from_date'];
  df['time_days'] =df['time_days'].astype(str)
  df['time_days'] = df['time_days'].str.replace(" days","")
  df['time_days'] =df['time_days'].astype(int)
  drop_field = [
              'from_date',
              'to_date'
              ]
  df.drop(columns=drop_field, inplace=True)
  mapping_time = [
                df['time_days'].between(0, 200),
                df['time_days'].between(200, 500),
                df['time_days'].between(500, 1000),
                df['time_days'].between(1000, 1500),
                df['time_days'].between(1500, 2000),
                df['time_days'].between(2500, 3500),
                df['time_days'].between(3500, 10000)
  ]
  values_time = [0,1,2,3,4,5,6]
  df['time_days'] = np.select(mapping_time,values_time,0)

def job(merged):
  #LDQL(Lãnh đạo, quản lý)
  #CMBC(Nhà chuyên môn bậc cao)
  #CMBT(Nhà chuyên môn bậc trung)
  #NV
  #LDNLT(Lao động có kỹ năng trong nông nghiệp, lâm nghiệp, thủy sản)
  #TVH(Thợ vận hành và lắp ráp máy móc, thiết bị)
  #LDGD(Lao động giản đơn)
  #LLVT(Lực lượng vũ trang)

  merged.loc[merged['job/role'].str.contains('chủ'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('phó'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('trưởng'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('giám đốc'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('giam đôc'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('cao cấp'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('quản lí'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('quản lý'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('quản đốc'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('cb'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('cán bộ'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('chính'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('chuyên gia'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('manager'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('supervisor'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('chief'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('chỉ huy'), 'job/role'] = 'CMBC'

  merged.loc[merged['job/role'].str.contains('chuyên viên'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('công nhân'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cong nhân'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('công nhan'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('công nhan'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cộng nhân'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cn'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cnhân'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('thợ'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cnkt'), 'job/role'] = 'LDGD' # cn??? regex
  merged.loc[merged['job/role'].str.contains('lao động phổ thông'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lao động'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lđ'),'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lđpt'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('nhân viên'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('nv'), 'job/role'] = 'NV'

  merged.loc[merged['job/role'].str.contains('chiến sỹ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('chiến sĩ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('bộ đội'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('quân sự'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('hạ sĩ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('hạ sỹ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('trung úy'), 'job/role'] = 'LLVT'

  merged.loc[merged['job/role'].str.contains('kỹ sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('kĩ sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('ky sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('ký sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('ky thuât'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('kỹ thuật'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('kĩ thuật'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('kỹ thuât'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('ky thuật'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('kỷ thuật'), 'job/role'] = 'CMBT'

  merged.loc[merged['job/role'].str.contains('cụng'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('lai xe'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lái xe'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('cán sự'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('cố vấn'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('công chức'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('cử nhân'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('học sinh'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('học viên'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('thạc sĩ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('thạc sỹ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('thực tập sinh'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('trung cấp'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('học'), 'job/role'] = 'CMBT'

  merged.loc[merged['job/role'].str.contains('trung sỹ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('trung sĩ'), 'job/role'] = 'LLVT'
  merged.loc[merged['job/role'].str.contains('kiểm lâm'), 'job/role'] = 'LDNLT'
  merged.loc[merged['job/role'].str.contains('thủy thủ'), 'job/role'] = 'LDNLT'
  merged.loc[merged['job/role'].str.contains('bác sĩ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('bác sỹ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('dược sĩ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('dược sỹ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('dược tá'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('hộ lý'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('hộ sinh'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('điều dưỡng'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('y tế'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('y sĩ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('y sỹ'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('giáo viên'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('gv'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('giảng viên'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('nghiên cứu viên'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('trợ giảng'), 'job/role'] = 'CMBC'

  merged.loc[merged['job/role'].str.contains('lao công'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('vệ sinh'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lđhđ'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lđpt'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lắp ráp'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('lễ tân'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('may'), 'job/role'] = 'LDGD'


  merged.loc[merged['job/role'].str.contains('kiến trúc sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('lập trình'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('ktv'), 'job/role'] = 'CMBC'

  merged.loc[merged['job/role'].str.contains('kiểm soát'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('kiểm sát'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('kiểm tra'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('kt'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('ks'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('ksv'), 'job/role'] = 'TVH'

  merged.loc[merged['job/role'].str.contains('giám sát'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('giam sat'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('gs'), 'job/role'] = 'TVH'
  merged.loc[merged['job/role'].str.contains('thư kí'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('thư ký'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('trợ lí'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('trợ lý'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('tiếp viên'), 'job/role'] = 'NV'

  merged.loc[merged['job/role'].str.contains('kế toán'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('kê toán'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('kiểm toán'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('thống kê'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('thủ kho'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('thủ quỹ'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('tài chính'), 'job/role'] = 'NV'


  merged.loc[merged['job/role'].str.contains('an ninh'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('bảo vệ'), 'job/role'] = 'LDGD'

  merged.loc[merged['job/role'].str.contains('biên tập'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('biên đạo'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('diễn viên'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('họa sĩ'), 'job/role'] = 'LDGD'

  merged.loc[merged['job/role'].str.contains('bí thư'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('ủy viên'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('thường trực'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('thường vụ'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('tư pháp'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('chánh'), 'job/role'] = 'LDQL' # noise
  merged.loc[merged['job/role'].str.contains('chấp hành viên'), 'job/role'] = 'LDQL' # noise

  merged.loc[merged['job/role'].str.contains('thẩm phán'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('thẩm tra'), 'job/role'] = 'LDQL'
  merged.loc[merged['job/role'].str.contains('thẩm định'), 'job/role'] = 'LDQL'

  merged.loc[merged['job/role'].str.contains('bán hàng'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('bưu tá'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('kỹ sư'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('kỹ thuật'), 'job/role'] = 'CMBC'

  merged.loc[merged['job/role'].str.contains('bếp'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('bốc'), 'job/role'] = 'LDGD'

  merged.loc[merged['job/role'].str.contains('bộ phận'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('consultant'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('marketing'), 'job/role'] = 'NV'

  merged.loc[merged['job/role'].str.contains('huấn luyện viên'), 'job/role'] = 'CMBT'
  merged.loc[merged['job/role'].str.contains('hành chính'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('hướng dẫn viên'), 'job/role'] = 'NV'

  merged.loc[merged['job/role'].str.contains('hỗ trợ'), 'job/role'] = 'NVBT'

  merged.loc[merged['job/role'].str.contains('nghỉ'), 'job/role'] = 'NA'
  merged.loc[merged['job/role'].str.contains('ngừng việc'), 'job/role'] = 'NA'
  merged.loc[merged['job/role'].str.contains('na'), 'job/role'] = 'NA'
  merged.loc[merged['job/role'].str.contains('thư viện'), 'job/role'] = 'NV'

  merged.loc[merged['job/role'].str.contains('tư vấn'), 'job/role'] = 'NVBT'
  merged.loc[merged['job/role'].str.contains('tạp vụ'), 'job/role'] = 'NV'
  merged.loc[merged['job/role'].str.contains('tập sự'), 'job/role'] = 'LDGD'
  merged.loc[merged['job/role'].str.contains('vh'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('vận hành'), 'job/role'] = 'CMBC'
  merged.loc[merged['job/role'].str.contains('viên chức'), 'job/role'] = 'LDQL'

  return merged