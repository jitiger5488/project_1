#co = cough(기침) / tem = temperature(체온) / mu_pa = muscle pain(근육통) / nos = nose(콧물) / nos_n = 콧물_감기 / galae = 가래
print("바이러스 감염 자가진단 프로그램 시작하겠습니다.")
co = input("기침이 자주 나오십니까? (O/X)  :  ")
co = str(co)
if co.lower() == "o":
    tem = input("현재 체온을 입력해주세요 :  ")
    tem = float(tem)
    if tem >= 39:
        print("독감(인플루엔자) 감염이 의심됩니다. 추가 진단을 시작하겠습니다.")
        mu_pa = input("근육통이 있습니까? (O/X)  :  ")
        nos = input("콧물이 있습니까? (O/X)  :  ")
        mu_pa = str(mu_pa)
        nos = str(nos)
        if mu_pa.lower() == 'o' or nos.lower() == 'o':
            print('독감(인플루엔자)감염으로 예상됩니다.')
        elif mu_pa.lower() == 'x' and nos.lower() == 'x':
            print('병원에 가셔서 진료를 받으시길 바랍니다.')
    elif tem < 39 and tem >= 37.5:
        print("감기 바이러스 감염이 의심됩니다. 추가진단을 시작하겠습니다.")
        nos_n = input("콧물이 있습니까? (O/X)  :  ")
        galae = input("가래가 나옵니까? (O/X)  :  ")
        nos_n = str(nos_n)
        galae = str(galae)
        if nos_n.lower() == 'o' and galae.lower() == 'o':
            print('리노 바이러스 감염으로 예상됩니다.')
        elif nos_n.lower() == 'o' and galae.lower() != 'o':
            print('일반형 코로나 바이러스 감염으로 예상됩니다.')
    elif tem < 37.5:
        print('병원에 가셔서 진료를 받으시길 바랍니다.')
elif co.lower() == 'x':
    print('의심되는 감염병이 발견되지 않았습니다. 프로그램을 종료하겠습니다.')
