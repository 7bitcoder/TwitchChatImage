import sys
from PIL import Image, ImageFilter


def getchar(T):
    if (T == (0,0,0,0,0,0,0,0)):
        return u'\u2880'
    elif (T == (0,0,0,0,0,0,0,1)):
        return u'\u2880'
    elif (T == (0,0,0,0,0,0,1,0)):
        return u'\u2840'
    elif (T == (0,0,0,0,0,0,1,1)):
        return u'\u28C0'
    elif (T == (0,0,0,0,0,1,0,0)):
        return u'\u2820'
    elif (T == (0,0,0,0,0,1,0,1)):
        return u'\u28A0'
    elif (T == (0,0,0,0,0,1,1,0)):
        return u'\u2860'
    elif (T == (0,0,0,0,0,1,1,1)):
        return u'\u28E0'
    elif (T == (0,0,0,0,1,0,0,0)):
        return u'\u2804'
    elif (T == (0,0,0,0,1,0,0,1)):
        return u'\u2884'
    elif (T == (0,0,0,0,1,0,1,0)):
        return u'\u2844'
    elif (T == (0,0,0,0,1,0,1,1)):
        return u'\u28C4'
    elif (T == (0,0,0,0,1,1,0,0)):
        return u'\u2824'
    elif (T == (0,0,0,0,1,1,0,1)):
        return u'\u28A4'
    elif (T == (0,0,0,0,1,1,1,0)):
        return u'\u2864'
    elif (T == (0,0,0,0,1,1,1,1)):
        return u'\u28E4'
    elif (T == (0,0,0,1,0,0,0,0)):
        return u'\u2810'
    elif (T == (0,0,0,1,0,0,0,1)):
        return u'\u2890'
    elif (T == (0,0,0,1,0,0,1,0)):
        return u'\u2850'
    elif (T == (0,0,0,1,0,0,1,1)):
        return u'\u28D0'
    elif (T == (0,0,0,1,0,1,0,0)):
        return u'\u2830'
    elif (T == (0,0,0,1,0,1,0,1)):
        return u'\u28B0'
    elif (T == (0,0,0,1,0,1,1,0)):
        return u'\u2870'
    elif (T == (0,0,0,1,0,1,1,1)):
        return u'\u28F0'
    elif (T == (0,0,0,1,1,0,0,0)):
        return u'\u2814'
    elif (T == (0,0,0,1,1,0,0,1)):
        return u'\u2894'
    elif (T == (0,0,0,1,1,0,1,0)):
        return u'\u2854'
    elif (T == (0,0,0,1,1,0,1,1)):
        return u'\u28D4'
    elif (T == (0,0,0,1,1,1,0,0)):
        return u'\u2834'
    elif (T == (0,0,0,1,1,1,0,1)):
        return u'\u28B4'
    elif (T == (0,0,0,1,1,1,1,0)):
        return u'\u2874'
    elif (T == (0,0,0,1,1,1,1,1)):
        return u'\u28F4'
    elif (T == (0,0,1,0,0,0,0,0)):
        return u'\u2802'
    elif (T == (0,0,1,0,0,0,0,1)):
        return u'\u2882'
    elif (T == (0,0,1,0,0,0,1,0)):
        return u'\u2842'
    elif (T == (0,0,1,0,0,0,1,1)):
        return u'\u28C2'
    elif (T == (0,0,1,0,0,1,0,0)):
        return u'\u2822'
    elif (T == (0,0,1,0,0,1,0,1)):
        return u'\u28A2'
    elif (T == (0,0,1,0,0,1,1,0)):
        return u'\u2862'
    elif (T == (0,0,1,0,0,1,1,1)):
        return u'\u28E2'
    elif (T == (0,0,1,0,1,0,0,0)):
        return u'\u2806'
    elif (T == (0,0,1,0,1,0,0,1)):
        return u'\u2886'
    elif (T == (0,0,1,0,1,0,1,0)):
        return u'\u2846'
    elif (T == (0,0,1,0,1,0,1,1)):
        return u'\u28C6'
    elif (T == (0,0,1,0,1,1,0,0)):
        return u'\u2826'
    elif (T == (0,0,1,0,1,1,0,1)):
        return u'\u28A6'
    elif (T == (0,0,1,0,1,1,1,0)):
        return u'\u2866'
    elif (T == (0,0,1,0,1,1,1,1)):
        return u'\u28E6'
    elif (T == (0,0,1,1,0,0,0,0)):
        return u'\u2812'
    elif (T == (0,0,1,1,0,0,0,1)):
        return u'\u2892'
    elif (T == (0,0,1,1,0,0,1,0)):
        return u'\u2852'
    elif (T == (0,0,1,1,0,0,1,1)):
        return u'\u28D2'
    elif (T == (0,0,1,1,0,1,0,0)):
        return u'\u2832'
    elif (T == (0,0,1,1,0,1,0,1)):
        return u'\u28B2'
    elif (T == (0,0,1,1,0,1,1,0)):
        return u'\u2872'
    elif (T == (0,0,1,1,0,1,1,1)):
        return u'\u28F2'
    elif (T == (0,0,1,1,1,0,0,0)):
        return u'\u2816'
    elif (T == (0,0,1,1,1,0,0,1)):
        return u'\u2896'
    elif (T == (0,0,1,1,1,0,1,0)):
        return u'\u2856'
    elif (T == (0,0,1,1,1,0,1,1)):
        return u'\u28D6'
    elif (T == (0,0,1,1,1,1,0,0)):
        return u'\u2836'
    elif (T == (0,0,1,1,1,1,0,1)):
        return u'\u28B6'
    elif (T == (0,0,1,1,1,1,1,0)):
        return u'\u2876'
    elif (T == (0,0,1,1,1,1,1,1)):
        return u'\u28F6'
    elif (T == (0,1,0,0,0,0,0,0)):
        return u'\u2808'
    elif (T == (0,1,0,0,0,0,0,1)):
        return u'\u2888'
    elif (T == (0,1,0,0,0,0,1,0)):
        return u'\u2848'
    elif (T == (0,1,0,0,0,0,1,1)):
        return u'\u28C8'
    elif (T == (0,1,0,0,0,1,0,0)):
        return u'\u2828'
    elif (T == (0,1,0,0,0,1,0,1)):
        return u'\u28A8'
    elif (T == (0,1,0,0,0,1,1,0)):
        return u'\u2868'
    elif (T == (0,1,0,0,0,1,1,1)):
        return u'\u28E8'
    elif (T == (0,1,0,0,1,0,0,0)):
        return u'\u280C'
    elif (T == (0,1,0,0,1,0,0,1)):
        return u'\u288C'
    elif (T == (0,1,0,0,1,0,1,0)):
        return u'\u284C'
    elif (T == (0,1,0,0,1,0,1,1)):
        return u'\u28CC'
    elif (T == (0,1,0,0,1,1,0,0)):
        return u'\u282C'
    elif (T == (0,1,0,0,1,1,0,1)):
        return u'\u28AC'
    elif (T == (0,1,0,0,1,1,1,0)):
        return u'\u286C'
    elif (T == (0,1,0,0,1,1,1,1)):
        return u'\u28EC'
    elif (T == (0,1,0,1,0,0,0,0)):
        return u'\u2818'
    elif (T == (0,1,0,1,0,0,0,1)):
        return u'\u2898'
    elif (T == (0,1,0,1,0,0,1,0)):
        return u'\u2858'
    elif (T == (0,1,0,1,0,0,1,1)):
        return u'\u28D8'
    elif (T == (0,1,0,1,0,1,0,0)):
        return u'\u2838'
    elif (T == (0,1,0,1,0,1,0,1)):
        return u'\u28B8'
    elif (T == (0,1,0,1,0,1,1,0)):
        return u'\u2878'
    elif (T == (0,1,0,1,0,1,1,1)):
        return u'\u28F8'
    elif (T == (0,1,0,1,1,0,0,0)):
        return u'\u281C'
    elif (T == (0,1,0,1,1,0,0,1)):
        return u'\u289C'
    elif (T == (0,1,0,1,1,0,1,0)):
        return u'\u285C'
    elif (T == (0,1,0,1,1,0,1,1)):
        return u'\u28DC'
    elif (T == (0,1,0,1,1,1,0,0)):
        return u'\u283C'
    elif (T == (0,1,0,1,1,1,0,1)):
        return u'\u28BC'
    elif (T == (0,1,0,1,1,1,1,0)):
        return u'\u287C'
    elif (T == (0,1,0,1,1,1,1,1)):
        return u'\u28FC'
    elif (T == (0,1,1,0,0,0,0,0)):
        return u'\u280A'
    elif (T == (0,1,1,0,0,0,0,1)):
        return u'\u288A'
    elif (T == (0,1,1,0,0,0,1,0)):
        return u'\u284A'
    elif (T == (0,1,1,0,0,0,1,1)):
        return u'\u28CA'
    elif (T == (0,1,1,0,0,1,0,0)):
        return u'\u282A'
    elif (T == (0,1,1,0,0,1,0,1)):
        return u'\u28AA'
    elif (T == (0,1,1,0,0,1,1,0)):
        return u'\u286A'
    elif (T == (0,1,1,0,0,1,1,1)):
        return u'\u28EA'
    elif (T == (0,1,1,0,1,0,0,0)):
        return u'\u280E'
    elif (T == (0,1,1,0,1,0,0,1)):
        return u'\u288E'
    elif (T == (0,1,1,0,1,0,1,0)):
        return u'\u284E'
    elif (T == (0,1,1,0,1,0,1,1)):
        return u'\u28CE'
    elif (T == (0,1,1,0,1,1,0,0)):
        return u'\u282E'
    elif (T == (0,1,1,0,1,1,0,1)):
        return u'\u28AE'
    elif (T == (0,1,1,0,1,1,1,0)):
        return u'\u286E'
    elif (T == (0,1,1,0,1,1,1,1)):
        return u'\u28EE'
    elif (T == (0,1,1,1,0,0,0,0)):
        return u'\u281A'
    elif (T == (0,1,1,1,0,0,0,1)):
        return u'\u289A'
    elif (T == (0,1,1,1,0,0,1,0)):
        return u'\u285A'
    elif (T == (0,1,1,1,0,0,1,1)):
        return u'\u28DA'
    elif (T == (0,1,1,1,0,1,0,0)):
        return u'\u283A'
    elif (T == (0,1,1,1,0,1,0,1)):
        return u'\u28BA'
    elif (T == (0,1,1,1,0,1,1,0)):
        return u'\u287A'
    elif (T == (0,1,1,1,0,1,1,1)):
        return u'\u28FA'
    elif (T == (0,1,1,1,1,0,0,0)):
        return u'\u281E'
    elif (T == (0,1,1,1,1,0,0,1)):
        return u'\u289E'
    elif (T == (0,1,1,1,1,0,1,0)):
        return u'\u285E'
    elif (T == (0,1,1,1,1,0,1,1)):
        return u'\u28DE'
    elif (T == (0,1,1,1,1,1,0,0)):
        return u'\u283E'
    elif (T == (0,1,1,1,1,1,0,1)):
        return u'\u28BE'
    elif (T == (0,1,1,1,1,1,1,0)):
        return u'\u287E'
    elif (T == (0,1,1,1,1,1,1,1)):
        return u'\u28FE'
    elif (T == (1,0,0,0,0,0,0,0)):
        return u'\u2801'
    elif (T == (1,0,0,0,0,0,0,1)):
        return u'\u2881'
    elif (T == (1,0,0,0,0,0,1,0)):
        return u'\u2841'
    elif (T == (1,0,0,0,0,0,1,1)):
        return u'\u28C1'
    elif (T == (1,0,0,0,0,1,0,0)):
        return u'\u2821'
    elif (T == (1,0,0,0,0,1,0,1)):
        return u'\u28A1'
    elif (T == (1,0,0,0,0,1,1,0)):
        return u'\u2861'
    elif (T == (1,0,0,0,0,1,1,1)):
        return u'\u28E1'
    elif (T == (1,0,0,0,1,0,0,0)):
        return u'\u2805'
    elif (T == (1,0,0,0,1,0,0,1)):
        return u'\u2885'
    elif (T == (1,0,0,0,1,0,1,0)):
        return u'\u2845'
    elif (T == (1,0,0,0,1,0,1,1)):
        return u'\u28C5'
    elif (T == (1,0,0,0,1,1,0,0)):
        return u'\u2825'
    elif (T == (1,0,0,0,1,1,0,1)):
        return u'\u28A5'
    elif (T == (1,0,0,0,1,1,1,0)):
        return u'\u2865'
    elif (T == (1,0,0,0,1,1,1,1)):
        return u'\u28E5'
    elif (T == (1,0,0,1,0,0,0,0)):
        return u'\u2811'
    elif (T == (1,0,0,1,0,0,0,1)):
        return u'\u2891'
    elif (T == (1,0,0,1,0,0,1,0)):
        return u'\u2851'
    elif (T == (1,0,0,1,0,0,1,1)):
        return u'\u28D1'
    elif (T == (1,0,0,1,0,1,0,0)):
        return u'\u2831'
    elif (T == (1,0,0,1,0,1,0,1)):
        return u'\u28B1'
    elif (T == (1,0,0,1,0,1,1,0)):
        return u'\u2871'
    elif (T == (1,0,0,1,0,1,1,1)):
        return u'\u28F1'
    elif (T == (1,0,0,1,1,0,0,0)):
        return u'\u2815'
    elif (T == (1,0,0,1,1,0,0,1)):
        return u'\u2895'
    elif (T == (1,0,0,1,1,0,1,0)):
        return u'\u2855'
    elif (T == (1,0,0,1,1,0,1,1)):
        return u'\u28D5'
    elif (T == (1,0,0,1,1,1,0,0)):
        return u'\u2835'
    elif (T == (1,0,0,1,1,1,0,1)):
        return u'\u28B5'
    elif (T == (1,0,0,1,1,1,1,0)):
        return u'\u2875'
    elif (T == (1,0,0,1,1,1,1,1)):
        return u'\u28F5'
    elif (T == (1,0,1,0,0,0,0,0)):
        return u'\u2803'
    elif (T == (1,0,1,0,0,0,0,1)):
        return u'\u2883'
    elif (T == (1,0,1,0,0,0,1,0)):
        return u'\u2843'
    elif (T == (1,0,1,0,0,0,1,1)):
        return u'\u28C3'
    elif (T == (1,0,1,0,0,1,0,0)):
        return u'\u2823'
    elif (T == (1,0,1,0,0,1,0,1)):
        return u'\u28A3'
    elif (T == (1,0,1,0,0,1,1,0)):
        return u'\u2863'
    elif (T == (1,0,1,0,0,1,1,1)):
        return u'\u28E3'
    elif (T == (1,0,1,0,1,0,0,0)):
        return u'\u2807'
    elif (T == (1,0,1,0,1,0,0,1)):
        return u'\u2887'
    elif (T == (1,0,1,0,1,0,1,0)):
        return u'\u2847'
    elif (T == (1,0,1,0,1,0,1,1)):
        return u'\u28C7'
    elif (T == (1,0,1,0,1,1,0,0)):
        return u'\u2827'
    elif (T == (1,0,1,0,1,1,0,1)):
        return u'\u28A7'
    elif (T == (1,0,1,0,1,1,1,0)):
        return u'\u2867'
    elif (T == (1,0,1,0,1,1,1,1)):
        return u'\u28E7'
    elif (T == (1,0,1,1,0,0,0,0)):
        return u'\u2813'
    elif (T == (1,0,1,1,0,0,0,1)):
        return u'\u2893'
    elif (T == (1,0,1,1,0,0,1,0)):
        return u'\u2853'
    elif (T == (1,0,1,1,0,0,1,1)):
        return u'\u28D3'
    elif (T == (1,0,1,1,0,1,0,0)):
        return u'\u2833'
    elif (T == (1,0,1,1,0,1,0,1)):
        return u'\u28B3'
    elif (T == (1,0,1,1,0,1,1,0)):
        return u'\u2873'
    elif (T == (1,0,1,1,0,1,1,1)):
        return u'\u28F3'
    elif (T == (1,0,1,1,1,0,0,0)):
        return u'\u2817'
    elif (T == (1,0,1,1,1,0,0,1)):
        return u'\u2897'
    elif (T == (1,0,1,1,1,0,1,0)):
        return u'\u2857'
    elif (T == (1,0,1,1,1,0,1,1)):
        return u'\u28D7'
    elif (T == (1,0,1,1,1,1,0,0)):
        return u'\u2837'
    elif (T == (1,0,1,1,1,1,0,1)):
        return u'\u28B7'
    elif (T == (1,0,1,1,1,1,1,0)):
        return u'\u2877'
    elif (T == (1,0,1,1,1,1,1,1)):
        return u'\u28F7'
    elif (T == (1,1,0,0,0,0,0,0)):
        return u'\u2809'
    elif (T == (1,1,0,0,0,0,0,1)):
        return u'\u2889'
    elif (T == (1,1,0,0,0,0,1,0)):
        return u'\u2849'
    elif (T == (1,1,0,0,0,0,1,1)):
        return u'\u28C9'
    elif (T == (1,1,0,0,0,1,0,0)):
        return u'\u2829'
    elif (T == (1,1,0,0,0,1,0,1)):
        return u'\u28A9'
    elif (T == (1,1,0,0,0,1,1,0)):
        return u'\u2869'
    elif (T == (1,1,0,0,0,1,1,1)):
        return u'\u28E9'
    elif (T == (1,1,0,0,1,0,0,0)):
        return u'\u280D'
    elif (T == (1,1,0,0,1,0,0,1)):
        return u'\u288D'
    elif (T == (1,1,0,0,1,0,1,0)):
        return u'\u284D'
    elif (T == (1,1,0,0,1,0,1,1)):
        return u'\u28CD'
    elif (T == (1,1,0,0,1,1,0,0)):
        return u'\u282D'
    elif (T == (1,1,0,0,1,1,0,1)):
        return u'\u28AD'
    elif (T == (1,1,0,0,1,1,1,0)):
        return u'\u286D'
    elif (T == (1,1,0,0,1,1,1,1)):
        return u'\u28ED'
    elif (T == (1,1,0,1,0,0,0,0)):
        return u'\u2819'
    elif (T == (1,1,0,1,0,0,0,1)):
        return u'\u2899'
    elif (T == (1,1,0,1,0,0,1,0)):
        return u'\u2859'
    elif (T == (1,1,0,1,0,0,1,1)):
        return u'\u28D9'
    elif (T == (1,1,0,1,0,1,0,0)):
        return u'\u2839'
    elif (T == (1,1,0,1,0,1,0,1)):
        return u'\u28B9'
    elif (T == (1,1,0,1,0,1,1,0)):
        return u'\u2879'
    elif (T == (1,1,0,1,0,1,1,1)):
        return u'\u28F9'
    elif (T == (1,1,0,1,1,0,0,0)):
        return u'\u281D'
    elif (T == (1,1,0,1,1,0,0,1)):
        return u'\u289D'
    elif (T == (1,1,0,1,1,0,1,0)):
        return u'\u285D'
    elif (T == (1,1,0,1,1,0,1,1)):
        return u'\u28DD'
    elif (T == (1,1,0,1,1,1,0,0)):
        return u'\u283D'
    elif (T == (1,1,0,1,1,1,0,1)):
        return u'\u28BD'
    elif (T == (1,1,0,1,1,1,1,0)):
        return u'\u287D'
    elif (T == (1,1,0,1,1,1,1,1)):
        return u'\u28FD'
    elif (T == (1,1,1,0,0,0,0,0)):
        return u'\u280B'
    elif (T == (1,1,1,0,0,0,0,1)):
        return u'\u282B'
    elif (T == (1,1,1,0,0,0,1,0)):
        return u'\u284B'
    elif (T == (1,1,1,0,0,0,1,1)):
        return u'\u28CB'
    elif (T == (1,1,1,0,0,1,0,0)):
        return u'\u282B'
    elif (T == (1,1,1,0,0,1,0,1)):
        return u'\u28AB'
    elif (T == (1,1,1,0,0,1,1,0)):
        return u'\u286B'
    elif (T == (1,1,1,0,0,1,1,1)):
        return u'\u28EB'
    elif (T == (1,1,1,0,1,0,0,0)):
        return u'\u280F'
    elif (T == (1,1,1,0,1,0,0,1)):
        return u'\u288F'
    elif (T == (1,1,1,0,1,0,1,0)):
        return u'\u284F'
    elif (T == (1,1,1,0,1,0,1,1)):
        return u'\u28CF'
    elif (T == (1,1,1,0,1,1,0,0)):
        return u'\u282F'
    elif (T == (1,1,1,0,1,1,0,1)):
        return u'\u28AF'
    elif (T == (1,1,1,0,1,1,1,0)):
        return u'\u286F'
    elif (T == (1,1,1,0,1,1,1,1)):
        return u'\u28EF'
    elif (T == (1,1,1,1,0,0,0,0)):
        return u'\u281B'
    elif (T == (1,1,1,1,0,0,0,1)):
        return u'\u289B'
    elif (T == (1,1,1,1,0,0,1,0)):
        return u'\u285B'
    elif (T == (1,1,1,1,0,0,1,1)):
        return u'\u28DB'
    elif (T == (1,1,1,1,0,1,0,0)):
        return u'\u283B'
    elif (T == (1,1,1,1,0,1,0,1)):
        return u'\u28BB'
    elif (T == (1,1,1,1,0,1,1,0)):
        return u'\u287B'
    elif (T == (1,1,1,1,0,1,1,1)):
        return u'\u28FB'
    elif (T == (1,1,1,1,1,0,0,0)):
        return u'\u281F'
    elif (T == (1,1,1,1,1,0,0,1)):
        return u'\u289F'
    elif (T == (1,1,1,1,1,0,1,0)):
        return u'\u285F'
    elif (T == (1,1,1,1,1,0,1,1)):
        return u'\u28DF'
    elif (T == (1,1,1,1,1,1,0,0)):
        return u'\u283F'
    elif (T == (1,1,1,1,1,1,0,1)):
        return u'\u28BF'
    elif (T == (1,1,1,1,1,1,1,0)):
        return u'\u287F'
    else:
        return u'\u28FF'


    pass##print(u'\u0123')
