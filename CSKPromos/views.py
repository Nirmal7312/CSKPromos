from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'index.html')
    return render(request, 'index.html')

def yearselect(request, wyear):
    if wyear == 2023:
        file = 'year2023.html'
        cards = []
        name = [
            '#SHORON #GAMEON',
            'AB TAYIYAARI SHURU KIJIYE',
            'Mai kya kar Raha hoon?',
            'YAHA EK NAHI DAS SHER HAI',
            'YELLOW JERSEY IS COMING BACK!',
            'Kela nahi peda,paneer aur Puri khaiye!',
            'Sawal ke Saath Dhamal bhi hoga! ',
            'AB INTERVIEW ENGLISH MEIN BHI HOGA',
            'csk phir dahadega',
            'kyo csk pahele match mein haara',
            'Kya Chennai Chepauk mein 4 saal ke baad jeetkar 2023 season mein pahela match Jeet payegi?',
            'CSK NE CHEPAUK MEIN SHOR MACHAYA',
            'CSK KO CHAHIYE STRATIGY',
            'CSKvsRR KI TAYIYAARI, RINKU PADE GT PAR BHAARI, DHAWAN RUKE 99 PAR NOT OUT(PART1)',
            'CSKvsRR KI TAYIYAARI, RINKU PADE GT PAR BHAARI, DHAWAN RUKE 99 PAR NOT OUT(PART2)',
            'RCB WAALO CSK AA RAHA HAI CHINNASWAMI MEIN KEHER BARSANE',
            'TAIYAAR HO JAAYO HYDRABAD, CSK APNE GUFA MEIN DAHHADNE WALA HAI',
            'WHISTLEPODU EDEN GARDENS MEIN DAHAADNE  AA RAHA HAI',
            'CSK CHEPAUK MEIN PUNJAB KE SAMNE PHIR DAHAADEGA',
            'LUCKNOW TAYIYAAR RAHNA CSK DAHADNE AA RAHA HAI',
            'MI WAALO CSK APNE GHAR MEIN DAHADEGA',
            'DC WAALO CSK APNE GHAR MEIN DAHADEGA',
            'KKR WAALO CSK APNE GHAR MEIN DAHADEGA',
            'DC WAALO CSK TUMHARE GHAR MEIN DAHADEGA',
            'GT WAALO CSK APNE GHAR MEIN DAHADEGA',
            'Thanks! CSK won 2023!'
        ]
        for i in range(26):
            cards.append(name[i])
            i += 1

        # details.append([cards, name])
        params = {'cards':cards}

    elif wyear == 2024:
        file = 'year2024.html'
        cards = []
        name = [
            'IPL2024 ke liye #TayiyaariShuruKijiye',
            'CSK Strongest Playing XI of IPL2024',
            'Schedule Launched!',
            'Ready for the RCB challenge!',
            'Interview with Nirmal!',
            'CSK new jersey!',
            'GT ke liye hai tayiyaar',
            'DC WAALO CSK JOR SE DAHADEGA',
            'Ready for KKR challenge!',
            'Ready for MI challenge!',
            'Ready for LSG challenge!',
            'csk lsg ke saamne kyo haara'
        ]
        for i in range(12):
            cards.append(name[i])
            i += 1

        params = {'cards':cards}

    elif wyear == 2025:
        file = 'year2025.html'
        cards = []
        name = [
            '#TheHistoryWillRepeatAgain!',
            'IPL 2025 RULES ANNOUNCED!',
            'Retaintion list hai aayi CSK ki kya hogi kharidayi part1',
            'Retaintion list hai aayi CSK ki kya hogi kharidayi part2',
            'CSK 2025 Best XI',
            'Mahi Laaye Tabahi Song',
            'EL Classico 23rd',
            'CSK vs MI Squad Comparison',
            'important updates csk ipl 2025',
            'CSK vs MI 23rd march ',
            'Podcast Ft.Aman',
            'CSK vs MI FinalPrediction',
            'Tayiyaar Raho RCB, Tum Sher ki Gufa mein AA rahe ho!',
            'How can CSK defeat RR in Assam',
            'We will comeback!',
            'DC WAALO CSK APNE GHAR MEIN DAHADEGA',
            'PBKS Tayiyaar Raho, CSK Tumhe Harane aa Raha Hai'
        ]
        for i in range(17):
            cards.append(name[i])
            i += 1

        params = {'cards':cards}
    return render(request, file, params)



