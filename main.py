from templates import article1, article2,  article3, article4, article5, article6, loops
import submitWP
import random
from primeFactorVisualizer import generateImages
from datetime import timedelta, datetime


def schedule(current_time):
    # tdelta = timedelta(minutes=random.randrange(3, 9))
    # current_time = current_time + tdelta
    hour = str(current_time.hour)
    minute = str(current_time.minute)
    second = str(current_time.second)
    if len(hour) == 1:
        hour = f"0{hour}"
    if len(minute) == 1:
        minute = f"0{minute}"
    if len(second) == 1:
        second = f"0{second}"
    return f"{current_time.date()}T{hour}:{minute}:{second}"


# n = 10365
current_time = datetime.now()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 539, 540, 542, 543, 544, 545, 546, 548, 549, 550, 551, 552, 553, 555, 557, 558, 559, 560, 561, 562, 563, 564, 566, 567, 568, 569, 570, 572, 573, 574, 575, 576, 577, 578, 580, 581, 582, 584, 585, 586, 588, 589, 590, 592, 594, 595, 596, 598, 599, 600, 602, 603, 605, 608, 609, 610, 612, 614, 615, 616, 617, 618, 620, 621, 623, 624, 625, 626, 627, 628, 629, 630, 635, 636, 637, 638, 639, 640, 644, 645, 646, 648, 650, 651, 652, 654, 655, 656, 657, 658, 660, 661, 663, 664, 665, 666, 667, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 682, 683, 684, 685, 686, 688, 690, 692, 693, 694, 696, 697, 699, 700, 702, 703, 704, 705, 710, 711, 712, 713, 714, 715, 716, 720, 721, 722, 723, 725, 726, 728, 729, 730, 731, 732, 733, 734, 735, 736, 738, 740, 741, 742, 744, 745, 747, 748, 749, 750, 751, 752, 753, 754, 756, 759, 760, 764, 765, 768, 770, 773, 774, 775, 776, 777, 780, 781, 782, 783, 784, 785, 786, 789, 790, 792, 793, 795, 796, 799, 800, 801, 803, 805, 806, 808, 810, 812, 813, 814, 816, 817, 818, 819, 820, 821, 822, 824, 825, 826, 828, 829, 832, 833, 834, 835, 836, 837, 840, 841, 845, 846, 847, 848, 850, 851, 852, 854, 855, 856, 857, 858, 859, 860, 861, 864, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 880, 881, 882, 884, 885, 886, 887, 888, 890, 891, 892, 893, 894, 896, 897, 899, 900, 901, 902, 903, 904, 908, 909, 910, 912, 913, 914, 917, 918, 920, 921, 923, 924, 925, 926, 927, 930, 931, 935, 936, 937, 940, 941, 942, 943, 944, 945, 946, 948, 949, 950, 952, 954, 956, 957, 958, 960, 961, 963, 967, 968, 969, 970, 971, 972, 973, 975, 976, 978, 979, 980, 981, 984, 986, 987, 988, 989, 990, 994, 996, 998, 999, 1000, 1001, 1002, 1003, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1020, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1035, 1036, 1040, 1042, 1044, 1045, 1046, 1048, 1050, 1053, 1054, 1056, 1057, 1058, 1064, 1073, 1078, 1079, 1080, 1081, 1082, 1083, 1085, 1088, 1089, 1090, 1092, 1093, 1094, 1096, 1098, 1100, 1104, 1105, 1107, 1110, 1111, 1112, 1113, 1115, 1116, 1117, 1120, 1121, 1122, 1124, 1125, 1127, 1128, 1129, 1130, 1131, 1133, 1134, 1140, 1141, 1144, 1146, 1147, 1150, 1151, 1152, 1154, 1155, 1156, 1157, 1161, 1163, 1170, 1173, 1175, 1176, 1183, 1188, 1190, 1192, 1196, 1197, 1198, 1199, 1200, 1201, 1204, 1205, 1207, 1208, 1209, 1210, 1212, 1215, 1218, 1219, 1220, 1221, 1224, 1225, 1230, 1232, 1234, 1235, 1236, 1237, 1240, 1241, 1242, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1258, 1260, 1261, 1265, 1267, 1269, 1274, 1275, 1276, 1280, 1282, 1283, 1284, 1285, 1287, 1288, 1289, 1290, 1291, 1295, 1296, 1298, 1300, 1301, 1304, 1305, 1309, 1313, 1314, 1320, 1321, 1323, 1325, 1326, 1329, 1330, 1331, 1336, 1337, 1350, 1352, 1353, 1358, 1360, 1362, 1365, 1368, 1369, 1372, 1375, 1376, 1377, 1378, 1379, 1380, 1384, 1386, 1391, 1394, 1396, 1400, 1402, 1404, 1408, 1412, 1425, 1430, 1432, 1435, 1440, 1441, 1444, 1445, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1463, 1470, 1472, 1474, 1475, 1476, 1480, 1482, 1484, 1485, 1489, 1500, 1501, 1505, 1512, 1517, 1520, 1521, 1530, 1532, 1534, 1535, 1536, 1538, 1539, 1540, 1543, 1544, 1545, 1547, 1548, 1550, 1551, 1553, 1556, 1560, 1564, 1566, 1567, 1568, 1569, 1573, 1575, 1581, 1582, 1584, 1585, 1586, 1587, 1589, 1591, 1595, 1597, 1600, 1601, 1604, 1606, 1607, 1612, 1617, 1620, 1624, 1625, 1632, 1638, 1645, 1650, 1651, 1657, 1664, 1665, 1680, 1681, 1682, 1683, 1684, 1687, 1690, 1692, 1694, 1697, 1700, 1701, 1705, 1709, 1711, 1715, 1716, 1722, 1724, 1726, 1728, 1729, 1739, 1740, 1745, 1748, 1749, 1750, 1751, 1754, 1755, 1760, 1763,
           1764, 1768, 1771, 1784, 1787, 1800, 1801, 1804, 1820, 1821, 1827, 1829, 1830, 1835, 1836, 1845, 1847, 1848, 1849, 1850, 1855, 1859, 1860, 1862, 1863, 1866, 1869, 1870, 1871, 1872, 1875, 1881, 1883, 1890, 1892, 1895, 1898, 1899, 1900, 1904, 1905, 1911, 1920, 1922, 1925, 1935, 1936, 1938, 1940, 1950, 1951, 1955, 1957, 1959, 1960, 1961, 1963, 1964, 1969, 1980, 1981, 1982, 1984, 1985, 1986, 1987, 1988, 1989, 1996, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2028, 2030, 2031, 2032, 2033, 2034, 2037, 2040, 2041, 2043, 2046, 2047, 2048, 2055, 2065, 2079, 2084, 2090, 2100, 2108, 2112, 2115, 2116, 2120, 2121, 2125, 2142, 2145, 2156, 2160, 2165, 2166, 2178, 2180, 2181, 2187, 2197, 2199, 2200, 2205, 2209, 2222, 2233, 2240, 2244, 2250, 2256, 2259, 2268, 2295, 2300, 2304, 2310, 2311, 2312, 2323, 2340, 2370, 2376, 2385, 2400, 2401, 2420, 2424, 2425, 2429, 2430, 2431, 2432, 2435, 2437, 2440, 2441, 2443, 2444, 2446, 2447, 2448, 2449, 2450, 2452, 2457, 2458, 2470, 2472, 2475, 2476, 2477, 2480, 2481, 2483, 2485, 2487, 2489, 2500, 2509, 2520, 2521, 2523, 2525, 2527, 2535, 2540, 2541, 2548, 2550, 2555, 2560, 2574, 2584, 2592, 2600, 2601, 2618, 2625, 2639, 2640, 2645, 2646, 2648, 2668, 2673, 2695, 2700, 2701, 2704, 2730, 2736, 2744, 2750, 2772, 2800, 2805, 2808, 2809, 2835, 2846, 2862, 2865, 2873, 2880, 2884, 2887, 2888, 2889, 2904, 2907, 2911, 2916, 2925, 2926, 2937, 2940, 2943, 2970, 2975, 2990, 2996, 3000, 3003, 3008, 3010, 3024, 3025, 3042, 3072, 3080, 3087, 3091, 3100, 3105, 3121, 3125, 3127, 3131, 3136, 3150, 3155, 3156, 3168, 3190, 3200, 3220, 3232, 3234, 3240, 3249, 3250, 3267, 3289, 3300, 3328, 3332, 3333, 3341, 3360, 3364, 3367, 3375, 3376, 3380, 3400, 3409, 3430, 3432, 3443, 3450, 3456, 3458, 3465, 3468, 3481, 3500, 3510, 3519, 3528, 3537, 3549, 3551, 3578, 3600, 3610, 3611, 3615, 3616, 3630, 3633, 3636, 3640, 3642, 3645, 3647, 3648, 3649, 3650, 3654, 3655, 3656, 3657, 3658, 3675, 3678, 3698, 3699, 3721, 3737, 3740, 3750, 3753, 3780, 3800, 3825, 3836, 3840, 3844, 3850, 3857, 3861, 3895, 3920, 3927, 3960, 3969, 3993, 4000, 4001, 4004, 4040, 4050, 4052, 4056, 4058, 4077, 4085, 4095, 4096, 4116, 4141, 4200, 4205, 4224, 4225, 4239, 4275, 4290, 4320, 4321, 4335, 4356, 4358, 4400, 4401, 4410, 4420, 4431, 4488, 4489, 4500, 4509, 4554, 4563, 4577, 4608, 4620, 4624, 4641, 4680, 4681, 4725, 4752, 4760, 4761, 4800, 4802, 4825, 4844, 4845, 4848, 4851, 4900, 4907, 4913, 4935, 4937, 4949, 4950, 4968, 5000, 5002, 5005, 5010, 5040, 5041, 5045, 5046, 5064, 5068, 5120, 5125, 5132, 5184, 5200, 5250, 5269, 5280, 5292, 5320, 5324, 5328, 5329, 5346, 5348, 5352, 5353, 5390, 5400, 5404, 5423, 5445, 5454, 5460, 5461, 5472, 5476, 5488, 5500, 5516, 5525, 5544, 5555, 5565, 5572, 5600, 5607, 5610, 5616, 5625, 5733, 5736, 5760, 5775, 5776, 5784, 5800, 5832, 5855, 5880, 5889, 5904, 5915, 5929, 5940, 5952, 5992, 5993, 6000, 6006, 6024, 6030, 6048, 6050, 6075, 6084, 6125, 6174, 6195, 6200, 6241, 6250, 6273, 6292, 6298, 6300, 6312, 6318, 6370, 6400, 6435, 6468, 6480, 6497, 6517, 6552, 6561, 6574, 6600, 6624, 6630, 6655, 6724, 6741, 6750, 6760, 6768, 6781, 6804, 6825, 6859, 6886, 6889, 6912, 6930, 7000, 7007, 7020, 7056, 7098, 7122, 7171, 7182, 7200, 7203, 7225, 7280, 7281, 7285, 7289, 7290, 7291, 7325, 7344, 7350, 7380, 7396, 7425, 7429, 7442, 7480, 7500, 7546, 7560, 7569, 7575, 7600, 7605, 7623, 7688, 7700, 7744, 7752, 7776, 7777, 7795, 7803, 7875, 7919, 7920, 7921, 7956, 7999, 8000, 8008, 8020, 8085, 8100, 8134, 8181, 8191, 8192, 8232, 8240, 8250, 8281, 8303, 8316, 8352, 8400, 8450, 8464, 8470, 8496, 8575, 8590, 8602, 8624, 8640, 8649, 8712, 8748, 8775, 8784, 8787, 8788, 8800, 8820, 8827, 8836, 8878, 8888, 8911, 8928, 9000, 9009, 9017, 9025, 9072, 9075, 9100, 9118, 9191, 9197, 9200, 9216, 9248, 9255, 9261, 9264, 9295, 9317, 9327, 9375, 9408, 9409, 9438, 9450, 9500, 9504, 9550, 9600, 9604, 9648, 9720, 9797, 9800, 9801, 9900, 9945, 9999, 10000, 10001, 10010, 10012, 10013, 10101, 10125, 10140, 10201, 10290, 10296, 10404, 10459, 10500, 10530, 10584, 10626, 10648, 10800, 10829, 10985, 11000, 11011, 11025, 11045, 11094, 11109, 11111, 11154, 11200, 11236, 11340, 11449, 11466, 11475, 11500, 11543, 11550, 11664, 11704, 11730, 11760, 11767, 11900, 11979, 12000, 12005, 12100, 12121, 12150, 12156, 12158, 12167, 12197, 12321, 12345, 12375, 12500, 12544, 12576, 12600, 12636, 12650, 12673, 12696, 12800, 12809, 12870, 12920, 12960, 13000, 13225, 13475, 13500, 13718, 13824, 13832, 13860, 13915, 13923, 14000, 14295, 14300, 14364, 14400, 14406, 14443, 14586, 14641, 14700, 14739, 15000, 15005, 15015, 15125, 15129, 15288, 15376, 15379, 15422, 15428, 15470, 15552, 15581, 15623, 15625, 15628, 15635, 15840, 15876, 16000, 16200, 16244, 16302, 16320, 16384, 16500, 16524, 16562, 16575, 16641, 16807, 16830, 17000, 17017, 17161, 17280, 17424, 17496, 17550, 17576, 17640, 17664, 17943, 18000, 18088, 18162, 18207, 18225, 18711, 18925, 19000, 19345, 19500, 19600, 19652, 19671, 19681, 19683, 19800, 19941, 20000, 20160, 20449, 20480, 20570, 20577, 20736, 21000, 21021, 21175, 21252, 21658, 21952, 22032, 22050, 22356, 22400, 22500, 23000, 23150, 23805, 24000, 24167, 24300, 24336, 24344, 24389, 24696, 24843, 24871, 25000, 25200, 25339, 25600, 26136, 26244, 27000, 27225, 27300, 27540, 27648, 27720, 27783, 28000, 28224, 28672, 28709, 28812, 28829, 28900, 29241, 29400, 29645, 29791, 30000, 30030, 30031, 30600, 31000, 32400, 32760, 32768, 33033, 33592, 33600, 34596, 35000, 35035, 35100, 35233, 35280, 35700, 35937, 35964, 36000, 36036, 36100, 36864, 38220, 39039, 39204, 39304, 40000, 40002, 40320, 40401, 40898, 41405, 42000, 42025, 42875, 43225, 43350, 44100, 45000, 45056, 45617, 46656, 47089, 50000, 50625, 52488, 52920, 53240, 54000, 54054, 54872, 55055, 56100, 56644, 58500, 58752, 59049, 59319, 59400, 60000, 60025, 61200, 61347, 62500, 63504, 64000, 64009, 64827, 65065, 65520, 65536, 65537, 66049, 66339, 68600, 68921, 69192, 69696, 69810, 69839, 70000, 70840, 71289, 72000, 72500, 72501, 72600, 73441, 74088, 75600, 77000, 77077, 79380, 85085, 85184, 85800, 86900, 87120, 88200, 91125, 91800, 92169, 97336, 99856, 99999]