if(len(sys.argv) < 4 or len(sys.argv) > 4):
    print("wrong number of arguments ")
    exit(-1);
imageFile = sys.argv[3]
treshold = int(sys.argv[2])
binearization = bool(sys.argv[1])
def bin(pixel):
    #print(pixel)
    if(not binearization):
        return pixel
    else:
        if(pixel[1] > treshold and pixel[2] > treshold and pixel[0] > treshold):
            return 1
        else:
            return 0


im = Image.open(imageFile)
file = open("image.txt", "w",encoding="utf-8")
base = 33
width = base*2 + base-1
heigh =  int((width*im.height)/im.width)
print("wid = "+str(width)+ " heig = "+str(heigh))
im = im.resize((width,heigh))
im = im.convert('RGB')

#Applying a filter to the image
if(not binearization):
    im = im.filter(ImageFilter.FIND_EDGES)
dat = u''
gaprows = 6;
gapcols = 3
for rows in range(heigh):
    if(rows*gaprows > heigh or rows*gaprows +1> heigh or rows*gaprows +2> heigh or rows*gaprows +3> heigh or rows*gaprows +4> heigh or rows*gaprows +5> heigh):
        break
    for col in range(base):
        pixelr11 = bin(im.getpixel((col*gapcols, rows*gaprows)))
        pixelr12 = bin(im.getpixel((col*gapcols + 1, rows*gaprows)))
        pixelr21 = bin(im.getpixel((col*gapcols, rows*gaprows+1)))
        pixelr22 = bin(im.getpixel((col*gapcols + 1, rows*gaprows+1)))
        pixelr31 = bin(im.getpixel((col*gapcols, rows*gaprows+2)))
        pixelr32 = bin(im.getpixel((col*gapcols + 1, rows*gaprows+2)))
        pixelr41 = bin(im.getpixel((col*gapcols, rows*gaprows+3)))
        pixelr42 = bin(im.getpixel((col*gapcols + 1, rows*gaprows+3)))
        char = getchar((pixelr11, pixelr12,pixelr21,pixelr22,pixelr31,pixelr32,pixelr41,pixelr42))
        dat = dat + char
    file.write(dat+'\n')
    dat = u''
im.show()
file.close()