def video2023(request, fc):
    video_ids = {
        1: '1WNt2l5AYcfRnbAjGlK31QvDHwJJcuBK9',
        2: '13aEmKpTV_4Jk9CvvAqmpDM_dfqYq_DYH',
        3: '12t2m1Jv3J2iBG4A6c6PoDH3wjaI53Yhi',
        4: '1HUMYDnYexXIJ7CiLOGDjJRNb95Ip6ST3',
        5: '1yflfcWRc3vG2lSeNVz7b9J8exFFCFwvW',
        6: '13DrsIrWRBz_J2bjldE3KdMpJqo8fYUfa',
        7: '1cEVaxrM_zcOFgoVR_HEBTHyX9ClZagDx',
        8: '1IHGnpvWZGzQtPxad-Bx1OizU9od25jNg',
        9: '1BfNMcmeyQxXNXKQgkX-Br10Ok-o5aHGF',
        10: '1YLDiZpMtucXxzJKvCv9ZRVwG3-yPxA4f',
        11: '15nEMTiwdqflVyIK254KpRXHHXY6FSXi4',
        12: '1GneTFBsjGH2uvyToqeLVDl6aSLKpHkb8',
        13: '1Hrq_jjilKs5LL8jZMN3DBG1RdcLd2LhG',
        14: '1QNHU-YnMmSvcFLkGIgjIADnVt1jTK_pA',
        15: '1ABKFZXno6wI6ThUQrpFIPHV-cutu0ipl',
        16: '1mvb8ApP6KF9EIA82z-DAoeVWQCUYq7fb',
        17: '13UqzqlJK-OXRkpCY8o3Vv5IqXEQlvT3Y',
        18: '19qwmd7e_uhUIUBfQyu0EkYSJ1uqrUnif',
        19: '1gPnXC8IAcS436AFYi695gU5ONT4lrF98',
        20: '1dyBnSpqNRpnLRRQCKURNNV7u3owHLErX',
        21: '1J7Of-PDpCJzXEVLRS1jroBF7n2AETqEK',
        22: '1gnxT0025lzZOU7Kcqj9hqrttxt77TZL5',
        23: '1AW5kqfZ4QDBLiwYxP4f9XJqjBAgLkioF',
        24: '1tbbUAgTbs3uzvEqm4oCEz-VtjaeY9g61',
        25: '14xq_gJ4lGxjqSDsd5PLBDt1qC8hn8W7N',
        26: '1BU0TdETLmRt-7bzETs_Wgd4Cg2sb8hja',
    }

    if fc in video_ids:
        params = {'vid_ids': video_ids[fc]}
    return render(request, 'video2023.html', params)

def video2024(request, fc):
    video_ids = {
        1: '1Se9KrlW31AppESonBSrMf5gl8RfjA2Wy',
        2: '1XfUJ3E8C_I_QxFs2c4XMzcIA5daNFsdL',
        3: '1Lo4XRsYY-F1S7uqzYRdIyruKbGkZ-k6p',
        4: '1RR_kS6PaZXNprxqu0mRwohOhIbTXeKyT',
        5: '1QrBXy6TB_imoUrpjO0Zs78q5ioZ2KZNT',
        6: '1P0U-zEmk2fYCz8sH1-P68GmtUWqhmVRp',
        7: '1SJubXJhndwzOCVh9M5U5pmmPNhDrr1Of',
        8: '1Pj_X7VxR-tJ0xgsQ5-XLcQIVBnUDeVQn',
        9: '1vBeR1yNueASf-BWweO3Jae8cQe2eW1Yj',
        10: '1_2UBH6ZyZoYoWUHSzbxQWCFhpUmQNpSx',
        11: '13NJU-Kyw9m0JGWUbLt_KyAdM3F_qxv9p',
        12: '18ZQZIoS9ZtbjpjRUck4xijmcTWRnSRGI',
    }

    if fc in video_ids:
        params = {'vid_ids': video_ids[fc]}
    return render(request, 'video2024.html', params)

def video2025(request, fc):
    video_ids = {
        1: '1NInS6Pp04de9Zh7iFqDRsaMAvu2RUYmO',
        2: '1Yq6lwXJsAHNnwhgY1RHDvu0SPZKhRD-j',
        3: '1hkorjp2fxQjSHSx2XjkuKR9ZhdimeJI8',
        4: '1WEWSsrL4GQe7ttf7ZuF5J4iDpSCuAqeP',
        5: '12jXjx7IEbJVEfLAtTxYPklhda61CFuzW',
        6: '1jpor2RGLyzaCStkS_34VeJoks7ZnTDNg',
        7: '1IcYz1BXVTWJmlOnCz1kzPQRhhvOxgYYE',
        8: '1jhG_j8T01_9zt4QBt6_sdRCUDuj3XjaF',
        9: '1yO2r5U7zEnQgqUZ-f5X1ea5igt6Gwdi9',
        10: '1SELm14rzHanaIFtNPjT8Q6mZhEG6kkMV',
        11: '11jKZ_N15RX7pXALTIvlFu0afEEmXj-Ah',
        12: '1qY074vRaqjggAhHv9LoFNMI5QR2XA5aC',
        13: '1jD9kKJ3QT_hgsseHeg6P1vlhvbjw9ZoM',
        14: '1rQm_hJPTN22PaqDb55qjCfN8KCeOeDG1',
        15: '1hdiW3dKpaSMKwFu7_YiKUKvRAXWzaoxW',
        16: '1e7quO3fTj9j6s9mF8ZLaFWEcH4BRUou1',
        17: '1sG0uJpNA-evVjOH9Ec31shcIMAbc7GKw',
    }

    if fc in video_ids:
        params = {'vid_ids': video_ids[fc]}
    return render(request, 'video2025.html', params)