for i in range(0, len(numbers)):
    n = numbers[i]
    treeImages = generateImages(n)['TreeFiles']
    divisionImages = generateImages(n)['DivisionFiles']
    bannerImages = generateImages(n)['Banners']
    p1 = article1.Post(n)
    p2 = article2.Post(n)
    p3 = article3.Post(n)
    p4 = article4.Post(n)
    p5 = article5.Post(n)
    p6 = article6.Post(n)
    posts = [p1, p2, p3, p4, p5, p6]

    title = random.choice(posts).title
    intro = random.choice(posts).intro
    theory = random.choice(posts).theory
    formula = random.choice(posts).formula
    howtocalculatelist = random.choice(posts).howtocalculatelist
    factorTree = random.choice(posts).factorTree
    factorTreeSteps = loops.FactorTreeMethod(
        n, numbers, i, treeImages).factorTreeSteps()
    division = random.choice(posts).division
    divisionSteps = loops.DivisionMethod(
        n, numbers, i, divisionImages).divisionSteps()
    extra1 = random.choice(posts).extra1
    extra2 = random.choice(posts).extra2
    faq = random.choice(posts).FAQ

    # content = intro + theory + howtocalculatelist + factorTree + factorTreeSteps
    content = f"{intro}{theory}{formula}{howtocalculatelist}{factorTree}{factorTreeSteps}{division}{divisionSteps}{extra1}{extra2}{faq}"

    tdelta = timedelta(minutes=random.randrange(10, 20))
    current_time = current_time + tdelta
    time = schedule(current_time)

    WPrequest = submitWP.submit(title, n, content, time, bannerImages)
    print(f"Number - {i+1} is scheduled at {time} with {WPrequest}")
