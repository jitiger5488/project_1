body_tem = inout("현재 체온을 입력해주세요  : ")
if body_tem >38:
  print("독감 자가진단을 시작하겠습니다. (o/x)로 답해주십시오.")
  inf_sp = input("증상이 갑작스럽게 시작되었습니까?  : ")
  inf_incom = input("몸살, 오한 등 전신 불편감이 심하게 느껴지십니까?  :")
  inf_tir = input("일상생활이 어려울 만큼 피로감이 심하십니까?  : ")
  inf_me = input("주변의 독감 확진자와 접촉하거나 독감이 유행하는 시기에 외부 활동이 많았습니까?  : ")
  if inf_sp.lower() == 'o':
      inf_sp = 1
  else:
      inf_sp = 0
  if inf_incom.lower() == 'o':
    inf_incom = 1
  else:
    inf_incom = 0
  if inf_tir.lower() == 'o':
    inf_tir = 1
  else:
    inf_tir = 0
  if inf_me.lower() == 'o':
    inf_me = 1
  else:
    inf_me = 0
  inf_final = inf_sp + inf_incom + inf_tir + inf_me + 1
  if inf_final >= 4:
    print("독감에 감염되었을 가능성이 매우 높습니다. 전문 의료기관에서 진료를 받으시길 바랍니다.")
  elif inf_final < 4 and >= 2:
    print('독감에 감염되었을 가능성이 있습니다.기침예절 준수 및 손 위생 관리에 신경쓰시길 바랍니다.")
  else:
    print("독감에 감염되었을 가능성이 낮습니다.")
elif body_tem <= 38 and >= 37:
  print("감기 자가진단을 시작하겠습니다. (o/x)로 답해주십시오.")
  col_sp = input("증상이 서서히 진행되었습니까?  : ")
  col_tir = input("평소보다 피곤하거나 컨디션이 떨어진 느낌이 있으십니까?  : ")
  col_thr = input("목이 불편하거나 이물감이 느껴지십니까?  : ")
  col_no = input("코막힘이나 콧물이 있으십니까?  : ")
  col_me = input("최근 감기 증상을 가진 사람과 접촉한 적이 있으십니까?  : ")
  if col_sp.lower() == 'o':
    col_sp = 1
  else:
    col_sp = 0
  if col_tir.lower() == 'o':
    col_tir = 1
  else:
    col_tir = 0
  if col_thr.lower() == 'o':
    col_thr = 1
  else:
    col_thr = 0
  if col_no.lower() == 'o':
    col_no = 1
  else:
    col_no = 0
  if col_me.lower() == 'o':
    col_me = 1
  else:
    col_me = 0
  col_final = col_sp + col_tir + col_thr + col_no + col_me + 1
  if col_final >= 3:
    print("감기에 감염되었을 가능성이 높습니다. 손 위생 관리와 적절한 수면&영양 섭취를 유지하시길 바랍니다.")
  elif col_final < 3 and >= 1:
    print("감기 초기 단계 혹은 일반적인 호흡기 불편 증상일 가능성이 있습니다.")
  else:
    print("감기에 감염되었을 가능성이 낮습니다.)
