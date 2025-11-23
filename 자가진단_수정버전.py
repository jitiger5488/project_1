body_tem = inout("현재 체온을 입력해주세요  : ")    #body_temperature
if body_tem >38:
  print("독감 자가진단을 시작하겠습니다. (o/x)로 답해주십시오.")
  inf_sp = input("증상이 갑작스럽게 시작되었습니까?  : ")    #influenza_speed
  inf_incom = input("몸살, 오한 등 전신 불편감이 심하게 느껴지십니까?  :")    #influenza_incomfortable
  inf_tir = input("일상생활이 어려울 만큼 피로감이 심하십니까?  : ")    #influenza_tired
  inf_me = input("주변의 독감 확진자와 접촉하거나 독감이 유행하는 시기에 외부 활동이 많았습니까?  : ")    #influenza_meeting
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
  col_sp = input("증상이 서서히 진행되었습니까?  : ")    #cold_speed
  col_tir = input("평소보다 피곤하거나 컨디션이 떨어진 느낌이 있으십니까?  : ")    #cold_tired
  col_thr = input("목이 불편하거나 이물감이 느껴지십니까?  : ")    #cold_throat
  col_no = input("코막힘이나 콧물이 있으십니까?  : ")    #cold_nose
  col_me = input("최근 감기 증상을 가진 사람과 접촉한 적이 있으십니까?  : ")    #cold_meeting
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
    print("감기에 감염되었을 가능성이 낮습니다.")
else:
  print("알레르기 질환 자가진단을 시작하겠습니다. (o,x)로 답해주십시오.")
  al_env = input("특정 환경(야외, 동물 혹은 먼지가 많은 장소 등)에 노출되면 증상이 나타나십니까?  : ")    #allergy_environment
  al_sea = input("실내  공기나 계절 변화에 따라 증상이 반복되십니까?  : ")    #allergy_season
  al_fnd = input("최근 새로운 음식을 섭취하거나 약물을 복용하신 후 불편감이 생기겼습니까?  : ")    #allergy_Food N Drug
  al_cer = input("하루 중 특정 상황에만 증상이 심해지는 경향이 있으십니까?: ")    #allergy_certain
  al_fam = input("가족 중 알레르기 질환자가 있으십니까?  : ")    #allergy_family
  if al_env.lower() == 'o':
    al_env = 1
  else:
    al_env = 0
  if al_sea.lower() == 'o':
    al_sea = 1
  else:
    al_sea = 0
  if al_fnd.lower() == 'o':
    al_fnd = 1
  else:
    al_fnd = 0
  if al_cer.lower() == 'o':
    al_cer = 1
  else:
    al_cer = 0
  if al_fam.lower() == 'o':
    al_fam = 1
  else:
    al_fam = 0
  al_final = al_env +al_sea + al_fnd + al_cer + al_fam
  if al_final >= 3:
    print("알레르기 질환자이실 가능성이 높습니다. 공기청정,침구 세탁, 외출 후 세안 및 샤워를 통해 알레르기 유발 물질을 제거하십시오.")
  elif al_final < 3 and >= 1:
    print("알레르기 질환이 의심됩니다.실내 환경 관리에 신경쓰시길 바랍니다.")
  else:
    print("알레르기 가능성이 남습니다.")
print("소화불량 자가진단을 시작하겠습니다. (o/x)로 답해주십시오.")
di_ae = input("식사 이후 위나 배가 자주 불편하십니까?  : ")    #digestion_After Eating
di_cf = input("특정 음식(기름진 음식, 우유, 밀가루 등)을 섭취하면 증상이 악화되십니까?  : ")    #digerstion_Certain Food
di_st = input("스트레스 상황에서 소화 불편이 악화되십니까?  : ")    #digestion_stress
di_to = input("배변 습관(설사&변비)에 변화가 있으십니까?  : ")    #digestion_toilet
di_re = input("장기간 반복되는 소화 불편이 있으십니까?  : ")    # digestion_repeat
if di_ae.lower() == 'o':
  di_ae = 1
else:
  di_ae = 0
if di_cf.lower() == 'o':
  di_cf = 1
else:
  di_cf = 0
if di_st.lower() == 'o':
  di_st = 1
else:
  di_st = 0
if di_to.lower() == 'o':
  di_to = 1
else:
  di_to = 0
if di_re.lower() == 'o':
  di_re = 1
else:
  di_re = 0
di_final = di_ae + di_cf + di_st + di_to + di_re
if di_final >= 3:
  print("소화 장애가 있으실 가능성이 높습니다. 자극적인 음식 섭취를 줄이고 규칙적인 식사패턴과 적절한 식사량을 유지하세요.")
elif di_final < 3 and >= 1:
  print("경미한 소화 기능 저하가 의심됩니다. 규칙적인 식사패턴과 적절한 식사량을 유지하세요.")
else:
  print("소화 장애가 있으실 가능성이 낮습니다.")
